from settings.set_loging import write_log
write_log("[#] 'secili_port.py' dosyası çalıştırılı")

import time
from func.port_scan import ping_control as ping
from func.port_scan import port_taraması as p_tsı
from func import helper_func as hf
from settings import set_themes as clr

acık_port=p_tsı.acık_port
port_list=[]

def secili_port():
        write_log("[#] 'secili_port()' fonksiyonu çalıştırıldı")
        hedef_ip=input(f"{clr.am}[$] Hedef IP adresi: {clr.r}") 
        write_log(f"[$] Hedef IP adresi: {hedef_ip}")
        ping.ping_kontrol(hedef_ip)
        secili_port = input(f"{clr.am}[$] Taranacak portlar -virgülle ayır- (1/65535)): {clr.r}")
        try:
            if not secili_port.strip():
                raise ValueError
            temiz_portlar = [t.strip() for t in secili_port.split(",")]
            if not all(t.isdigit() for t in temiz_portlar):
                raise ValueError
            port_list = [int(t) for t in temiz_portlar]
            write_log(f"[$] Taranacak portlar -virgülle ayır- (1/65535)): {port_list}")
        except ValueError:
            print(f"{clr.k}[!] Geçersiz seçili port yanlızca sayı!{clr.r}") 
            write_log("[!] Geçersiz seçili port yanlızca sayı!")
            hf.cık()
        for ssı in port_list:
            if ssı > 65535:
                print(f"{clr.k}[!] Geçersiz port girdisi{clr.r}") 
                write_log("[!] Geçersiz port girdisi")
                hf.cık()
        try:
            t_out = float(input(f"{clr.am}[$] İstek atma aralığı (önerilen 0.5 sn): {clr.r}"))
            write_log(f"[$] İstek atma aralığı (önerilen 0.5 sn): {t_out}")
        except:
            print(f"{clr.k}[!] Geçersiz süre girdisi! yanlızca sayı!{clr.r}")
            write_log("[!] Geçersiz süre girdisi! yanlızca sayı!")
            hf.cık()
        for port in port_list:
            time.sleep(t_out) # İstek atma aralığı
            p_tsı.port_taraması(hedef_ip,port)
        print(f"\n\t{clr.y}$$--------------Tarama Tamamlandı--------------$${clr.r}") # cam göbeği
        write_log("[#] $$--------------Tarama Tamamlandı--------------$$")
        print(f"\n{clr.am}Toplam taranan:{clr.r} {len(port_list)} {clr.am}Açık port sayısı:{clr.r} {len(acık_port)}\n{clr.am}Taranan portlar: {clr.r} {port_list}\n{clr.am}Hedef IP:{clr.r} {hedef_ip}")
        write_log(f"[#] Toplam taranan: {len(port_list)} | Açık port sayısı: {len(acık_port)} | Taranan portlar: {port_list} | Hedef IP: {hedef_ip}")
        if not acık_port:
            print(f"\n{clr.am}[*] Açık portlar:{clr.r} ")
            write_log("[*] Açık portlar:")
            print(f"\t{clr.k}$$------------Açık Port Bulunamadı------------$${clr.r}") 
            write_log("\t$$------------Açık Port Bulunamadı------------$$")
            hf.cık()
        else:
            print(f"\n{clr.am}[*] Açık portlar:{clr.r} ")
            write_log("[*] Açık portlar:")
            for port, servis,son_time,banner in acık_port:
                print(f"\t\033[32m[-] Port:{clr.r} {port} - \033[32mServis:{clr.r} {servis} - \033[32mSüre:{clr.r} {son_time} - \033[32mBanner:{clr.r} {banner}")
                write_log(f"\t[-] Port: {port} - Servis: {servis} - Süre: {son_time} - Banner: {banner}")
                
        write_log("======================================================")
