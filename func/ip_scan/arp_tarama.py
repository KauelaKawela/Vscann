from settings.set_loging import write_log
write_log("[&] 'arp_tarama.py' dosyası çalıştırıldı", level="EXEC")

import os
import subprocess
import re
from settings import set_themes as clr
from settings.set_lang import get_string

def root_mu():
    """Root yetkisi olup olmadığını kontrol eder"""
    write_log("[~] 'root_mu()' fonksiyonu çalıştırıldı", level="FUNC")
    try:
        sonuc = os.geteuid() == 0
        write_log(f"[#] Root kontrolü: {sonuc}", level="EXEC")
        return sonuc
    except AttributeError:
        # Windows'ta geteuid yok
        write_log("[!] Root kontrolü yapılamadı (Windows?)", level="ERROR")
        return False

def arp_tara(ag_adresi):
    """ARP tabanlı ağ taraması - Root gerektirir
    
    Args:
        ag_adresi: CIDR formatında ağ adresi (örn: 192.168.1.0/24)
    
    Returns:
        list: (ip, mac) tuple'larından oluşan liste
    """
    write_log(f"[~] 'arp_tara()' fonksiyonu çalıştırıldı - Ağ: {ag_adresi}", level="FUNC")
    aktif_cihazlar = []
    
    print(f"{clr.s}[#] {get_string('arp_scan_started')}{clr.r}\n")
    write_log(f"[#] {get_string('arp_scan_started')}", level="EXEC")
    
    try:
        # arp-scan ile tarama
        sonuc = subprocess.run(
            ["arp-scan", "--localnet", "--interface=auto"],
            capture_output=True, text=True, timeout=60
        )
        
        if sonuc.returncode == 0:
            # arp-scan çıktısını parse et
            for satir in sonuc.stdout.splitlines():
                # IP ve MAC adreslerini bul (format: 192.168.1.1\taa:bb:cc:dd:ee:ff\tVendor)
                eslesme = re.match(r'^(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F:]{17})', satir)
                if eslesme:
                    ip = eslesme.group(1)
                    mac = eslesme.group(2)
                    aktif_cihazlar.append((ip, mac))
                    write_log(f"[+] ARP bulundu: {ip} - MAC: {mac}", level="RESULT")
            return aktif_cihazlar
        else:
            write_log(f"[!] arp-scan hatası, nmap -sn deneniyor..", level="ERROR")
            
    except FileNotFoundError:
        write_log("[!] arp-scan bulunamadı, nmap -sn deneniyor..", level="ERROR")
    except subprocess.TimeoutExpired:
        write_log("[!] arp-scan zaman aşımı, nmap -sn deneniyor..", level="ERROR")
    except Exception as e:
        write_log(f"[!] arp-scan hatası: {e}, nmap -sn deneniyor..", level="ERROR")
    
    # Fallback: nmap -sn ile ARP taraması
    try:
        sonuc = subprocess.run(
            ["nmap", "-sn", ag_adresi],
            capture_output=True, text=True, timeout=120
        )
        
        if sonuc.returncode == 0:
            ip_pattern = re.compile(r'Nmap scan report for (?:.*\()?(\d+\.\d+\.\d+\.\d+)\)?')
            mac_pattern = re.compile(r'MAC Address: ([0-9A-Fa-f:]{17})')
            
            satirlar = sonuc.stdout.splitlines()
            mevcut_ip = None
            
            for satir in satirlar:
                ip_eslesme = ip_pattern.search(satir)
                if ip_eslesme:
                    mevcut_ip = ip_eslesme.group(1)
                
                mac_eslesme = mac_pattern.search(satir)
                if mac_eslesme and mevcut_ip:
                    mac = mac_eslesme.group(1)
                    aktif_cihazlar.append((mevcut_ip, mac))
                    write_log(f"[+] Nmap bulundu: {mevcut_ip} - MAC: {mac}", level="RESULT")
                    mevcut_ip = None
                elif mevcut_ip and ("Host is up" in satir):
                    # MAC bulunamazsa (local IP olabilir)
                    if not any(ip == mevcut_ip for ip, _ in aktif_cihazlar):
                        aktif_cihazlar.append((mevcut_ip, "N/A"))
                        write_log(f"[+] Nmap bulundu: {mevcut_ip} - MAC: N/A", level="RESULT")
            
            return aktif_cihazlar
        
    except FileNotFoundError:
        print(f"{clr.k}[!] {get_string('tools_missing_arp')}{clr.r}")
        write_log(f"[!] {get_string('tools_missing_arp')}", level="ERROR")
    except subprocess.TimeoutExpired:
        print(f"{clr.k}[!] {get_string('nmap_timeout')}{clr.r}")
        write_log(f"[!] {get_string('nmap_timeout')}", level="ERROR")
    except Exception as e:
        print(f"{clr.k}[!] {get_string('arp_scan_error')}: {e}{clr.r}")
        write_log(f"[!] {get_string('arp_scan_error')}: {e}", level="ERROR")
    
    return aktif_cihazlar
