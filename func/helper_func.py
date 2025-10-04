import sys,clr

def cık():
      sys.exit()
      print(f"{clr.s} [$] Çıkılıyor..{clr.r}")
      
def bas_port_kontrol(baslangıc_port):
      if baslangıc_port > 65535:
         print(f"{clr.k}[!] Port girdisi 65535'ten büyük olamaz!{clr.r}")
         cık()
         
def bit_port_kontrol(bitis_port):
           if bitis_port > 65535:
              print(f"{clr.k}[!] Port girdisi 65535'ten büyük olamaz!{clr.r}")
              cık()
                 
def temiz():
    if os.name == "nt":
         os.system("cls")
    else:
         os.system("clear")