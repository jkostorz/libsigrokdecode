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

ori = {

    0x002:  'Amplifier volume up',
    0x003:  'Amplifier volume down',
    0x004:  'Amplifier power toggle',
    0x005:  'Amplifier mute toggle',
    0x020:  'Amplifier input CD',
    0x02f:  'Amplifier power on',
    0x070:  'Amplifier input TAPE',
    0x0d5:  'Amplifier source next',
    0x0d6:  'Amplifier source previous',
    0x0d7:  'Amplifier mute on (sound off)',
    0x0d8:  'Amplifier mute off (sound on)',
    0x0d9:  'Amplifier power on',
    0x0da:  'Amplifier power off',
    0x0e0:  'Amplifier input 2',
    0x0e9:  'Amplifier on',
    0x0ea:  'All off',
    0x0ef:  'Amplifier ready',
    0x0fb:  'Amplifier power on',

    0x120:  'Amplifier input DVD',
    0x170:  'Amplifier input HDD',
    0x17f:  'Amplifier power on',
    0x1a0:  'Amplifier input VIDEO2',
    0x1a2:  'Amplifier volume up',
    0x1a3:  'Amplifier volume down',
    0x1a4:  'Amplifier mute on (sound off)',
    0x1a5:  'Amplifier mute off (sound on)',
    0x1ae:  'Amplifier power off',
    0x1af:  'Amplifier power on',
    0x1b0:  'Dimmer or power button',
    0x1b1:  'Dimmer or power button',
    0x1b2:  'Dimmer or power button',

    0x2b0:  'Amplifier display dim max',
    0x2b1:  'Amplifier display dim mid',
    0x2b2:  'Amplifier display dim min',
    0x2b8:  'Amplifier display dim day',
    0x2bf:  'Amplifier display dim night',

    0x420:  'Amplifier service mode off',
    0x421:  'Amplifier service mode 1',
    0x422:  'Amplifier service mode 2',
    0x423:  'Amplifier service mode 3',
    0x424:  'Amplifier service mode 4',
    0x425:  'Amplifier service mode 5',
    0x426:  'Amplifier service mode 6',
    0x427:  'Amplifier service mode 7',
    0x428:  'Amplifier service mode 8',
    0x429:  'Amplifier service mode 9',
    0x42a:  'Amplifier service mode A',
    0x42b:  'Amplifier service mode B',
    0x42c:  'Amplifier service mode C',
    0x42d:  'Amplifier service mode D',
    0x42e:  'Amplifier service mode E',
    0x4a0:  'Service mode ACK',
    0x4a3:  'Unknown code 0x4A3',
    0x4a6:  'Unknown code 0x4A6',
    0x4aa:  'Unknown codei 0x4AA',

    0x521:  'HDD stop',
    0x595:  'HDD return',
    0x59d:  'HDD input',
    0x5c2:  'HDD up',
    0x5c3:  'HDD down',
    0x5c8:  'HDD next',
    0x5c9:  'HDD previous',
    0x5cb:  'HDD play',
    0x5d2:  'HDD shuffle',
    0x5d3:  'HDD repeat',
    0x5d5:  'HDD display',
    0x5d6:  'HDD menu',
    0x5d7:  'HDD enter',

    0xaa0:  'Amplifier VIDEO 1 stop',
    0xaa1:  'Amplifier mute',
    0xaa2:  'Amplifier VIDEO 2 stop',
    0xaae:  'Unknown code 0xAAE',
    0xaaf:  'Unknown code 0xAAF',

    0xc00:  'Tuner next',
    0xc01:  'Tuner previous',
    0xc06:  'Tuner input',
    0xc07:  'Tuner display',
    0xc21:  'Tuner stop',
    0xc4d:  'Tuner enter',
    0xc82:  'Tuner up',
    0xc83:  'Tuner down',
    0xc84:  'Tuner left',
    0xc85:  'Tuner right',
    0xc93:  'Tuner menu',
    0xc95:  'Tuner return',
    0xcd0:  'Tuner play',
    0xcd8:  'Tuner repeat',
    0xcd9:  'Tuner shuffle',

    0xd13:  'Stop',
    0xd15:  'Play',
    0xd16:  'Pause',
    0xd19:  'Forward',
    0xd1a:  'Rewind',

    0xf00:  'CD forward',
    0xf01:  'CD rewind',
    0xf04:  'CD on',
    0xf06:  'CD repeat',
    0xf08:  'CD clear',
    0xf09:  'CD memory',
    0xf0a:  'CD display',
    0xf0b:  'CD eject',
    0xf0c:  'CD 8',
    0xf0d:  'CD 9',
    0xf0e:  'CD 0',
    0xf0f:  'CD digits',
    0xf10:  'CD 1',
    0xf11:  'CD 2',
    0xf12:  'CD 3',
    0xf13:  'CD 4',
    0xf18:  'CD 5',
    0xf19:  'CD 6',
    0xf1a:  'CD 7',
    0xf1b:  'CD play',
    0xf1c:  'CD stop',
    0xf1d:  'CD next',
    0xf1e:  'CD prev',
    0xf1f:  'CD pause',
    0xf21:  'CD stop',
    0xf40:  'CD up',
    0xf41:  'CD down',
    0xf42:  'CD right',
    0xf43:  'CD left',
    0xf46:  'CD random',
    0xf5c:  'CD channel up',
    0xf5f:  'CD channel down',
    0xf8d:  'CD enter',
    0xf8f:  'CD standby',
    0xf92:  'CD return',
    0xfc3:  'CD input',
    0xfcf:  'CD menu',

}
