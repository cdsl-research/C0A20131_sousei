from .web_rule import web_r
from .web_count import web_c
import yaml
import time
def web_print():
    with open('./conf.yaml','r') as file:
        aut = yaml.safe_load(file)
        Auto = aut["Auto"]
        if Auto == "Auto":
            cut = 0
            while True:
                url = web_c()
                web_p = web_r(url)
                cut += 1
                print(web_p) 
                time.sleep(10)

        else:
            url = web_c()
            web_p = web_r(url)

