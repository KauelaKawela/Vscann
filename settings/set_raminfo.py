from settings import set_themes as clr
import json,os
from settings.set_loging import write_log

CONFIG_PATH = "config.json"
DEFAULT_RAM_INFO = False  

def load_config():
    if not os.path.exists(CONFIG_PATH):
        save_config({"set_ram_info": DEFAULT_RAM_INFO})
    with open(CONFIG_PATH, "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}
    if "set_ram_info" not in data:
        data["set_ram_info"] = DEFAULT_RAM_INFO
    return data

def save_config(new_data: dict):
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

def get_ram_info():
    config = load_config()
    return config.get("set_ram_info", DEFAULT_RAM_INFO)

def set_ram_info(value: bool):
    save_config({"set_ram_info": value})

def reset_ram_info():
    save_config({"set_ram_info": DEFAULT_RAM_INFO})
    print(f"{clr.s}[#] RAM bilgisi varsayılana (Kapalı) döndürüldü{clr.r}")
    write_log("[#] RAM bilgisi varsayılana (Kapalı) döndürüldü\n")

def raminfo_ackapa():
    current = get_ram_info()
    durum = f"{clr.s}Kapat{clr.r}" if current else f"{clr.s}Aç{clr.r}" 
    secim = input(f"""{clr.am5}[$] RAM bilgisini {clr.r}[{durum}]{clr.am5} (e/h):{clr.r} """).lower().strip()
    if secim == "e":
        yeni_durum = not current
        set_ram_info(yeni_durum)
        yeni_yazi = f"{clr.y}Açık{clr.r}" if yeni_durum else f"{clr.k}Kapalı{clr.r}"
        print(f"{clr.am5}[#] RAM bilgisi artık {yeni_yazi}{clr.r}")
        write_log(f"[#] RAM bilgisi artık {yeni_yazi}\n")
    elif secim == "h":
        print(f"{clr.am3}[!] Değişiklik yapılmadı{clr.r}")
        write_log("[!] Değişiklik yapılmadı (Ram info)\n")
    else:
        print(f"{clr.k}[!] Geçersiz seçim{clr.r}")
        write_log("[!] Geçersiz seçim(Ram info)\n")