count = 0 # 0, 1,2,3,4,5,6

while count < 50 : # true,true,true,true,true,true
    print(count) # 0, 1, 2, 3, 4, 5
    if count == 10:
        break
    count += 1 # 0+1,1+1,2+1,3+1,4+1,5+1
    
# reverse 
t = 5
while t >= 0 : 
    print(t)
    if t == 2:
        continue
    t -= 1
