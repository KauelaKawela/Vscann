from settings.set_loging import write_log
write_log("[#] 'ag_taraması.py' dosyası çalıştırılı")

import subprocess, ipaddress, time
from func.ip_scan import get_local_ip as get_ip
from settings import set_themes as clr

#------------------------------------------------------
#from func.ip_scan import get_mac

def ag_taraması():
    write_log("[#] 'ag_taraması()' fonksiyonu çalıştırıldı")
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
        if respose ==0:
            aktif_ip.append(ip)
    #IP taraması bittikten sonra teker teker mac ve interface leri alınıp listeye eklenecek - [] yerine {{},{},{}} gibi saklanacak       
    print(f"\n\t{clr.y}$$--------------Tarama Tamamlandı--------------$${clr.r}") 
    write_log("[#] $$--------------Tarama Tamamlandı--------------$$")
    
    print(f"\n{clr.am}Aktif cihazlar: {clr.r}")
    write_log("\nAktif cihazlar: ")
    for ip, son_sure in aktif_ip:
        print(f"\t{clr.y}[+] {ip} - Süre: {son_sure}")
        write_log(f"\t[+] {ip}")
    hf.cık()
    
    #------------------------------------------------------
    #for ip, son_sure, mac, iface in aktif_ip:
        #print(f"\t{clr.y}[+] {ip} - Mac: {mac} - Interface: {iface}")
        #write_log(f"\t[+] {ip} - Mac: {mac} - Interface: {iface}")
    #------------------------------------------------------
    
