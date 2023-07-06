##
def add_func(n1,n2):
    #result = 0
    #print(n1, '+', n2, "=", result)
    return n1+n2

def sub_func(n1,n2):
    #result = 0
    #print(n1, '-', n2, "=", result)
    return n1-n2

def mul_func(n1,n2):
    #result = 0
    #print(n1, '-', n2, "=", result)
    return n1*n2

# def ex_func(n1,n2):
#     #result = 0
#     #print(n1, '-', n2, "=", result)
#     return n1/n2

## 전역 변수부
num1, num2 , result = 100,200, 0

## main

result = add_func(num1,num2)

print(result)
result = sub_func(num1,num2)
print(result)
result = add_func(num1,num2)
print(result)
