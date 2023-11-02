#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add 
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div
  
a=10
b=5
summ = add(a,b)
diff = sub(a,b)
divi = div(a,b)
mult = mul(a,b)

print("{:d} + {:d} = {:d}".format(a,b,summ))
print("{:d} - {:d} = {:d}".format(a,b,diff))
print("{:d} / {:d} = {:d}".format(a,b,divi))
print("{:d} x {:d} = {:d}".format(a,b,mult))
