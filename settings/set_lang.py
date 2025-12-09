import json
import os
from settings import set_themes as clr
from settings.set_loging import write_log

CONFIG_PATH = "config.json"
DEFAULT_LANG = "tr"

def load_config():
    """Config dosyasını oku, yoksa oluştur"""
    if not os.path.exists(CONFIG_PATH):
        save_config({"lang": DEFAULT_LANG})
    with open(CONFIG_PATH, "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}
    if "lang" not in data:
        data["lang"] = DEFAULT_LANG
    return data

def save_config(new_data: dict):
    """Config'teki mevcut veriyi koruyarak güncelle"""
    data = {}
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            try:
                data = json.load(f)
            except:
                data = {}
    data.update(new_data)
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f, indent=4)

def DIL_SEC(secim):
    diller = {"1": "tr", "2": "en", "3": "de", "4": "fr"}
    secilen = diller.get(secim, DEFAULT_LANG)
    save_config({"lang": secilen})
    print(f"[#] Dil seçildi: {secilen.upper()}{clr.r}")
    write_log(f"[#] Dil seçildi: {secilen.upper()}\n")
    return secilen


def dil_control():
    secim = input(f"""
{clr.am5}[1] Türkçe (Varsayılan)
{clr.am4}[2] English
{clr.am3}[3] Deutsch
{clr.am2}[4] Français

{clr.am}[$] Seçiminiz: """)
    return DIL_SEC(secim)

config = load_config()
dil = config["lang"].upper()