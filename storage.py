import command
import parse


class storage(object):

    def update_storageinfo(self):

        df = command.fire("df -h")
        df.remove('on')
        attribute = ['Size', 'Used', 'Avail', 'Use%', 'Mounted on']

        self.storageinfo = {}

        for x in range(6, len(df), 6):
            if 'dev' in df[x].split("/"):
                self.storageinfo[df[x]] = {}

                for y in range(1, 6):
                    self.storageinfo[df[x]][attribute[y - 1]] = parse.next_to(
                        df, df[x], place=y)

    def __init__(self):
        self.update_storageinfo()
