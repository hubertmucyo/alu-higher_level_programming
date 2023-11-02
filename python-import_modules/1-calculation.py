#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1.py as obj
  
a = 10
b = 5
summ = obj.add(a,b)
diff = obj.sub(a,b)
divi = obj.div(a,b)
mult = obj.mul(a,b)

print("{:d} + {:d} = {:d}".format(a,b,summ))
print("{:d} - {:d} = {:d}".format(a,b,diff))
print("{:d} / {:d} = {:d}".format(a,b,divi))
print("{:d} x {:d} = {:d}".format(a,b,mult))
