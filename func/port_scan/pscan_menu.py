import Vscann
from os import system
from func.port_scan import port_range as p_r
from func.port_scan import ping_control as ping
from func.port_scan import secili_port as secp
from func.port_scan import standart,all_ports
from settings.set_loging import write_log
from settings import set_themes as clr
from func import helper_func as hf

def PSCAN_menu(secilmis):
      secim_menusu = {
      "0":Vscann.main,
      "1":p_r.port_range,
      "2":secp.secili_port,
      "3":standart.standart,
      "4":all_ports.tum_portlar,
      }
      func = secim_menusu.get(secilmis)
      if func:
          func()
      else:
           print(f"{clr.k}[!] Geçerli bir değer girin{clr.r}")
           write_log("[!] Geçerli bir değer girin")
           hf.cık()

def tarama_menusu():
       system("cls||clear")
       Vscann.Vbanner()
       secim = input(f"""
{clr.am6}======================================================
{clr.am6}           ███ TARAMA YÖNTEMİ SEÇİM MENÜSÜ ███       
{clr.am7}======================================================

{clr.am6}[1] Port aralığı
{clr.am5}[2] Seçili portlar
{clr.am4}[3] Standart tarama (1-1024)
{clr.am3}[4] Tüm portlar (65535)
{clr.am}------------------------------------------------------
{clr.am2}[0] Geri

{clr.am3}[$] Seçiminiz: {clr.r}""")
       PSCAN_menu(secim)
