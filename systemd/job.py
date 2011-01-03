import dbus

from systemd.property import Property

#TODO: Implement org.freedesktop.DBus.Properties signals for it interface

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