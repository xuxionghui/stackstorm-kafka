from st2common.runners.base_action import Action


class IpToLongAction(Action):
    def run(self, ip):
        if str == 0:
            return 0
        tmp = ip.split(".")
        return (int(tmp[0]) << 24) + (int(tmp[1]) << 16) + (int(tmp[2]) << 8) + int(tmp[3])


