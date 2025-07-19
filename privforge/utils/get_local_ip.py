import psutil

def get_ip():
    ip_list = [
        addr.address
        for iface, addrs in psutil.net_if_addrs().items()
        for addr in addrs
        if addr.family == 2 and not addr.address.startswith("127.")
    ]
    
    return ip_list[0] if ip_list else None