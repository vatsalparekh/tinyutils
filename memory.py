import command
import parse


class memory(object):

    def update_meminfo(self):

        self.meminfo = {}

        attributes = ['total', 'used', 'free', 'shared', 'buffers', 'cached']
        free = command.fire("free -m")
        count = 1

        for attrib in attributes:
            self.meminfo[attrib] = parse.next_to(
                free, 'Mem:', place=count)
            count += 1

        self.meminfo['swap'] = {}

        for x in range(3):
            self.meminfo['swap'][attributes[x]] = parse.next_to(
                free, 'Swap:', place=x + 1)

    def __init__(self):
        self.update_meminfo()
