import json,os
from datetime import datetime
from os import system 
from settings import set_themes as clr

CONFIG_PATH = "config.json"
DEFAULT_LOGINFO = False
LOG_FILE = "scann_log.txt"

def load_config():
    """Config dosyasını yükle, yoksa varsayılanla oluştur."""
    if not os.path.exists(CONFIG_PATH):
        save_config({"set_log_info": DEFAULT_LOGINFO})
    with open(CONFIG_PATH, "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}
    if "set_log_info" not in data:
        data["set_log_info"] = DEFAULT_LOGINFO
    return data
    
def save_config(new_data: dict):
    """Config içeriğini koruyarak sadece verilen verileri günceller."""
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
        
def get_log_info():
    """Log bilgisinin mevcut durumunu döndürür."""
    config = load_config()
    return bool(config.get("set_log_info", DEFAULT_LOGINFO))

def set_log_info(value: bool):
    """Log bilgisini True/False olarak kaydeder."""
    save_config({"set_log_info": value})
    
def reset_log_info():
    save_config({"set_log_info": DEFAULT_LOGINFO})
    print(f"{clr.s}[!] Kaydetme varsayılana [{clr.k}Kapalı{clr.r}] ayarlandı{clr.r}")

def loginfo_ackapa():
    current = get_log_info()
    durum = f"{clr.s}Kapat{clr.r}" if current else f"{clr.s}Aç{clr.r}" 
    secim = input(f"""{clr.am5}[$] Kaydetmeyi {clr.r}[{durum}]{clr.am5} (e/h):{clr.r} """).lower().strip()
    
    if secim == "e":
        yeni_durum = not current
        set_log_info(yeni_durum)
        yeni_yazi = f"{clr.y}Açık{clr.r}" if yeni_durum else f"{clr.k}Kapalı{clr.r}"
        print(f"{clr.am5}[#] Kaydetme {yeni_yazi}{clr.r}")
        input(f"\n{clr.s}Bir tuşa basın..{clr.r}")
        system("python Vscann.py||python3 Vscann.py")
    elif secim == "h":
        print(f"{clr.am3}[!] Değişiklik yapılmadı{clr.r}")
    else:
        print(f"{clr.k}[!] Geçersiz seçim{clr.r}")
        
def write_log(message: str):
    """Basit log sistemi"""
    
    if not get_log_info():
        return  # Log kapalıysa hiç yazma
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{time_now}] - {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)
