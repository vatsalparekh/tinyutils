import command
import parse


class network(object):

    def update_available_interfaces(self):

        ip = command.fire("ip a")

        self.available_interfaces = []

        for x in range(15):
            interface_tmp_num = str(x) + ':'

            if interface_tmp_num in ip:
                self.available_interfaces.append(
                    parse.next_to(ip, interface_tmp_num))

    def update_interface_details(self):

        ip = command.fire("ip a")
        ifconfig = command.fire("ifconfig")

        ifconfig_interfaces = []
        count = 0
        for x in ifconfig:
            if x == 'Link':
                ifconfig_interfaces.append(ifconfig[count - 1])
            count += 1

        self.interface_details = {}

        for interfaces in self.available_interfaces:

            self.interface_details[interfaces] = {}

            self.interface_details[interfaces]['state'] = parse.next_to(
                ip, 'state', search_base=interfaces,
                search_end=parse.next_to(self.available_interfaces,
                                         interfaces))

            self.interface_details[interfaces]['inet'] = parse.next_to(
                ip, 'inet', search_base=interfaces,
                search_end=parse.next_to(self.available_interfaces,
                                         interfaces))

            self.interface_details[interfaces]['inet6'] = parse.next_to(
                ip, 'inet6', search_base=interfaces,
                search_end=parse.next_to(self.available_interfaces,
                                         interfaces))

        for interfaces in ifconfig_interfaces:
            self.interface_details[interfaces + ":"]['HWaddr'] = parse.next_to(
                ifconfig, 'HWaddr',
                search_base=interfaces,
                search_end=parse.next_to(ifconfig_interfaces, interfaces))

    def __init__(self):
        self.update_available_interfaces()
        self.update_interface_details()
