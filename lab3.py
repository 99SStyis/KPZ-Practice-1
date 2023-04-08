import re
import platform

def palindrom(text):
    if not text or not isinstance(text, str):
        raise TypeError("Please, type string")

    words = text.split()
    result = []
    for word in words:
        if word == word[::-1]:
            result.append(word) 
    return result 


def validate_ip(ip_address):
    if not ip_address or not isinstance(ip_address, str):
        raise TypeError("Please, type string")
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if not pattern.match(ip_address):
        return False
    parts = ip_address.split('.')
    for part in parts:
        if not 0 <= int(part) <= 255: 
            return False
    return True 


def get_os():
    os = platform.system() 
    if os == 'Darwin':
        return 'Mac'
    elif os == 'Windows':
        return 'Windows'
    elif os == 'Linux':
        return 'Linux'
