import yaml
def web_c():
    with open('./conf.yaml') as file:
        web_c = yaml.safe_load(file)
        web_s = web_c["url"]
        return web_s


