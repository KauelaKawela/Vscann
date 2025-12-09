import socket

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Bilinmeyen servis"
            