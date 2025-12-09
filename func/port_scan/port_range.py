import time
from func.port_scan import ping_control as ping
from func import helper_func as hf
from func.port_scan import port_taraması as p_tsı
from settings import set_themes as clr
from settings.set_loging import write_log

acık_port=p_tsı.acık_port
port_list=[]

def port_range():
        hedef_ip=input(f"{clr.am}[$] Hedef IP adresi: {clr.r}") 
        write_log(f"[$] Hedef IP adresi: {hedef_ip}")
        ping.ping_kontrol(hedef_ip)
        try:
            baslangıc_port=int(input(f"{clr.am}[$] Başlangıç portu:{clr.r} "))
            write_log(f"[$] Başlangıç portu: {baslangıc_port}")
        except:
            print(f"{clr.k}[!] Geçersiz başlangıç port girdisi yanlızca sayı!{clr.r}")
            write_log("[!] Geçersiz başlangıç port girdisi yanlızca sayı!\n")
            hf.cık()
        hf.bas_port_kontrol(baslangıc_port)
        try:
            bitis_port=int(input(f"{clr.am}[$] Bitiş portu: {clr.r}"))
            write_log(f"[$] Bitiş portu: {bitis_port}")
        except:
            print(f"{clr.k}[!] Geçersiz bitiş port girdisi yanlızca sayı!{clr.r}")
            write_log("[!] Geçersiz bitiş port girdisi yanlızca sayı!")
            hf.cık()
        hf.bit_port_kontrol(bitis_port)
        try:
            t_out = float(input(f"{clr.am}[$] İstek atma aralığı (önerilen 0.5 sn): {clr.r}"))
            write_log(f"[$] İstek atma aralığı (önerilen 0.5 sn): {t_out}")
        except:
            print(f"{clr.k}[!] Geçersiz süre girdisi! yanlızca sayı!{clr.r}")
            write_log("[!] Geçersiz süre girdisi! yanlızca sayı!")
            hf.cık()
        if baslangıc_port > bitis_port:     
            for port in range(bitis_port,baslangıc_port+1):
                  time.sleep(t_out) # İstek atma aralığı 
                  p_tsı.port_taraması(hedef_ip,port)
            print(f"\n\t{clr.y}$$--------------Tarama Tamamlandı--------------$${clr.r}") 
            write_log("[#] $$--------------Tarama Tamamlandı--------------$$")
            print(f"\n{clr.am}Toplam taranan:{clr.r} {baslangıc_port-bitis_port + 1} {clr.am}Açık port sayısı:{clr.r} {len(acık_port)}\n{clr.am}Port Aralığı:{clr.r} {bitis_port}-{baslangıc_port}\n{clr.am}Hedef IP:{clr.r} {hedef_ip}")
            write_log(f"Toplam taranan: {baslangıc_port-bitis_port + 1} | Açık port sayısı: {len(acık_port)} | Port Aralığı: {bitis_port}-{baslangıc_port} | Hedef IP: {hedef_ip}")
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
                hf.cık()
        else:
            for port in range(baslangıc_port,bitis_port+1):
                   time.sleep(t_out) # İstek atma aralığı 
                   p_tsı.port_taraması(hedef_ip,port)
            print(f"\n\t{clr.y}$$--------------Tarama Tamamlandı--------------$${clr.r}") # cam göbeği
            write_log("[#] $$--------------Tarama Tamamlandı--------------$$")
            print(f"\n{clr.am}Toplam taranan:{clr.r} {bitis_port - baslangıc_port + 1} {clr.am}Açık port sayısı:{clr.r} {len(acık_port)}\n{clr.am}Port Aralığı:{clr.r} {baslangıc_port}-{bitis_port}\n{clr.am}Hedef IP:{clr.r} {hedef_ip}")
            write_log(f"Toplam taranan: {baslangıc_port-bitis_port + 1} | Açık port sayısı: {len(acık_port)} | Port Aralığı: {bitis_port}-{baslangıc_port} | Hedef IP: {hedef_ip}")
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
                    print(f"\t\033[32m[-] Port:{clr.r} {port} - \033[32mServis:{clr.r} {servis} - \033[32mSüre:{clr.r} {son_time} - \033[32mBanner:{clr.r} {banner}") # koyu yeşil
                    write_log(f"\t[-] Port: {port} - Servis: {servis} - Süre: {son_time} - Banner: {banner}")
                hf.cık()
        write_log("\n")