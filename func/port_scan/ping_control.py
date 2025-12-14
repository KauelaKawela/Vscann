from settings.set_loging import write_log
write_log("[#] 'ping_control.py' dosyası çalıştırıldı")

import subprocess
from settings import set_themes as clr
from func import helper_func as hf

def ping_kontrol(ip):
      write_log("[#] 'ping_kontrol()' fonksiyonu çalıştırıldı")
      print(f"\n{clr.s}[#] [{ip}] adresine ping atılıyor..{clr.r}\n")
      write_log(f"[#] [{ip}] adresine ping atılıyor..\n")
      try:
              ping_yanıt = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
              if "1 received" in ping_yanıt.stdout or "bytes from" in ping_yanıt.stdout or "bytes" in ping_yanıt.stdout:
                      print(f"{clr.y}[+] Ping başarılı! Cihaz ağda{clr.r}") 
                      write_log("[+] Ping başarılı! Cihaz ağda")
                      print(ping_yanıt.stdout)
                      write_log(ping_yanıt.stdout+"\n")
                      write_log("------------------------------------------------------\n")
                      print(f"\n{clr.am3}------------------------------------------------------{clr.r}\n")
                      return True
              else:
                  print(f"\n{clr.k}[!] Hedef cihaz ağda değil veya erişilemez! Çıkılıyor..{clr.r}\n") 
                  write_log("[!] Hedef cihaz ağda değil veya erişilemez! Çıkılıyor..\n")
                  print(ping_yanıt.stdout + ping_yanıt.stderr)
                  write_log(ping_yanıt.stdout + ping_yanıt.stderr)
                  hf.cık()
      except Exception as e:
            print(f"{clr.k}[!] Ping hatası: {e}{clr.r}")
            write_log(f"[!] Ping hatası: {e}")
            hf.cık()
