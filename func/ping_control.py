import clr
import subprocess
from func import helper_func as hf

def ping_kontrol(ip):
      print(f"\n{clr.s}[#] [{ip}] adresine ping atılıyor..{clr.r}\n")
      try:
              ping_yanıt = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
              if "1 received" in ping_yanıt.stdout or "bytes from" in ping_yanıt.stdout:
                      print(f"{clr.y}[+] Ping başarılı! Cihaz ağda.{clr.r}") 
                      print(ping_yanıt.stdout)
                      print(f"\n{clr.am3}------------------------------------------------------{clr.r}\n")
                      return True
              else:
                  print(f"\n{clr.k}[!] Hedef cihaz ağda değil veya erişilemez! Çıkılıyor..{clr.r}\n") 
                  print(ping_yanıt.stdout + ping_yanıt.stderr)
                  hf.cık()
      except Exception as e:
            print(f"{clr.k}[!] Ping hatası: {e}{clr.r}") 
            return False