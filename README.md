# ⚡ Vscann

## ⚠️ Sorumluluk Reddi

Bu araç **yalnızca eğitim ve yetkili sızma testleri** için geliştirilmiştir.

- **İzinsiz** ağlara, sistemlere veya cihazlara tarama yapmayınız.
- Bu aracın **kötüye kullanımı** durumunda geliştirici hiçbir şekilde **sorumlu değildir**.
- Kullanımınız, **bulunduğunuz ülkenin yasaları** ile tamamen sizin sorumluluğunuzdadır.

`Vscann.py`, hedef bir IP adresindeki açık portları tespit etmeye yarayan, Python ile yazılmış terminal tabanlı bir port tarama aracıdır.

## 🚀 Özellikler

- IP adresine **ping** atarak ağda olup olmadığını kontrol eder.
- Seçilebilir dört farklı tarama modu:
  - **Aralık tarama** (Örn: 20–100)
  - **Belirli portlar** (Virgülle ayırarak: 21,22,80,443)
  - **Standart tarama** (1–1024)
  - **Tüm portlar** (1–65535)
- Açık portlarda:
  - Servis adı tespiti (`getservbyport`)
  - Banner grabbing (banner bilgisini alma)
  - Tarama süresi ölçümü
- Kullanılan RAM miktarı gösterimi (başlangıçta)
- ANSI renklerle zenginleştirilmiş arayüz

---

## 📦 Gereksinimler

- Python 3.x
- Linux ortamı (ping ve `/proc/meminfo` desteği için)

> **Not:** `Termux`, Kali Linux veya diğer Debian tabanlı sistemlerde sorunsuz çalışır.

---

## ⚙️ Kurulum

```bash
git clone https://github.com/KauelaKawela/vscann
cd vscann
python3 Vscann.py
```



# ⚡ Vscann

## ⚠️ Disclaimer

This tool is intended **strictly for educational and authorized penetration testing purposes** only.

- Do **not** scan or target networks, systems, or devices without **explicit permission**.
- The developer is **not responsible** for any misuse or damage caused by this tool.
- Use it **at your own risk** and in **compliance with all applicable laws** in your jurisdiction.

`Vscann.py` is a terminal-based port scanning tool written in Python that detects open ports on a target IP address.

## 🚀 Features

- Checks if the target IP is reachable by sending a **ping**.
- Offers four scanning modes:
  - **Range scan** (e.g., 20–100)
  - **Selected ports** (comma-separated list: 21,22,80,443)
  - **Standard scan** (ports 1–1024)
  - **Full scan** (ports 1–65535)
- For open ports:
  - Service name detection (`getservbyport`)
  - Banner grabbing
  - Response time measurement
- Displays used RAM information at startup
- Colorful terminal output using ANSI codes

---

## 📦 Requirements

- Python 3.x
- Linux environment (required for `ping` and `/proc/meminfo` access)

> **Note:** Fully compatible with **Termux**, **Kali Linux**, and other Debian-based systems.

---

## ⚙️ Installation

```bash
git clone https://github.com/KauelaKawela/vscann
cd vscann
python3 Vscann.py
```