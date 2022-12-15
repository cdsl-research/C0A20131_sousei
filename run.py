from importlib import import_module
import yaml
def run(): 
    with open('conf.yaml','r') as file:
        module = yaml.safe_load(file)
        modules = module["module"]
        for i in modules:
            modules2 = import_module(f"{i}.main")
            modules2.main()
        
        
    
run()
    