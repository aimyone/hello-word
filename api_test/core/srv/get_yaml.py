import yaml
def get_data():
    file = open("../../common/yaml.yaml", 'r', encoding='utf-8')
    abc = yaml.load(stream= file, Loader=yaml.Loader)
    print(abc)
    for y in abc:
        print(y,)
        return y