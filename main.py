##
def add_func(n1,n2):
    #result = 0
    #print(n1, '+', n2, "=", result)
    return n1+n2

## 전역 변수부
num1, num2 , hap = 100,200, 0

## main

hap = add_func(num1,num2)
print(hap)