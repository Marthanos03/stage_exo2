import socket


def check_port(ip: str, port: int) -> bool:
    """check if a port is open or closed"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port " + str(port) + " on " + ip + " is open")
                return True
            else:
                print("Port " + str(port) + " on " + ip + " is closed")
                return False
        except socket.error as e:
            print("error append " + e)
            return False


check_port('localhost', 8080)
