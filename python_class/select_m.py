import yaml
import DNS_S
import Web_S
import log_S
#import test
def get_select():

    with open('conf.yaml','r',) as file:#yamlファイルを読み込み
        IP_dict = yaml.safe_load(file)
        sect = IP_dict["method"]
        if "DNS" in sect:
            DNS_P = DNS_S.print_DNS()
        if "Web" in sect:
            Web_P = Web_S.print_Web()
        if "log" in sect:
            log_P = log_S.log_print()



            
        
        #return sect
        
        
get_select()
