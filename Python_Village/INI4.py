file_path = '' #type your path here

with open(file_path, 'r') as f:
    a, b = list(map(int, f.readline().strip().split()))
    
if a > b:
    a, b = b, a
    

if a % 2 == 0:
    first_odd = a + 1
else:
    first_odd = a
    
if b % 2 == 0:
    last_odd = b - 1
else:
    last_odd = b
    

n = (last_odd - first_odd) // 2 + 1

sum = n * (first_odd + last_odd) // 2
print(sum) #This solution should be much faster than a complete brute-force.