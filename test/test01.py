from utils.convert import *
def main():
    str = "AGL:8745"
    dict = str2dict(str)
    print(type(dict))
    print(dict)
if __name__ == '__main__':
    main()