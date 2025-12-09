from settings.set_loging import write_log
from settings import set_themes as clr
from os import system
import Vscann
from func import helper_func as hf
from func.ip_scan import ag_taraması as ag_tara

def ipscan_menu(secilmis):
      secim_menusu = {
      "0":Vscann.main,
      "1":ag_tara.ag_taraması
      }
      func = secim_menusu.get(secilmis)
      if func:
          func()
      else:
           print(f"{clr.k}[!] Geçerli bir değer girin{clr.r}")
           write_log("[!] Geçerli bir değer girin (Ağ tarama menusu)")
           hf.cık()

def ip_taraması():
     system("cls||clear")
     Vscann.Vbanner()
     secim = input(f"""
{clr.am6}======================================================
{clr.am6}             ███ AĞ TARAMA MENUSU ███       
{clr.am7}======================================================

{clr.am6}[1] Başlat
{clr.am5}------------------------------------------------------
{clr.am4}[0] Geri

{clr.am3}[$] Seçiminiz: {clr.r}""")
     ipscan_menu(secim)
