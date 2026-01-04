from settings import set_themes as clr
from settings.set_loging import write_log
write_log("[#] 'help.py' dosyası çalıştırılı")

def yardım():
     write_log("[#] 'yardım()' fonksiyonu çalıştırıldı")
     print(f"""
{clr.k}[!] BU ARAÇ YALNIZCA EĞİTİM AMACIYLA HAZIRLANMIŞTIR{clr.r}

{clr.am2}[1] Port tarama menüsünü açar 
     {clr.am3}[-] 0- Ana menüye döner
     {clr.am4}[-] 1- [Başlangıç] - [Bitiş] port aralığını tarar
     {clr.am5}[-] 2- [443,8080,21,80...] Seçili portları tarar
     {clr.am6}[-] 3- [1-1024] Standart portları tarar 
     {clr.am7}[-] 4- [1-65535] Tüm portları tarar

{clr.am6}[2] Ağ tarama menüsünü açar
     {clr.am5}[-] 0- Ana menüye döner
     {clr.am4}[-] 1- Ağ taramasını başlatır

{clr.am5}[3] Ayarlar menüsünü açar
     {clr.am3}[-] 0- Ana menüye döner
     {clr.am2}[-] 1- Dil seçilir (Varsayılan Türkçe)
     {clr.am}[-] 2- Tema değiştirilir (Varsayılan Mavi)
     {clr.am2}[-] 3- Araç çalışırken izlediği yolu ve çıktıları daha sonra analiz edebilmek içn kayıt altına alır (Varsayılan kapalı)
     {clr.am3}[-] 4- Araç çalışırken ne kadar ram kullanıldığını gösterir (Varsayılan kapalı)
     """)
