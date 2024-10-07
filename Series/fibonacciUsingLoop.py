prev1=0
prev2=1

print(prev1)
print(prev2)

for fibo in range(10):
    newfibbo = prev1+prev2
    print(newfibbo)
    prev2 = prev1
    prev1=newfibbo
