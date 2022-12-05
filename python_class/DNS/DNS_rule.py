import subprocess
import socket
def DNS_rule1(name):
    Addr = socket.gethostbyname(name)
    try:
        return Addr
    except:
        return "失敗"
    
def DNS_rule2(name):
    Addr = subprocess.run(["nslookup",name],stdout=subprocess.PIPE)
    print(Addr.stdout.decode("cp932"))
    if Addr.returncode == 0:
        return "成功"
    else:
        return "失敗"
    print("----------")
    
    
