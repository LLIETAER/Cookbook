from scapy.all import *
import time
Wifi = "en0"

p = Ether(dst="ff:ff:ff:ff:ff:ff",src="b8:81:98: E0:46:6a")/ARP(pdst="192.168.1.0/24")

ans, unans = srp(p,iface=Wifi,timeout=2)
print("A total scan To%d hosts"%len(ans))

result=[]

for s, r in ans:
    Result.append([r[ARP].psrc,r[ARP].hwsrc])

for ip, mac in result:
    print(ip, " --->", mac)