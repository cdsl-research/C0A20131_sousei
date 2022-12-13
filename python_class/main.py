import yaml
import select_m
import time
with open('conf.yaml','r') as file:
         sel = yaml.safe_load(file)
         sel2 = sel["method"]
         sel3 = sel2["Step"]
         cnt = 0
         while True:
            selct = select_m.get_select()
            print(selct)
            time.sleep(int(sel3))
            cnt +=1
