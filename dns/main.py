import subprocess
def dns(name,num):
    num2 = 0
    while True:
        if num2 == num:
            break
        Addr = subprocess.run(["nslookup",name],stdout=subprocess.PIPE)
        print(Addr.stdout.decode("cp932"))
        if Addr.returncode == 0:
            print("成功")
        else:
            return False
        print("----------")
        num2 += 1
        
def main(**kwargs):     
    dns(kwargs["domain_name"],kwargs["dns_count"])
    
