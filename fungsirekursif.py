def foo(a):
    if a <= 0: return 0

    return foo (int(a / 10)) + a % 10
        
      
print(foo(123))
print (foo(211122))
print (22)

