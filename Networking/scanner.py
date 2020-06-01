import sys
from scapy.all import Ether, ARP, srp


def main():
    # input("Enter the Target Range: ")
    _range = "192.168.1.0/254"
    _interface = "en0" # input("Enter the network interface: ")
    ip, ntBits = _range.split('/')
    ip_addresses = []
    # Since it's an IPv4
    st_bit = ip.split('.')[3:4][0]
    for n in range(1, int(ntBits)+1):
        eval_ip = ".".join(ip.split('.')[:-1]) + '.' + str(n)
        ip_addresses.append(eval_ip)
    print(ip_addresses)

    for ip in ip_addresses:
        _pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
        ans, unans = srp(_pkt, iface=_interface, timeout=0.2, verbose=False)
        for snt, recv in ans:
            if recv:
                print("Host Alive: %s - %s" % (recv[ARP].psrc, recv[Ether].src))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C pressed. Exiting. ")
        sys.exit(0)