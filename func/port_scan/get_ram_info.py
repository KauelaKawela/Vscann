from settings import set_themes as clr

def get_ram_info():
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
            total = int(lines[0].split()[1]) // 1024
            free = int(lines[1].split()[1]) // 1024
            available = int(lines[2].split()[1]) // 1024
            used = total - available
            percent = used * 100 // total
            if percent >= 80:
                renk = clr.k # Kırmızı
            elif percent >= 50:
                renk = '\033[93m'  # Sarı
            else:
                renk = '\033[92m'  # Yeşil
            output = f"[RAM] Kullanılan: {used}MB / {total}MB  ({percent}%)"
            print(f"{renk}{output}{clr.r}")
            return output
    except Exception as e:
        print(f"{clr.k}[RAM] Bilgi alınamadı: {e}{clr.r}")
        return f"[RAM] Bilgi alınamadı: {e}"