import unittest

import signal
import dbus

from systemd.manager import Manager
from systemd.exceptions import SystemdError
from systemd.unit import Unit
from systemd.job import Job

class ManagerTest(unittest.TestCase):

    # Stolen from Django framework
    def assertRaisesErrorWithMessage(self, error, message, callable, *args, **kwargs):
        self.assertRaises(error, callable, *args, **kwargs)
        try:
            callable(*args, **kwargs)
        except error, e:
            self.assertEqual(message, str(e))

    def setUp(self):
        self.manager = Manager()
    
    #def test_get_unit(self):
    #    self.assertIsInstance(self.manager.get_unit('network.service'), Unit)
        #Put this variables to a file named tests_settings.py
    #    NO_EXIST_SERVICE = 'noexisssssst.service'
    #    self.assertRaisesErrorWithMessage(
    #        SystemdError,
    #        'NoSuchUnit(Unit %s is not loaded.)' % NO_EXIST_SERVICE,
    #        self.manager.get_unit, NO_EXIST_SERVICE)
    
    #def test_get_unit_by_pid(self):
    #    #Put this variables to a file named tests_settings.py
    #    EXIST_PID = 0
    #    NO_EXIST_PID = 0
    #    self.assertIsInstance(self.manager.get_unit_by_pid(EXIST_PID), Unit)
    #    self.assertRaisesErrorWithMessage(
    #        SystemdError,
    #        'NoSuchUnit(No unit for PID %s is loaded.' % NO_PID,
    #        self.manager.get_unit_by_pid, NO_PID)

    # This will HALT your computer
    #def test_halt(self):
    #    self.manager.halt()

    #def test_k_exec(self):
    #    self.manager.k_exec()


    #def test_kill_unit(self):
    #    self.manager.kill_unit('sshd.service', 'main', 'control-group', 9)
    #    self.manager.kill_unit('sshd.service', 'control', 'control-group', 9)
    #    self.manager.kill_unit('sshd.service', 'all', 'control-group', 9)
    #    self.manager.kill_unit('sshd.service', 'all', 'process-group', 9)
    #    self.manager.kill_unit('sshd.service', 'all', 'process', 9)
    #def test_list_jobs(self):
    #    self.assertIsInstance(self.manager.list_jobs(), tuple)

    #def test_list_units(self):
    #    self.assertIsInstance(self.manager.list_units(), tuple)

   #def test_load_unit(self):
   #     self.assertIsInstance(self.manager.load_unit('sshd.service'), Unit)

    # This will POWEROFF your computer
    #def test_power_off(self):
    #    self.manager.power_off()

    # This will REBOOT your computer
    #def test_reboot(self):
    #    self.manager.reboot()

    #def test_reexecute(self):
    #    self.manager.reexecute()

    #def test_reload(self):
    #    self.manager.reload()
    """

    def test_reload_or_restart_unit(self):
        self.assertIsInstance(
            self.manager.reload_or_restart_unit('sshd.service', 'fail'),
            Job)
        self.assertIsInstance(
            self.manager.reload_or_restart_unit('sshd.service', 'replace'),
            Job)
    
    def test_reload_or_try_restart_unit(self):
        self.assertIsInstance(
            self.manager.reload_or_try_restart_unit('sshd.service', 'fail'),
            Job)
        self.assertIsInstance(
            self.manager.reload_or_try_restart_unit('sshd.service', 'replace'),
            Job)
        self.assertIsInstance(
            self.manager.reload_or_try_restart_unit('sshd.service', 'isolate'),
            Job)
    """
    
    #TODO: START TESTING FROM HERE TODO
    #def test_reload_unit(self):
    #    self.assertIsInstance(
    #        self.manager.reload_unit('sshd.service', 'fail'), Job)
    #    self.assertIsInstance(
    #        self.manager.reload_unit('sshd.service', 'replace'),e Job)

    # def test_reset_failed(self):
    #     self.manager.reset_failed()

    #def test_reset_failed_unit(self):
    #    self.manager.reset_failed_unit()

    #def test_restart_unit(self):
    #    self.assertIsInstance(
    #        self.manager.restart_unit('sshd.service', 'fail'), Job)
    #    self.assertIsInstance(
    #        self.manager.restart_unit('sshd.service', 'replace'), Job)

    #TODO:Calling this with TELEPHONE crash systemd or dbus
    #def test_set_environment(self):
    #    self.manager.set_environment('TELEPHONE')

    #def test_start_unit(self):
    #    self.assertIsInstance(
    #        self.manager.start_unit('sshd.service', 'fail'), Job)
    #    self.assertIsInstance(
    #        self.manager.start_unit('sshd.service', 'replace'), Job)
         #the below mode note acepted
    #    self.assertIsInstance(
    #        self.manager.start_unit('sshd.service', 'isolate'), Job)
    #    self.assertIsInstance(
    #        self.manager.start_unit('sshd.service', 'rescue'), Job)
    #    self.assertIsInstance(
    #        self.manager.start_unit('sshd.service', 'emergency'), Job)

    #def test_start_unit_replace(self):
    #    self.manager.start_unit_replace(old_unit, new_unit, mode)

    #def test_stop_unit(self):
    #    self.assertIsInstance(
    #        self.manager.stop_unit('sshd.service', 'fail'), Job)
    #    self.assertIsInstance(
    #        self.manager.stop_unit('sshd.service', 'replace'), Job)

    #def test_subscribe(self):
    #    self.manager.subscribe()

    #def test_try_restart_unit(self):
    #    self.assertIsInstance(
    #        self.manager.restart_unit('sshd.service', 'fail'), Job)
    #    self.assertIsInstance(
    #        self.manager.restart_unit('sshd.service', 'replace'), Job)

    #def test_try_restart_unit(self):
    #    self.manager.try_restart_unit('network.service', 'fail')
    #    self.manager.try_restart_unit('network.service', 'replace')
    #    self.assertRaisesErrorWithMessage(
    #        SystemdError,
    #        "LoadFailed(Unit noexist.service failed to load: No such file or directory. See system logs and 'systemctl status' for details.)",
    #        self.manager.try_restart_unit, 'noexist.service', 'fail')

    #TODO:Calling this with TELEPHONE crash systemd or dbus
    #def test_unset_environment(self):
    #    self.manager.unset_environment('TELEPHONE')

    #def test_unsubscribe(self):
    #    self.assertRaisesErrorWithMessage(
    #        SystemdError,
    #        'NotSubscribed(Client is not subscribed.)',
    #        self.manager.unsubscribe)