from importlib import import_module #import_moduleをインポート
import yaml #yamlをimport
def run():  #run()関数実行関数
    with open('conf.yaml','r') as file: 
        ob = yaml.safe_load(file)
        modules = ob["module"] #モジュールを読み込む
        condition = ob["conditions"]
        for k,v in modules.items():
            modules2 = import_module(f"{k}.main") #関数読み込み
            print(v)
            modules2.main(**v) #実行         
run()
    