from settings import set_themes as clr
from settings.set_loging import write_log
write_log("[#] 'help.py' dosyası çalıştırılı")

def yardım():
     write_log("[#] 'yardım()' fonksiyonu çalıştırıldı")
     print(f"""
{clr.am3}[-] 0- Çalışmayı sonlandırır
{clr.am4}[-] 1- [Başlangıç] - [Bitiş] port aralığını tarar
{clr.am5}[-] 2- [443,8080,21,80...] Seçili portları tarar
{clr.am6}[-] 3- [1-1024] Standart portları tarar 
{clr.am7}[-] 4- [1-65535] Tüm portları tarar
{clr.am6}[-] 5- Bilgilendirme
     """)
