import socket,os,time,sys,subprocess
from datetime import datetime

acık_port=[]
port_list=[]
now = datetime.now()
tema = "\033[38;5;87m"
kırmızı = "\033[31m"
sarı = "\033[93m"
yesil = "\033[1;32m"
reset = "\033[0m"
color_codes = [87, 81, 75, 69, 63, 27, 21, 19]
Vbanner = """

@@@  @@@  @@@@@@  @@@@@@@  @@@@@@  @@@  @@@ @@@  @@@ 
@@!  @@@ !@@     !@@      @@!  @@@ @@!@!@@@ @@!@!@@@ 
@!@  !@!  !@@!!  !@!      @!@!@!@! @!@@!!@! @!@@!!@! 
 !: .:!      !:! :!!      !!:  !!! !!:  !!! !!:  !!! 
   ::    ::.: :   :: :: :  :   : : ::    :  ::    :  
                             @kauela_kawela
"""
def cyan_blue():
    lines = Vbanner.strip().splitlines()  # Satırlara böl
    for i, line in enumerate(lines):
        color = color_codes[i % len(color_codes)]
        print(f"\033[38;5;{color}m{line}{reset}")
     
def baslatıcı():
    if os.name == "nt":
         os.system("cls")
    else:
         os.system("clear")
    cyan_blue()
    secim = input(f"""{tema}
======================================================
           ███ TARAMA YÖNTEMİ SEÇİM MENÜSÜ ███       
======================================================

0- Geri
1- Aralık
2- Seçili
3- Standart (1-1024)
4- Tüm portlar (65535)
------------------------------------------------------
Seçmek için numarayı gir: {reset}""")
    return secim

def cık():
      exit()
def bas_port_kontrol():
      if baslangıc_port > 65535:
         print(f"{kırmızı}[!] Port girdisi 65535'ten büyük olamaz!{reset}")
         cık()
def bit_port_kontrol():
           if bitis_port > 65535:
              print(f"{kırmızı}[!] Port girdisi 65535'ten büyük olamaz!{reset}")
              cık()
           elif baslangıc_port > bitis_port:
                  print(f"{kırmızı}[!] Başlangıç portu bitiş portundan büyük olamaz!{reset}")
                  cık()
def get_ram_info():
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
            total = int(lines[0].split()[1]) // 1024
            free = int(lines[1].split()[1]) // 1024
            available = int(lines[2].split()[1]) // 1024
            used = total - available
            percent = used * 100 // total
            if percent >= 80:
                renk = '{kırmızı}'  # Kırmızı
            elif percent >= 50:
                renk = '\033[93m'  # Sarı
            else:
                renk = '\033[92m'  # Yeşil
            output = f"[RAM] Kullanılan: {used}MB / {total}MB  ({percent}%)"
            print(f"{renk}{output}{reset}")
            return output
    except Exception as e:
        print(f"{kırmızı}[RAM] Bilgi alınamadı: {e}{reset}")
        return f"[RAM] Bilgi alınamadı: {e}"
def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Bilinmeyen servis"
def banner_grabbing(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        if "HTTP" in banner:
            return f"HTTP Servisi - {banner}"
        elif "SSH" in banner:
            return f"SSH Servisi - {banner}"
        elif "FTP" in banner:
            return f"FTP Servisi - {banner}"
        else:
            return f"Bilinmeyen Servis - {banner}"
    except socket.error:
        return f"Port {port}: banner bilgisi alınamadı"
def port_taraması(ip,port):
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.settimeout(0.5)
      try:
            start_time = time.time()
            sonuc = s.connect_ex((ip,port))
            son_time = time.time() - start_time
            if sonuc == 0:
                  banner = banner_grabbing(ip,port)
                  servis = get_service_name(port)
                  print(f"{yesil}[ + ]{reset} Port {port} {yesil}açık{reset} - {yesil}Servis:{reset} {servis} - {yesil}Süre:{reset} {son_time}- {yesil}Banner:{reset} {banner}")
                  acık_port.append((port,servis,son_time,banner))
            else:
                  servis = get_service_name(port)
                  print(f"{kırmızı}[ - ] {reset}Port {port} {kırmızı}kapalı{reset} - {kırmızı}Servis:{reset} {servis} - {kırmızı}Süre:{reset} {son_time} ")
      except Exception as e:
            print(f"{kırmızı}[!] Port {port} hatası: {e}{reset}")
            cık()
      except socket.timeout:
            print(f"{kırmızı}[!] Port: {port} Zaman aşımı!{reset}")
            cık()
      except ConnectionRefusedError:
            print(f"{kırmızı}[!] Port: {port} Bağlantı reddedildi! {reset}") 
            cık()
      except socket.error as se:
            print(f"{kırmızı}[!] Port: {port} Soket oluşturulamadı: {se}{reset}") 
            cık()
      finally:
            s.close()
def ping_kontrol(ip):
      print(f"\n{sarı}[#] [{ip}] adresine ping atılıyor..{reset}\n")
      try:
              ping_yanıt = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
              if "1 received" in ping_yanıt.stdout or "bytes from" in ping_yanıt.stdout:
                      print(f"{yesil}[+] Ping başarılı! Cihaz ağda.{reset}") 
                      print(ping_yanıt.stdout)
                      print(f"\n{tema}------------------------------------------------------{reset}\n")
                      return True
              else:
                  print(f"\n{kırmızı}[!] Hedef cihaz ağda değil veya erişilemez! Çıkılıyor..{reset}\n") 
                  print(ping_yanıt.stdout + ping_yanıt.stderr)
                  cık()
      except Exception as e:
            print(f"{kırmızı}[!] Ping hatası: {e}{reset}") 
            return False
def main():
    global baslangıc_port, bitis_port,t_out
    aralık_secili = baslatıcı()
    if aralık_secili == "0":
        print(f"{sarı} [$] Çıkılıyor..{reset}")
        exit()
    elif aralık_secili == "1":
        hedef_ip=input(f"{tema}Hedef IP adresi: {reset}") 
        ping_kontrol(hedef_ip)
        try:
            baslangıc_port=int(input(f"{tema}Başlangıç portu:{reset} "))
            bas_port_kontrol()
        except:
            print(f"{kırmızı}[!] Geçersiz başlangıç port girdisi yanlızca sayı!{reset}")
            cık()
        try:
            bitis_port=int(input(f"{tema}Bitiş portu: {reset}"))
        except:
            print(f"{kırmızı}[!] Geçersiz bitiş port girdisi yanlızca sayı!{reset}")
            cık()
        bit_port_kontrol()
        try:
            t_out = float(input(f"{tema}İstek atma aralığı (önerilen 0.5 sn): {reset}"))
        except:
            print(f"{kırmızı}[!] Geçersiz süre girdisi! yanlızca sayı!{reset}")
            cık()
        for port in range(baslangıc_port,bitis_port+1):
            time.sleep(t_out) # İstek atma aralığı 
            port_taraması(hedef_ip,port)
        print(f"\n\t{yesil}$$--------------Tarama Tamamlandı--------------$${reset}") # cam göbeği
        print(f"\n{tema}Toplam taranan:{reset} {bitis_port - baslangıc_port + 1} {tema}Açık port sayısı:{reset} {len(acık_port)}\n{tema}Port Aralığı:{reset} {baslangıc_port}-{bitis_port}\n{tema}Hedef IP:{reset} {hedef_ip}")
        if not acık_port:
            print(f"\n{tema}[*] Açık portlar:{reset} ") 
            print(f"\t{kırmızı}$$------------Açık Port Bulunamadı------------$${reset}") 
            cık()
        else:
            print(f"\n{tema}[*] Açık portlar:{reset} ")
            for port, servis,son_time,banner in acık_port:
                print(f"\t\033[32m[-] Port:{reset} {port} - \033[32mServis:{reset} {servis} - \033[32mSüre:{reset} {son_time} - \033[32mBanner:{reset} {banner}") # koyu yeşil
            cık()
    elif aralık_secili == "2":
        hedef_ip=input(f"{tema}Hedef IP adresi: {reset}") 
        ping_kontrol(hedef_ip)
        secili_port = input(f"{tema}Taranacak portlar -virgülle ayır- (1/65535)): {reset}") 
        try:
            if not secili_port.strip():
                raise ValueError
            temiz_portlar = [t.strip() for t in secili_port.split(",")]
            if not all(t.isdigit() for t in temiz_portlar):
                raise ValueError
            port_list = [int(t) for t in temiz_portlar]
        except ValueError:
            print(f"{kırmızı}[!] Geçersiz seçili port yanlızca sayı!{reset}") 
            cık()
        for ssı in port_list:
            if ssı > 65535:
                print(f"{kırmızı}[!] Geçersiz port girdisi{reset}") 
                cık()
        try:
            t_out = float(input(f"{tema}İstek atma aralığı (önerilen 0.5 sn): {reset}"))
        except:
            print(f"{kırmızı}[!] Geçersiz süre girdisi! yanlızca sayı!{reset}")
            cık()
        for port in port_list:
            time.sleep(t_out) # İstek atma aralığı
            port_taraması(hedef_ip,port)
        print(f"\n\t{yesil}$$--------------Tarama Tamamlandı--------------$${reset}") # cam göbeği
        print(f"\n{tema}Toplam taranan:{reset} {len(port_list)} {tema}Açık port sayısı:{reset} {len(acık_port)}\n{tema}Taranan portlar: {reset} {port_list}\n{tema}Hedef IP:{reset} {hedef_ip}")
        if not acık_port:
            print(f"\n{tema}[*] Açık portlar:{reset} ")
            print(f"\t{kırmızı}$$------------Açık Port Bulunamadı------------$${reset}") 
            cık()
        else:
            print(f"\n{tema}[*] Açık portlar:{reset} ")
            for port, servis,son_time,banner in acık_port:
                print(f"\t\033[32m[-] Port:{reset} {port} - \033[32mServis:{reset} {servis} - \033[32mSüre:{reset} {son_time} - \033[32mBanner:{reset} {banner}")
    elif aralık_secili == "3":
          hedef_ip=input(f"{tema}Hedef IP adresi: {reset}") 
          ping_kontrol(hedef_ip)
          try:
              t_out = float(input(f"{tema}İstek atma aralığı (önerilen 0.5 sn): {reset}"))
          except:
              print(f"{kırmızı}[!] Geçersiz süre girdisi! yanlızca sayı!{reset}")
              cık()
          for port in range(1,1025):
                time.sleep(t_out) # İstek atma aralığı
                port_taraması(hedef_ip,port)
          print(f"\n\t{yesil}$$--------------Tarama Tamamlandı--------------$${reset}") 
          print(f"\n{tema}Toplam taranan:{reset} 1024 {tema}Açık port sayısı:{reset} {len(acık_port)}\n{tema}Hedef IP:{reset} {hedef_ip}")
          if not acık_port:
              print(f"\n{tema}[*] Açık portlar:{reset} ")
              print(f"\t{kırmızı}$$------------Açık Port Bulunamadı------------$${reset}") 
              cık()
          else:
              print(f"\n{tema}[*] Açık portlar:{reset} ")
              for port, servis,son_time,banner in acık_port:
                    print(f"\t\033[32m[-] Port:{reset} {port} - \033[32mServis:{reset} {servis} - \033[32mSüre:{reset} {son_time} - \033[32mBanner:{reset} {banner}")
    elif aralık_secili == "4":
          hedef_ip=input(f"{tema}Hedef IP adresi: {reset}") 
          ping_kontrol(hedef_ip)
          try:
              t_out = float(input(f"{tema}İstek atma aralığı (önerilen 0.5 sn): {reset}"))
          except:
              print(f"{kırmızı}[!] Geçersiz süre girdisi! yanlızca sayı!{reset}")
              cık()
          for port in range(1,65536):
                time.sleep(t_out) # İstek atma aralığı
                port_taraması(hedef_ip,port)
          print(f"\n\t{yesil}$$--------------Tarama Tamamlandı--------------$${reset}") 
          print(f"\n{tema}Toplam taranan:{reset} 65535 {tema}Açık port sayısı:{reset} {len(acık_port)}\n{tema}Hedef IP:{reset} {hedef_ip}")
          if not acık_port:
              print(f"\n{tema}[*] Açık portlar:{reset} ")
              print(f"\t{kırmızı}$$------------Açık Port Bulunamadı------------$${reset}") 
              cık()
          else:
              print(f"\n{tema}[*] Açık portlar:{reset} ")
              for port, servis,son_time,banner in acık_port:
                    print(f"\t\033[32m[-] Port:{reset} {port} - \033[32mServis:{reset} {servis} - \033[32mSüre:{reset} {son_time} - \033[32mBanner:{reset} {banner}")
    else:
        print(f"{kırmızı}[!] Hatalı tarama seçimi{reset}") 
        cık()

if __name__ == "__main__":
   main()
