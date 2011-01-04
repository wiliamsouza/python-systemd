#
# Copyright (c) 2010 Mandriva
#
# This file is part of python-systemd.
#
# python-systemd is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 2.1 of
# the License, or (at your option) any later version.
#
# python-systemd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

class SystemdError(Exception):
    def __init__(self, error):
        self.name = error.get_dbus_name().split('.')[3]
        self.message = error.get_dbus_message()

    def __str__(self):
        return '%s(%s)' % (self.name, self.message)

    def __repr__(self):
        return '%s(%s)' % (self.name, self.message)