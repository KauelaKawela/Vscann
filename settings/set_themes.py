import json
import os
from settings.set_loging import write_log

CONFIG_PATH = "config.json"
DEFAULT_THEME = "mavi"

temalar = {
    "mavi": {
        "am1": "\033[38;5;87m", "am2": "\033[38;5;81m", "am3": "\033[38;5;75m",
        "am4": "\033[38;5;69m", "am5": "\033[38;5;63m", "am6": "\033[38;5;27m", "am7": "\033[38;5;21m",
        "k": "\033[31m", "s": "\033[93m", "y": "\033[1;32m", "r": "\033[0m"
    },
    "yesil": {
        "am1": "\033[38;5;46m", "am2": "\033[38;5;40m", "am3": "\033[38;5;34m",
        "am4": "\033[38;5;28m", "am5": "\033[38;5;70m", "am6": "\033[38;5;76m", "am7": "\033[38;5;82m",
        "k": "\033[31m", "s": "\033[93m", "y": "\033[1;32m", "r": "\033[0m"
    },
    "mor": {
        "am1": "\033[38;5;141m", "am2": "\033[38;5;135m", "am3": "\033[38;5;129m",
        "am4": "\033[38;5;93m", "am5": "\033[38;5;99m", "am6": "\033[38;5;105m", "am7": "\033[38;5;111m",
        "k": "\033[31m", "s": "\033[93m", "y": "\033[1;32m", "r": "\033[0m"
    },
    "beyaz": {
        "am1": "\033[38;5;255m", "am2": "\033[38;5;252m", "am3": "\033[38;5;250m",
        "am4": "\033[38;5;247m", "am5": "\033[38;5;244m", "am6": "\033[38;5;240m", "am7": "\033[38;5;237m",
        "k": "\033[31m", "s": "\033[93m", "y": "\033[1;32m", "r": "\033[0m"
    },
    "kırmızı": {
        "am1": "\033[38;5;196m", "am2": "\033[38;5;160m", "am3": "\033[38;5;124m",
        "am4": "\033[38;5;88m", "am5": "\033[38;5;203m", "am6": "\033[38;5;210m", "am7": "\033[38;5;9m",
        "k": "\033[31m", "s": "\033[93m", "y": "\033[1;32m", "r": "\033[0m"
    },
    "sarı": {
        "am1": "\033[38;5;226m", "am2": "\033[38;5;220m", "am3": "\033[38;5;214m",
        "am4": "\033[38;5;178m", "am5": "\033[38;5;229m", "am6": "\033[38;5;230m", "am7": "\033[38;5;185m",
        "k": "\033[31m", "s": "\033[93m", "y": "\033[1;32m", "r": "\033[0m"
    },
    "turuncu": {
        "am1": "\033[38;5;208m", "am2": "\033[38;5;202m", "am3": "\033[38;5;166m",
        "am4": "\033[38;5;130m", "am5": "\033[38;5;215m", "am6": "\033[38;5;223m", "am7": "\033[38;5;172m",
        "k": "\033[31m", "s": "\033[93m", "y": "\033[1;32m", "r": "\033[0m"
    }
}

def load_config():
    """Config dosyasını oku, yoksa oluştur"""
    if not os.path.exists(CONFIG_PATH):
        save_config({"theme": DEFAULT_THEME})
    with open(CONFIG_PATH, "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}
    if "theme" not in data:
        data["theme"] = DEFAULT_THEME
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

def tema_degis(secim):
    secilen_numaralar = {
        "1": "mavi", "2": "turuncu", "3": "sarı",
        "4": "yesil", "5": "mor", "6": "kırmızı", "7": "beyaz"
    }
    secilen = secilen_numaralar.get(secim, DEFAULT_THEME)
    save_config({"theme": secilen})
    print(f"{am6}[#] {secilen.upper()} teması seçildi")
    write_log(f"[#] {secilen.upper()} teması seçildi\n")
    return temalar[secilen]

config = load_config()
tema = temalar[config["theme"]]

am  = tema["am1"]
am2 = tema["am2"]
am3 = tema["am3"]
am4 = tema["am4"]
am5 = tema["am5"]
am6 = tema["am6"]
am7 = tema["am7"]
k = tema["k"]
s = tema["s"]
y = tema["y"]
r = tema["r"]

def tema_control():
    tema_secimi = input(f"""
{am4}[1] Mavi (Varsayılan)
{am3}[2] Turuncu
{am2}[3] Sarı
{am}[4] Yeşil
{am2}[5] Mor
{am3}[6] Kırmızı
{am4}[7] Beyaz

{am5}[$] Seçiminiz: {r}""")
    return tema_degis(tema_secimi)
