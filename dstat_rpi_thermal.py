### Author: Justin Azoff <justin@bouncybouncy.net>

class dstat_plugin(dstat):
    TEMP_FILE = "/sys/devices/virtual/thermal/thermal_zone0/temp"
    def __init__(self):
        self.name = 'Temp'
        self.type = 'f'
        self.width = 5
        self.scale = 5
        self.vars = self.nick = ['temp']
        if not os.path.exists(self.TEMP_FILE):
            raise Exception, 'Needs newer Raspberry Pi firmware'

    def extract(self):
        with open(self.TEMP_FILE) as f:
            temp = int(f.read())/1000.0
        self.val['temp'] = temp

# vim:ts=4:sw=4:et
