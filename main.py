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

def ex_func(n1,n2):
    #result = 0
    #print(n1, '-', n2, "=", result)
    return n1/n2

def square_func(n1,n2):
    return n1**n2
## 전역 변수부
num1, num2 , result = 100,200, 0

## main

result = add_func(num1,num2)

print(num1, '+', num2, "=", result)
result = sub_func(num1,num2)
print(num1, '-', num2, "=", result)
result = mul_func(num1,num2)
print(num1, '*', num2, "=", result)
result = ex_func(num1,num2)
print(num1, '/', num2, "=", result)

result = square_func(num1,num2)
print(num1, '**', num2, "=", result)
