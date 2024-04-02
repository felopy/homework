#28
def find_index(haystack,needle):
    n = []
    if needle in haystack:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                return i
    else:
        return -1
print(find_index("orange","ang"))

#69
def square_up(n):
    x = n
    for i in range(n-1):
        x += n
    return x
print(square_up(int(input("Enter digit: "))))

#202
def happy(x):
    k = str(x)
    if -4 < x < 4:
        return None
    else:
        while True:
            n = 0
            for i in k:                
                n += (int(i)**2)
            if len(k) == 1:
                return None
            if n == 1:
               return "happy"
            else:
                k = str(n)
                continue
print(happy(int(input("Enter num: "))))
        


