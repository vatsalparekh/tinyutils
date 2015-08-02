import command
import parse


class cpu(object):

    def update_cpuinfo(self):

        lscpu = []

        for elemnets in command.fire("lscpu", only_element=False):
            for items in elemnets.split(":"):
                lscpu.append(items.strip())

        self.cpuinfo = {}

        attributes = ['Model name', 'Architecture',
                      'Socket(s)', 'Core(s) per socket', 'Thread(s) per core',
                      'CPU(s)', 'Virtualization', 'L1d cache', 'L1i cache',
                      'L2 cache', 'L3 cache', 'Byte Order']

        for attrib in attributes:
            self.cpuinfo[attrib] = parse.next_to(lscpu, attrib)

    def __init__(self):
        self.update_cpuinfo()
