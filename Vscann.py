from os import system
import sys,subprocess,help,os
from datetime import datetime
from func import helper_func as hf
from settings import set_themes as clr
from settings import set_lang as lang
from settings import set_opt 
from settings.set_loging import write_log
from func.port_scan import pscan_menu as pmenu
from func.ip_scan import ipscan_menu as ipscan

acık_port=[]
port_list=[]
    
def Vbanner():
     print(fr"""

{clr.am}@@@  @@@  @@@@@@  @@@@@@@  @@@@@@  @@@  @@@ @@@  @@@
{clr.am2}@@!  @@@ !@@     !@@      @@!  @@@ @@!@!@@@ @@!@!@@@
{clr.am3}@!@  !@!  !@@!!  !@!      @!@!@!@! @!@@!!@! @!@@!!@!
{clr.am4} !: .:!      !:! :!!      !!:  !!! !!:  !!! !!:  !!!
{clr.am5}   ::    ::.: :   :: :: :  :   : : ::    :  ::    :
{clr.am6}            Github: https://github.com/KauelaKawela
""")

def MENU(secilmis):
      secim_menusu = {
      "0":hf.cık,
      "1":pmenu.tarama_menusu,
      "2":ipscan.ip_taraması,
      "3":set_opt.ayarlar,
      "4":help.yardım
      }
      func = secim_menusu.get(secilmis)
      if func:
          func()
      else:
           print(f"{clr.k}[!] Geçerli bir değer girin{clr.r}")
           write_log("[!] Geçerli bir değer girin")
                  
def main():
    system("cls||clear")
    Vbanner()
    try:
         secim = input(f"""
{clr.am6}======================================================
{clr.am6}                  ███ ANA MENU ███       
{clr.am7}======================================================

{clr.am6}[1] Port taraması
{clr.am5}[2] Ağ taraması
{clr.am4}[3] Ayarlar
{clr.am3}[4] Yardım
{clr.am2}------------------------------------------------------
{clr.am2}[0] Çıkış

{clr.am3}[$] Seçiminiz: {clr.r}""")
         MENU(secim)
    except KeyboardInterrupt as e:
         print(f"{clr.k}[!] İşlem sonlandırıldı{clr.r}")
         write_log("[!] İşlem sonlandırıldı\n")
    except AttributeError as e:
         print(f"{clr.k}[!] Hata: {e}{clr.r}")
         write_log(f"[!] Hata: {e}\n")
    except TypeError as e:
         print(f"{clr.k}[!] Hatalı girdi türü! Geçerli bir değer girin {clr.r}")
         write_log("[!] Hatalı girdi türü! Geçerli bir değer girin\n")
    except Exception as e:
         print(f"{clr.k}[!] Hata: {e}{clr.r}")
         write_log(f"[!] Hata: {e}\n")
         
if __name__ == "__main__":
   main()
