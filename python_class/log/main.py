import yaml
def log(log,num):
    num2 = 0
    while True:
        if num2 == num:    
            break
        with open(log) as file:
            a = len(file.readlines())
            print(a)
        if a == 0:
            return False
        num2 += 1
        
def main():
    with open('../conf.yaml','r') as file:
       log1 = yaml.safe_load(file)
       log2 = log1["module"]
       log3 = log2["log"]
       log_count = log3["log_count"]
       log_path = log3["log_path"]
       log(log_path,log_count)
   
if __name__ == '__main__':
    main()
