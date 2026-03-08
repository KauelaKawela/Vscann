from settings.set_loging import write_log
write_log("[&] 'get_mac.py' dosyası çalıştırıldı", level="EXEC")

import os
import json

# MAC OUI veritabanını yükle
_mac_db = {}
_DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "db", "mac_oui_db.json")

def _load_mac_db():
    """MAC OUI veritabanını JSON dosyasından yükler"""
    global _mac_db
    if _mac_db:
        return _mac_db
    try:
        with open(_DB_PATH, "r", encoding="utf-8") as f:
            _mac_db = json.load(f)
        write_log(f"[#] MAC OUI DB yüklendi: {len(_mac_db)} kayıt", level="EXEC")
    except FileNotFoundError:
        write_log(f"[!] MAC OUI DB bulunamadı: {_DB_PATH}", level="ERROR")
    except Exception as e:
        write_log(f"[!] MAC OUI DB yükleme hatası: {e}", level="ERROR")
    return _mac_db

def get_mac_addr():
    """Yerel ağ arayüzlerinin MAC adreslerini döndürür"""
    write_log("[~] 'get_mac_addr()' fonksiyonu çalıştırıldı", level="FUNC")
    interfaces = os.listdir('/sys/class/net/')
    for iface in interfaces:
        try:
            with open(f'/sys/class/net/{iface}/address', 'r') as f:
                mac = f.read().strip()
                if mac != "00:00:00:00:00:00":
                    return iface, mac
        except:
            pass
    return None, None

def get_all_mac_addrs():
    """Tüm ağ arayüzlerinin MAC adreslerini döndürür
    
    Returns:
        list: [(iface, mac)] listesi
    """
    write_log("[~] 'get_all_mac_addrs()' fonksiyonu çalıştırıldı", level="FUNC")
    sonuclar = []
    try:
        interfaces = os.listdir('/sys/class/net/')
        for iface in interfaces:
            try:
                with open(f'/sys/class/net/{iface}/address', 'r') as f:
                    mac = f.read().strip()
                    if mac != "00:00:00:00:00:00":
                        sonuclar.append((iface, mac))
            except:
                pass
    except Exception as e:
        write_log(f"[!] MAC adresi okuma hatası: {e}", level="ERROR")
    return sonuclar

def mac_to_vendor(mac_adresi):
    """MAC adresinden üretici/marka bilgisini döndürür
    
    Args:
        mac_adresi: MAC adresi (herhangi bir formatta: AA:BB:CC:DD:EE:FF veya aa-bb-cc-dd-ee-ff)
    
    Returns:
        str: Üretici adı veya "Bilinmeyen Üretici"
    """
    if not mac_adresi or mac_adresi == "N/A":
        return "Bilinmeyen Üretici"
    
    db = _load_mac_db()
    
    # MAC adresini normalize et (büyük harf, : ayracı)
    mac_temiz = mac_adresi.upper().replace("-", ":").replace(".", ":")
    
    # OUI prefix'i al (ilk 3 oktet: AA:BB:CC)
    parcalar = mac_temiz.split(":")
    if len(parcalar) >= 3:
        oui = ":".join(parcalar[:3])
        
        if oui in db:
            return db[oui]
    
    return "Bilinmeyen Üretici"

def get_mac_info_str(mac_adresi):
    """MAC adresi için okunabilir bilgi stringi döndürür"""
    vendor = mac_to_vendor(mac_adresi)
    return f"{mac_adresi} ({vendor})"

# Modül yüklendiğinde ilk MAC adresini al
iface, mac = get_mac_addr()
