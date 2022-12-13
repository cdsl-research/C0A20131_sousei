import subprocess
import yaml
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
        
def main():
    with open('../conf.yaml','r') as file:
        dns1 = yaml.safe_load(file)
        dns2 = dns1["module"]
        dns3 = dns2["dns"]
        dns_count = dns3["dns_count"]
        domain_name = dns3["domain_name"]       
        dns(domain_name,dns_count)
       
if __name__ == '__main__':
    main()
        
        
        

 
    
