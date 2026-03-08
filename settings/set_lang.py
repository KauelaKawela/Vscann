import json
import os
from settings.set_loging import write_log
write_log("[&] 'set_lang.py' dosyası çalıştırıldı", level="EXEC")
from settings import set_themes as clr
from func.translations import strings

CONFIG_PATH = "config.json"
DEFAULT_LANG = "tr"

def load_config():
    """Config dosyasını oku, yoksa oluştur"""
    from settings.set_loging import write_log
    write_log("[~] 'load_config()' fonksiyonu çalıştırıldı [set_lang.py]", level="FUNC")
    if not os.path.exists(CONFIG_PATH):
        save_config({"lang": DEFAULT_LANG})
        write_log("[#] config.json dosyası oluşturuldu", level="EXEC")
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
    from settings.set_loging import write_log
    write_log("[~] 'save_config()' fonksiyonu çalıştırıldı [set_lang.py]", level="FUNC")
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

def get_lang():
    config = load_config()
    return config.get("lang", DEFAULT_LANG)

def get_string(key):
    lang = get_lang()
    return strings.get(lang, strings[DEFAULT_LANG]).get(key, key)

def DIL_SEC(secim):
    diller = {"1": "tr", "2": "en"}
    secilen = diller.get(secim, DEFAULT_LANG)
    save_config({"lang": secilen})
    print(f"[#] {get_string('lang_selected')}: {secilen.upper()}{clr.r}")
    from settings.set_loging import write_log
    write_log(f"[#] Dil seçildi: {secilen.upper()}\n", level="EXEC")
    return secilen

def dil_control():
    from settings.set_loging import write_log
    write_log("[~] 'dil_control()' fonksiyonu çalıştırıldı", level="FUNC")
    secim = input(f"""
{clr.am5}[1] Türkçe
{clr.am4}[2] English

{clr.am}[$] {get_string('choice')}: """)
    DIL_SEC(secim)
    write_log(f"[$] [{secim}] seçeneği seçildi (Dil)", level="EXEC")
    input(f"\n{clr.s}{get_string('press_any_key')}{clr.r}")

# Initialize
config = load_config()
dil = config["lang"].upper()
