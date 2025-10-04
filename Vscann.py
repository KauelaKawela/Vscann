import socket,os,time,sys,subprocess
from datetime import datetime
from func import helper_func as hf
import clr
from func import port_range as p_r
from func import ping_control as ping
from func import secili_port as secp
from func import standart,all_ports

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
      "1":p_r.port_range,
      "2":secp.secili_port,
      "3":standart.standart,
      "4":all_ports.tum_portlar,
      "5":yardım
      }
      func = secim_menusu.get(secilmis)
      if func:
          func()
      else:
           print(f"{clr.k}[!] Geçerli bir değer girin{clr.r}")

def yardım():
     print(f"""
{clr.am3}[-] 0- Çalışmayı sonlandırır
{clr.am4}[-] 1- [Başlangıç] - [Bitiş] port aralığını tarar
{clr.am5}[-] 2- [443,8080,21,80...] Seçili portları tarar
{clr.am6}[-] 3- [1-1024] Standart portları tarar 
{clr.am7}[-] 4- [1-65535] Tüm portları tarar
{clr.am6}[-] 5- Bilgilendirme
     """)
     
def main():
    Vbanner()
    try:
         secim = input(f"""
{clr.am6}======================================================
{clr.am6}           ███ TARAMA YÖNTEMİ SEÇİM MENÜSÜ ███       
{clr.am6}======================================================

{clr.am6}[1] Aralık
{clr.am5}[2] Seçili
{clr.am4}[3] Standart (1-1024)
{clr.am3}[4] Tüm portlar (65535)
{clr.am2}[5] Yardım
{clr.am}------------------------------------------------------
{clr.am2}[0] Geri

{clr.am3}[$] Seçiminiz: {clr.r}""")
         MENU(secim)
    except KeyboardInterrupt as e:
         print(f"{clr.k}[!] İşlem sonlandırıldı{clr.r}")
    except AttributeError as e:
         print(f"{clr.k}[!] Hatalı girdi türü! Geçerli bir değer girin{clr.r}")
    except TypeError as e:
         print(f"{clr.k}[!] Hatalı girdi türü! Geçerli bir değer girin{clr.r}")
    except Exception as e:
         print(f"{clr.k}[!] Hata: {e}{clr.r}")
         
if __name__ == "__main__":
   main()