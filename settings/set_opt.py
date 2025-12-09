from settings import set_raminfo as sri
from settings import set_loging as log_f
from settings import set_themes as clr
from settings import set_lang as lang
from settings.set_loging import write_log
from func import helper_func as hf
from os import system
import Vscann

def AYAR_SECİM(secim):
      ayarlarss = {
      "0":Vscann.main,
      "1":lang.dil_control,
      "2":clr.tema_control,
      "3":log_f.loginfo_ackapa,
      "4":sri.raminfo_ackapa
      }
      func = ayarlarss.get(secim)
      if func:
          func()
      else:
          print(f"{clr.k}[!] Geçerli bir değer girin{clr.r}")
          write_log("[!] Geçerli bir değer girin (Ayar menu)\n")
          hf.cık()
          
rambilgi = sri.get_ram_info()    
kaydetme = log_f.get_log_info()

kayıt = (f"{clr.y}Açık{clr.r}" if kaydetme==True else f"{clr.k}Kapalı{clr.r}")
ram_bilgisi = (f"{clr.y}Açık{clr.r}" if rambilgi==True else f"{clr.k}Kapalı{clr.r}")   

def ayarlar():
    system("cls||clear")
    Vscann.Vbanner()
    set_secim = input(f"""
{clr.am6}======================================================
{clr.am6}                ███ AYARLAR ███       
{clr.am7}======================================================

{clr.am6}[1] Dil {clr.r}[{clr.s}{lang.dil}{clr.r}]
{clr.am5}[2] Tema {clr.r}[{clr.s}{clr.config["theme"]}{clr.r}]
{clr.am4}[3] Tarama kaydı {clr.r}[{kayıt}]
{clr.am3}[4] Ram Bilgisi {clr.r}[{ram_bilgisi}]
{clr.am2}------------------------------------------------------{clr.r}
{clr.am2}[0] Geri{clr.r}

{clr.am3}[$] Seçiminiz: {clr.r}""")
    return AYAR_SECİM(set_secim)
