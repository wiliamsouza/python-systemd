class SystemdError(Exception):
    def __init__(self, error):
        self.name = error.get_dbus_name().split('.')[3]
        self.message = error.get_dbus_message()

    def __str__(self):
        return '%s(%s)' % (self.name, self.message)

    def __repr__(self):
        return '%s(%s)' % (self.name, self.message)