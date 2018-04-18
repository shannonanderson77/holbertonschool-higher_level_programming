#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    list = list(filter(lambda x: not x.startswith('__'), names))
    for i in range(len(list)):
        print("{}".format(list[i]))
