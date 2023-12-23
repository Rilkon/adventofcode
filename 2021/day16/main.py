import copy
import os
from functools import reduce
from operator import mul
from time import perf_counter as pc


def hex_to_bin(h):
    return bin(int(h, 16))[2:].zfill(len(h) * 4)


class Packet:

    def __init__(self, version, packet_type):
        self.version = version
        self.packet_type = packet_type

    def get_version(self) -> int:
        return self.version

    def get_value(self) -> int:
        pass

    def __repr__(self):
        mystring = ' , '.join("%s: %s" % item for item in vars(self).items())
        return str(self.__class__.__name__) + " [" + mystring + " ]"


class OperatorPacket(Packet):

    def __init__(self, version, packet_type, tid, len_tid, subpackets):
        super().__init__(version, packet_type)
        self.tid = tid
        self.len_tid = len_tid
        self.subpackets = subpackets

    def get_version(self) -> int:
        return sum(p.get_version() for p in self.subpackets) + self.version

    def get_value(self) -> int:
        if self.packet_type == 0:
            return sum(subpacket.get_value() for subpacket in self.subpackets)
        elif self.packet_type == 1:
            return reduce(mul, [p.get_value() for p in self.subpackets], 1)
        elif self.packet_type == 2:
            return min(p.get_value() for p in self.subpackets)
        elif self.packet_type == 3:
            return max(p.get_value() for p in self.subpackets)
        elif self.packet_type == 5:
            return int(self.subpackets[0].get_value() > self.subpackets[1].get_value())
        elif self.packet_type == 6:
            return int(self.subpackets[0].get_value() < self.subpackets[1].get_value())
        elif self.packet_type == 7:
            return int(self.subpackets[0].get_value() == self.subpackets[1].get_value())
        else:
            raise ValueError(f"{self.packet_type=}")


class LiteralPacket(Packet):

    def __init__(self, version, packet_type, value):
        super().__init__(version, packet_type)
        self.value = value

    def get_value(self) -> int:
        return self.value


def parse_binstring(binstring) -> (Packet, ""):
    version = int(binstring[0:3], 2)
    packet_type = int(binstring[3:6], 2)

    # literal packet
    if packet_type == 4:
        tempbin = ""
        for i in range(6, len(binstring), 5):
            # slice in 5 pairs beginning at 6 (here value begins for literal packets)
            tempbin = tempbin + binstring[i + 1: i + 5]
            # stop for the trash bits at the end of the 5bit blocks starting with 1
            if binstring[i] == "0":
                break
        # convert our concatenated binstring to decimal to store vlaue
        value = int(tempbin, 2)
        # slice the binstring to start where we stopped
        return LiteralPacket(version, packet_type, value), binstring[i + 5:]

    # operator packet
    tid = binstring[6]
    subpackets = []
    if tid == "0":
        # If the length type ID is 0, then the next 15 bits are a number that represents the
        # total length in bits of the sub-packets contained by this packet.
        len_tid = int(binstring[7:22], 2)
        sub_bits = binstring[22: 22 + len_tid]
        # as long as we have bits, parse substring for packages (recursively)
        while len(sub_bits) > 0:
            subpacket, sub_bits = parse_binstring(sub_bits)
            subpackets.append(subpacket)
        # Update remaining binstring
        binstring = binstring[22 + len_tid:]
    else:
        # If the length type ID is 1, then the next 11 bits are a number that represents the
        # number of sub-packets immediately contained by this packet.
        len_tid = int(binstring[7:18], 2)
        binstring = binstring[18:]
        for i in range(0, len_tid):
            subpacket, sub_bits = parse_binstring(binstring)
            subpackets.append(subpacket)
            # update the remaining binstring for the loop unitl len_tid is reached
            binstring = sub_bits

    return (OperatorPacket(version, packet_type, tid, len_tid, subpackets), binstring,)


def main():
    time1 = pc()
    filename = "day16.txt"
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        data = f.read()

    binstring = hex_to_bin(data)
    print("Part1: ", parse_binstring(binstring)[0].get_version())

    print("Part2: ", parse_binstring(binstring)[0].get_value())
    print("Execution Time: ", (pc() - time1) * 1000, "ms")


if __name__ == "__main__":
    main()
