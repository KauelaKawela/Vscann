import time,clr,socket
from func import helper_func as hf
from func import get_service_name as gsn
from func import banner_gb as b_gb

acık_port=[]
port_list=[]

def port_taraması(ip,port):
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.settimeout(0.5)
      try:
            start_time = time.time()
            sonuc = s.connect_ex((ip,port))
            son_time = time.time() - start_time
            if sonuc == 0:
                  banner = b_gb.banner_grabbing(ip,port)
                  servis = gsn.get_service_name(port)
                  print(f"{clr.y}[ + ]{clr.r} Port {port} {clr.y}açık{clr.r} - {clr.y}Servis:{clr.r} {servis} - {clr.y}Süre:{clr.r} {son_time}- {clr.y}Banner:{clr.r} {banner}")
                  acık_port.append((port,servis,son_time,banner))
            else:
                  servis = gsn.get_service_name(port)
                  print(f"{clr.k}[ - ] {clr.r}Port {port} {clr.k}kapalı{clr.r} - {clr.k}Servis:{clr.r} {servis} - {clr.k}Süre:{clr.r} {son_time} ")
      except Exception as e:
            print(f"{clr.k}[!] Port {port} hatası: {e}{clr.r}")
            hf.cık()
      except socket.timeout:
            print(f"{clr.k}[!] Port: {port} Zaman aşımı!{clr.r}")
            hf.cık()
      except ConnectionRefusedError:
            print(f"{clr.k}[!] Port: {port} Bağlantı reddedildi! {clr.r}") 
            hf.cık()
      except socket.error as se:
            print(f"{clr.k}[!] Port: {port} Soket oluşturulamadı: {se}{clr.r}") 
            hf.cık()
      finally:
            s.close()