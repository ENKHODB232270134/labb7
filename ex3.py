uzeg = 5.8  
marker = 7.2  
nuntag = 1.2   

u = int(input())  
m = int(input())  
n = float(input())  
k = float(input())

s = ((u*uzeg) + (m*marker) + (n*nuntag)) - (((u*uzeg) + (m*marker) + (n*nuntag)) /100* k)

print(f"Niit: {s} dollar")
