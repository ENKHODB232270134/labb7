a = int(input())

if a <= 100:
   b = 5
elif a < 1000:
   b = a * 0.2
else:
   b =a * 0.1

if a % 2 == 0:
    b += 1
if a % 10 == 5:
    b += 2

f = a + b
print(f"\n{a} \n{b} \n{f}")
