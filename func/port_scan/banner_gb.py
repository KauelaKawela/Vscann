import socket

def banner_grabbing(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        banner = s.recv(1024).decode("latin-1",errors="ignore").strip()
        if "HTTP" in banner:
            return f"HTTP Servisi - {banner}"
        elif "SSH" in banner:
            return f"SSH Servisi - {banner}"
        elif "FTP" in banner:
            return f"FTP Servisi - {banner}"
        elif "MariaDB" in banner:
            return f"MariaDB servisi - {banner}"
        else:
            return f"Bilinmeyen Servis - {banner}"
    except socket.error:
        return f"banner bilgisi alınamadı"
