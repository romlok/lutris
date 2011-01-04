# -*- coding:Utf-8 -*-
#
#  Copyright (C) 2010 Mathieu Comandon <strider@strycore.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys

name = "Lutris"
version = "0.2.2"
website = "http://lutris.net"
protocol_version = 1
installer_prefix = "http://lutris.net/media/installers/"
#installer_prefix = "http://localhost:8000/media/installers/"
CONFIG_EXTENSION = ".yml"
license = 'GPL-3'
copyright = "(c) 2010 Lutris Gaming Platform"
authors = ["Mathieu Comandon <strycore@gmail.com>"]
artists = ["Ludovic Soulié <contact@yudoh.com>"]
license = """
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """
#Paths

LAUNCH_PATH = os.path.abspath(sys.path[0])
print "LP : ", LAUNCH_PATH
if not LAUNCH_PATH.startswith('/usr'):
    DATA_PATH = os.path.join(sys.path[0], '..','data')
else:
    DATA_PATH = '/usr/share/lutris'
if not os.path.exists(DATA_PATH):
    print "DATA_PATH can't be found at : %s" % DATA_PATH
lutris_icon_file = "media/logo.svg"
lutris_icon_path = os.path.join(DATA_PATH, lutris_icon_file)

lutris_config_path = os.path.join(os.path.expanduser('~'), '.config', 'lutris')
system_config_file = 'system' + CONFIG_EXTENSION
system_config_full_path = os.path.join(lutris_config_path, system_config_file)
runner_config_path = os.path.join(lutris_config_path, 'runners')
GAME_CONFIG_PATH = os.path.join(lutris_config_path, 'games')
COVER_PATH = os.path.join(lutris_config_path, 'covers')
tmp_path = os.path.join(lutris_config_path, 'tmp')
TMP_PATH = tmp_path
cache_path = os.path.join(lutris_config_path, 'cache')

