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
        
def main(**kwargs):
    log(kwargs["log_path"],kwargs["log_count"])
   
