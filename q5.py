def minimum(x, y, z): 
  
    if x < y: 
        if x < z: 
            return x 
        else: 
            return z 
    else: 
        if y < z: 
            return y 
        else: 
            return z 
  
a = 10
b = 4
c = 12
print(minimum(a, b, c))