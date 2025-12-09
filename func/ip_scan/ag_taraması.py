import subprocess, ipaddress, time
from func.ip_scan import get_local_ip as get_ip
from settings.set_loging import write_log
from settings import set_themes as clr

#------------------------------------------------------
#from func.ip_scan import get_mac

def ag_taraması():
    local_ip = get_ip.get_local_ip()
    net = ipaddress.ip_network(local_ip + "/24",strict=False)
    
    print(f"{clr.s}[#] Ağ taraması başlatılıyor.. {clr.r}\n")
    write_log("[#] Ağ taraması başlatılıyor.. ")
    
    aktif_ip = []
    
    for ip in net.hosts():
        ip = str(ip)
        bas_sure = time.time()
        respose = subprocess.call(
            ["ping", "-c", "1", "-W", "10", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
            )
        son_sure = round(time.time() - bas_sure,5)
        if respose ==0:
            print(f"{clr.y}[+]{clr.r} {ip} {clr.y}aktif{clr.r} -  {clr.y}Süre:{clr.r} {son_sure}")
            aktif_ip.append((ip,son_sure))
    #------------------------------------------------------
            #iface, mac = get_mac.get_mac_addr()
            #print(f"{clr.y}[+]{clr.r} {ip} {clr.y}aktif{clr.r} -  {clr.y}Süre:{clr.r} {son_sure} - Mac: {mac} - Interface: {iface}")
            #aktif_ip.append((ip,son_sure,mac,iface))
    #------------------------------------------------------
            
        else:
            print(f"{clr.k}[-]{clr.r} {ip} {clr.k}pasif{clr.r} - {clr.k}Süre:{clr.r} {son_sure}")
    #------------------------------------------------------
            #print(f"{clr.k}[-]{clr.r} {ip} {clr.k}pasif{clr.r} - {clr.k}Süre:{clr.r} {son_sure} - Mac: {mac} - Interface: {iface}")
    #------------------------------------------------------
    
    print(f"\n\t{clr.y}$$--------------Tarama Tamamlandı--------------$${clr.r}") 
    write_log("[#] $$--------------Tarama Tamamlandı--------------$$")
    
    print(f"\n{clr.am}Aktif cihazlar: {clr.r}")
    write_log("\nAktif cihazlar: ")
    for ip, son_sure in aktif_ip:
        print(f"\t{clr.y}[+] {ip} - Süre: {son_sure}")
        write_log(f"\t[+] {ip} - Süre: {son_sure}")
    #------------------------------------------------------
    #for ip, son_sure, mac, iface in aktif_ip:
        #print(f"\t{clr.y}[+] {ip} - Süre: {son_sure} - Mac: {mac} - Interface: {iface}")
        #write_log(f"\t[+] {ip} - Süre: {son_sure} - Mac: {mac} - Interface: {iface}")
    #------------------------------------------------------
    
