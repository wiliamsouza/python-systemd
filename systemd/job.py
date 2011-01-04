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

import dbus

from systemd.property import Property

class Job(object):
    """Abstraction class to org.freedesktop.systemd1.Job interface"""
    def __init__(self, job_path):
        self.__bus = dbus.SystemBus()
        self.__proxy = self.__bus.get_object(
            'org.freedesktop.systemd1',
            job_path,
        )
        self.__interface = dbus.Interface(
            self.__proxy,
            'org.freedesktop.systemd1.Job',
        )
        #self.__properties()

    def __properties(self):
        #TODO: Fix it, way Job interface not have properties
        interface = dbus.Interface(
            self.__proxy,
            'org.freedesktop.DBus.Properties')
        properties = interface.GetAll(self.__interface.dbus_interface)
        attr_property =  Property()
        for key, value in properties.items():
            setattr(attr_property, key, value)
        setattr(self, 'properties', attr_property)

    def cancel(self):
        self.__interface.Cancel()

class JobInfo(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.type = None
        self.state = None
        self.job_path = None
        self.unit_path = None