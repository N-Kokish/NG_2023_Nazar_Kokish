import platform
import socket
import psutil
memory_info = {
        'Total RAM': round(psutil.virtual_memory().total / (1024 ** 3), 2),
        'Available RAM': round(psutil.virtual_memory().available / (1024 ** 3), 2),
    }
print(memory_info)
print("processor: ",platform.processor())
print("system release version: ",platform.uname())
host_name = socket.gethostname()
print("Ip :",socket.gethostbyname(host_name))
