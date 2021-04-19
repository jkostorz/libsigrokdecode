#
#   ©2021 Janusz Kostorz
#   All rights reserved.
#
#   This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#   See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses/>.
#

import sigrokdecode as srd
from common.srdhelper import bitpack


class SamplerateError(Exception):
    pass


class Pin:
    JURA, = range(1)


class Ann:
    Raw, Code, = range(2)


class Decoder(srd.Decoder):
    api_version = 3
    id = 'jura'
    name = 'JURA'
    longname = 'Coffee machine JURA'
    desc = 'Serial service protocol for the JURA coffee machine'
    license = 'gplv2+'
    inputs = ['logic']
    outputs = []
    tags = ['JURA']
    channels = ({'id': 'jura', 'name': 'JURA', 'desc': 'service connector'}, )
    options = ()
    annotations = (
        ('raw', 'Raw'),
        ('code', 'Code'),
    )
    annotation_rows = (
        ('raw', 'Raw', (Ann.Raw, )),
        ('code', 'Code', (Ann.Code, )),
    )

    def __init__(self):
        self.reset()

    def start(self):
        self.bitt = int(self.samplerate * 104166666e-12)  # One bit time
        self.halft = int(self.samplerate * 52083333e-12)  # Half bit time
        self.bytet = int(self.samplerate * 104166666e-11)  # Full byte time
        self.idle = int(self.samplerate * 10e-3)  # Idle time
        self.anchor = self.register(srd.OUTPUT_ANN)  # Anchor for outputs

    def reset(self):
        self.state = 'Raw'
        self.samplenum_bit = self.samplenum_code = 0
        self.raw = self.code = []

    def metadata(self, key, value):
        if key == srd.SRD_CONF_SAMPLERATE:
            self.samplerate = value

    def decode(self):

        # Wait for samples
        if not self.samplerate:
            raise SamplerateError('No input data')

        # Main
        while True:

            # Wait for start
            self.jura, = self.wait({Pin.JURA: 'f'})

            # Init setup
            self.raw = []
            self.samplenum_bit = self.samplenum
            if len(self.code) == 0:
                self.samplenum_code = self.samplenum
            self.wait({'skip': (self.halft)})

            # Long idle reset
            space = self.samplenum - self.samplenum_bit
            if self.state != 'Stop' and space > self.idle:
                self.reset()

            # Raw bits
            if self.state == 'Raw':

                # Read serial, extract code
                for b in range(8):
                    self.jura, = self.wait({'skip': self.bitt})
                    self.raw.append(self.jura)
                    if b == 2 or b == 5:
                        self.code.append(self.jura)

                # Generate raw bits
                bits = bitpack(self.raw)
                self.put(self.samplenum_bit, self.samplenum_bit + self.bytet,
                         self.anchor, [Ann.Raw, ['0b{0:08b}'.format(bits)]])

                # Wait for half of stop bit
                self.wait({'skip': self.bitt})

                # Code ready
                if len(self.code) == 8:
                    self.samplenum_end = self.samplenum_bit + self.bytet
                    self.state = 'Code'

            # Code
            if self.state == 'Code':

                # Generate hex
                self.hex = bitpack(self.code)

                # Generate ascii
                if self.hex == 10:
                    ascii = ', LF (line feed)'
                elif self.hex == 13:
                    ascii = ', CR (carriage return)'
                elif self.hex == 32:
                    ascii = ', SPACE'
                elif self.hex > 32 and self.hex < 127:
                    ascii = ', Ascii: ' + chr(self.hex)
                else:
                    ascii = ', Ascii: non printable'
                f = 'Hex: 0x{{:0{}X}}'.format(2)
                self.put(self.samplenum_code, self.samplenum_end, self.anchor,
                         [Ann.Code, [f.format(self.hex) + ascii]])

                # Done
                self.reset()
