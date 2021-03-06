class Configurable:
    def __init__(self, conf, tags, file, write_mode):
        self.conf = conf
        self.tags = tags
        self.file = file
        self.write_mode = write_mode
        if len(tags) == 0:
            self.configured = conf

    def set_attrs(self, attrs):
        if len(attrs) != len(self.tags):
            Exception("'attrs'-en luzeerak "+str(len(self.tags))+" izan behar du, eta ez "+str(len(attrs)))
        else:
            self.attrs = attrs
            if self.write_mode == "r":
                self.replace()
            else:
                self.configure()

    def replace(self):
        lines = open(self.file, 'r').read().split("\n")

        for i, t in enumerate(self.tags):
            written = False
            s = ""
            for l in lines:
                if t in l:
                    written = True
                    s += self.attrs[i]+"\n"
                else:
                    s += l+"\n"
            if not written:
                s += self.attrs[i]+"\n"

            self.configured = s
            lines = s.split("\n")

    def configure(self):
        s = self.conf
        for i, t in enumerate(self.tags):
            s = s.replace("%"+t+"%",self.attrs[i])

        self.configured = s

    def to_file(self):
        if self.write_mode == "a": # append
            f = open(self.file, 'a')
            f.write(self.configured)
            f.close()
        elif self.write_mode == "w" or self.write_mode == "r": # write
            f = open(self.file, 'w')
            f.write(self.configured)
            f.close()
        else:
            Exception("'write_mode'-ren balioa ez da egokia")

    def print_config(self):
        for i, t in enumerate(self.tags):
            print t+" "+self.attrs[i]
