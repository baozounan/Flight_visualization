from utils.convert import *
import json
def main():
    str='{"Pos":2962.7,"M":0.1,"GS":"64kts","G":1.2,"AGL":2967}'
    dict = json.loads(str)
    print(dict)
if __name__ == '__main__':
    main()