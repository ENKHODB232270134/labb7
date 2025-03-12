a1 = int(input())
a2 = int(input())
a3 = int(input())


n = int((a1 + a2 + a3) / 60)  
sec = (a1 + a2 + a3) % 60

print(f"{n}:{sec:02}")
