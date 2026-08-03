import socket


def resolve(target):

    try:
        ip = socket.gethostbyname(target)
        return ip

    except socket.gaierror:
        return None
