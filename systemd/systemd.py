import dbus
from dbus.mainloop.glib import DBusGMainLoop

loop = DBusGMainLoop()

bus = dbus.SystemBus()#mainloop=loop)

proxy = bus.get_object(
        'org.freedesktop.systemd1',
        '/org/freedesktop/systemd1'
    )

interface = dbus.Interface(proxy, 'org.freedesktop.systemd1.Manager')

def on_unit_new():
    pass

def on_properties_changed():
    pass


#interface.connect_to_signal('unit_new', on_unit_new)

#try:
    #manager.getContents()
#print interface.GetUnit('network.service')
#    print a
    #net_proxy = system_bus.get_object(
    #net = dbus.Interface()
    #manager.subscribe()
#except dbus.exceptions.DBusException, e:
    #print e

#print interface.Version

for unit in interface.ListUnits():
    #print unit[6]
    #print type(unit[9])

    properties_proxy = bus.get_object(
        'org.freedesktop.systemd1',
        unit[6],
    )

    properties_interface = dbus.Interface(properties_proxy, 'org.freedesktop.DBus.Properties')

    #properties_interface.connect_to_signal('properties_changed', on_propreties_changed)

    unit_proxy = bus.get_object(
        'org.freedesktop.systemd1',
        unit[6],
    )

    # Imterface to Start/Stop/Reload a service
    unit_interface = dbus.Interface(unit_proxy, 'org.freedesktop.systemd1.Unit')

    if unit[6] == '/org/freedesktop/systemd1/unit/network_2eservice':
        print 'Stoping network'
        unit_interface.Start('replace')

    #for u in unit:
    #    print u
    #print '-'*80

#while 1:
#    pass
