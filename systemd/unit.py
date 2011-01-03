import dbus

from systemd.property import Property

class Unit(object):
    """Abstraction class to org.freedesktop.systemd1.Unit interface"""
    def __init__(self, unit_path):
        self.__bus = dbus.SystemBus()
        self.__proxy = self.__bus.get_object(
            'org.freedesktop.systemd1',
            unit_path,
        )
        self.__interface = dbus.Interface(
            self.__proxy,
            'org.freedesktop.systemd1.Unit',
        )
        self.__properties()

    def __properties(self):
        interface = dbus.Interface(
            self.__proxy,
            'org.freedesktop.DBus.Properties')
        properties = interface.GetAll(self.__interface.dbus_interface)
        attr_property =  Property()
        for key, value in properties.items():
            setattr(attr_property, key, value)
        setattr(self, 'properties', attr_property)

    def kill(self, who, mode, signal):
        self.__interface.Kill(who, mode, signal)

    def reload(self, mode):
        job_path = self.__interface.Reload(mode)
        return str(job_path)

    def reload_or_restart(self, mode):
        job_path = self.__interface.ReloadOrRestart(mode)
        return str(job_path)

    def reload_or_try_restart(self, mode):
        job_path = self.__interface.ReloadOrTryRestart(mode)
        return str(job_path)

    def reset_failed(self):
        self.__interface.ResetFailed()

    def restart(self, mode):
        job_path = self.__interface.Restart(mode)
        return str(job_path)

    def start(self, mode):
        job_path = self.__interface.Start(mode)
        return str(job_path)

    def stop(self, mode):
        job_path = self.__interface.Stop(mode)
        return str(job_path)

    def try_restart(self,mode):
        job_path = self.__interface.TryRestart(mode)
        return str(job_path)

class UnitInfo(object):
    def __init__(self):
        self.id = None
        self.description = None
        self.load_state = None
        self.active_state = None
        self.sub_state = None
        self.following = None
        self.unit_path = None
        self.job_id = None
        self.job_type = None
        self.job_path = None