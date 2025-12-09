import os

def get_mac_addr():
    interfaces = os.listdir('/sys/class/net/')
    for iface in interfaces:
        try:
            with open(f'/sys/class/net/{iface}/address','r') as f:
                mac = f.read().strip()
                if mac != "00:00:00:00:00:00":
                    return iface, mac
        except:
            pass
    return None, None
interfaces = os.listdir('/sys/class/net/')

iface, mac = get_mac_addr()
print(f"Interfaces: {iface}")
print(f"Mac: {mac}")
print(interfaces)            
