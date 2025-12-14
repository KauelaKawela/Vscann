import sys
from settings import set_themes as clr
from settings.set_loging import write_log
        
def cık():
      print(f"{clr.s}[#] Çıkılıyor..{clr.r}")
      write_log("[#] Çıkılıyor.. \n======================================================")
      sys.exit()
      
def bas_port_kontrol(baslangıc_port):
      write_log("[#] 'bas_port_kontrol()' fonksiyonu çalıştırıldı")
      if baslangıc_port > 65535:
         print(f"{clr.k}[!] Port girdisi 65535'ten büyük olamaz!{clr.r}")
         write_log("[!] Port girdisi 65535'ten büyük olamaz!")
         cık()
         
def bit_port_kontrol(bitis_port):
      write_log("[#] 'bit_port_kontrol()' fonksiyonu çalıştırıldı")
      if bitis_port > 65535:
            print(f"{clr.k}[!] Port girdisi 65535'ten büyük olamaz!{clr.r}")
            write_log("[!] Port girdisi 65535'ten büyük olamaz!")
            cık()
                
