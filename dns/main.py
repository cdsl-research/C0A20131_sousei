import subprocess
def dns(name,num):
    num2 = 0
    while True:
        if num2 == num:
            break
        Addr = subprocess.run(["nslookup",name],stdout=subprocess.PIPE)
        print(Addr.stdout.decode("cp932"))
        if Addr.returncode == 0:
            ans = "成功"
            #print("成功")
        else:
            #return False
            ans = "失敗"
        print("----------")
        num2 += 1
    return ans
        
def main(**kwargs):     
    return dns(kwargs["domain_name"],kwargs["dns_count"])