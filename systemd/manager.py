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
import dbus.mainloop.glib
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

from systemd.unit import Unit
from systemd.job import Job
from systemd.property import Property
from systemd.exceptions import SystemdError

class Manager(object):
    """Abstraction class to org.freedesktop.systemd1.Manager interface"""
    def __init__(self):
        self.__bus = dbus.SystemBus()
        self.__proxy = self.__bus.get_object(
            'org.freedesktop.systemd1',
            '/org/freedesktop/systemd1')

        self.__interface = dbus.Interface(
            self.__proxy,
            'org.freedesktop.systemd1.Manager')

        self.subscribe()

        self.__properties_interface = dbus.Interface(
            self.__proxy,
            'org.freedesktop.DBus.Properties')

        self.__properties_interface.connect_to_signal(
            'PropertiesChanged',
            self.__on_properties_changed)

        self.__properties()

    def __on_properties_changed(self, *args, **kargs):
        self.__properties()

    def __properties(self):
        properties = self.__properties_interface.GetAll(
            self.__interface.dbus_interface)
        attr_property =  Property()
        for key, value in properties.items():
            setattr(attr_property, key, value)
        setattr(self, 'properties', attr_property)

    def clear_jobs(self):
        try:
            self.__interface.ClearJobs()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def create_snapshot(self, name, cleanup):
        try:
            snapshot_path = self.__interface.CreateSnapshot(name, cleanup)
            return str(snapshot_path)
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def dump(self):
        try:
            self.__interface.Dump()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def exit(self):
        try:
            self.__interface.Exit()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def get_job(self, ID):
        """Get job by it ID.
        
        @param ID: Job ID.
        
        @raise SystemdError: Raised when no job is found with the given ID.
        
        @rtype: systemd.job.Job
        """
        try:
            job_path = self.__interface.GetJob(ID)
            job = Job(job_path)
            return job
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def get_unit(self, name):
        """Get unit by it name.
        
        @param name: Unit name (ie: network.service).
        
        @raise SystemdError: Raised when no unit is found with the given name.
        
        @rtype: systemd.unit.Unit
        """
        try:
            unit_path = self.__interface.GetUnit(name)
            unit = Unit(unit_path)
            return unit
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def get_unit_by_pid(self, pid):
        """Get unit by it PID.
        
        @param PID: Unit PID.
        
        @raise SystemdError: Raised when no unit with that PID is found.
        
        @rtype: systemd.unit.Unit
        """
        try:
            unit_path = self.__interface.GetUnitByPID(pid)
            unit = Unit(unit_path)
            return unit
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def halt(self):
        try:
            self.__interface.Halt()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def k_exec(self):
        try:
            self.__interface.KExec()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)
    
    def kill_unit(self, name, who, mode, signal):
        """Kill unit.
        
        @param name: Unit name (ie: network.service).
        @param who: Must be one of main, control or all.
        @param mode: Must be one of control-group, process-group, process.
        @param signal: Must be one of the well know signal number such  as
        SIGTERM(15), SIGINT(2), SIGSTOP(19) or SIGKILL(9).
        
        @raise SystemdError: Raised when no unit is found with the given name.
        
        @rtype: L{systemd.job.Job}
        """
        try:
            self.__interface.KillUnit(name, who, mode, signal)
        except dbus.exceptions.DBusException, error:
            print error
            raise SystemdError(error)

    def list_jobs(self):
        """List all jobs.
        
        @raise SystemdError, IndexError: Raised when dbus error or index error
        is raised.
        
        @rtype: A tuple of L{systemd.unit.Job}
        """
        try:
            jobs = []
            for job in self.__interface.ListJobs():
                jobs.append(Job(job[4]))
            return tuple(jobs)
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def list_units(self):
        """List all units, inactive units too.
        
        @raise SystemdError: Raised when dbus error or index error
        is raised.
        
        @rtype: A tuple of L{systemd.unit.Unit}
        """
        try:
            units = []
            for unit in self.__interface.ListUnits():
                units.append(Unit(unit[6]))
            return tuple(units)
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def load_unit(self, name):
        """Load unit by it name.
        
        @param name: Unit name (ie: network.service).
        
        @raise SystemdError: Raised when no unit is found with the given name.
        
        @rtype: L{systemd.unit.Unit}
        """
        try:
            unit_path = self.__interface.LoadUnit(name)
            unit = Unit(unit_path)
            return unit
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def power_off(self):
        try:
            self.__interface.PowerOff()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def reboot(self):
        try:
            self.__interface.Reboot()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def reexecute(self):
        try:
            self.__interface.Reexecute()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def reload(self):
        try:
            self.__interface.Reload()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def reload_or_restart_unit(self, name, mode):
        """Reload or restart unit.
        
        @param name: Unit name (ie: network.service).
        @param mode: Must be one of fail, replace or isolate.
        
        @raise SystemdError: Raised when no unit is found with the given name.
        
        @rtype: L{systemd.job.Job}
        """
        try:
            job_path = self.__interface.ReloadOrRestartUnit(name, mode)
            job = Job(job_path)
            return job
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def reload_or_try_restart_unit(self, name, mode):
        """Reload or try restart unit.
        
        @param name: Unit name (ie: network.service).
        @param mode: Must be one of fail, replace or isolate.
        
        @raise SystemdError: Raised when no unit is found with the given name.
        
        @rtype: L{systemd.job.Job}
        """
        try:
            job_path = self.__interface.ReloadOrTryRestartUnit(name, mode)
            job = Job(job_path)
            return job
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def reload_unit(self, name, mode):
        """Reload  unit.
        
        @param name: Unit name (ie: network.service).
        @param mode: Must be one of fail, replace.
        
        @raise SystemdError: Raised when no unit is found with the given name or
        mode is not corret.
        
        @rtype: L{systemd.job.Job}
        """
        try:
            job_path = self.__interface.ReloadUnit(name, mode)
            job = Job(job_path)
            return job
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def reset_failed(self):
        try:
            self.__interface.ResetFailed()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def reset_failed_unit(self, name):
        try:
            self.__interface.ResetFailedUnit(name)
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def restart_unit(self, name, mode):
        """Restart unit.
        
        @param name: Unit name (ie: network.service).
        @param mode: Must be one of fail, replace or isolate.
        
        @raise SystemdError: Raised when no unit is found with the given name.
        
        @rtype: L{systemd.job.Job}
        """
        try:
            job_path = self.__interface.RestartUnit(name, mode)
            job = Job(job_path)
            return job
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def set_environment(self, names):
        try:
            self.__interface.SetEnvironment(names)
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def start_unit(self, name, mode):
        """Start unit.
        
        @param name: Unit name (ie: network.service).
        @param mode: Must be one of fail or replace.
        
        @raise SystemdError: Raised when no unit is found with the given name.
        
        @rtype: L{systemd.job.Job}
        """
        try:
            job_path = self.__interface.StartUnit(name, mode)
            job = Job(job_path)
            return job
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def start_unit_replace(self, old_unit, new_unit, mode):
        """Start unit replace.
        
        @param old_unit: Old unit.
        @param new_unit: New unit.
        @param mode: Must be one of fail, replace, isolate, rescue or emergency.
        
        @raise SystemdError: Raised when no unit is found with the given name.
        
        @rtype: L{systemd.job.Job}
        """
        try:
            job_path = self.__interface.StartUnitReplace(old_unit, new_unit, mode)
            job = Job(job_path)
            return job
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def stop_unit(self, name, mode):
        """Stop unit.
        
        @param name: Unit name (ie: network.service).
        @param mode:  Must be one of fail or replace.
        
        @raise SystemdError: Raised when no unit is found with the given name.
        
        @rtype: L{systemd.job.Job}
        """
        try:
            job_path = self.__interface.StopUnit(name, mode)
            job = Job(job_path)
            return job
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def subscribe(self):
        try:
            self.__interface.Subscribe()
        except dbus.exceptions.DBusException, error:
            print error
            raise SystemdError(error)

    def try_restart_unit(self, name, mode):
        """Try restart unit.
        
        @param name: Unit name (ie: network.service).
        @param mode: Must be one of "fail" or "replace.
        
        @raise SystemdError: Raised when no unit is found with the given name or
        mode is invalid.
        
        @rtype: L{systemd.job.Job}
        """
        try:
            job_path = self.__interface.TryRestartUnit(name, mode)
            job = Job(job_path)
            return job
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def unset_environment(self, names):
        try:
            self.__interface.UnsetEnvironment(names)
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)

    def unsubscribe(self):
        try:
            self.__interface.Unsubscribe()
        except dbus.exceptions.DBusException, error:
            raise SystemdError(error)