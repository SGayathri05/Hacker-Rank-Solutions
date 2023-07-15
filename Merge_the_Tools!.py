from collections import OrderedDict as od

def merge_the_tools(string, k):
    n = len(string)
    l = n//k
    for i in range(l):
        print("".join(od.fromkeys(string[i*k:(i*k)+k])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
