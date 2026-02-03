order = 400

if order > 100 :
    discount = 25
    print(order,discount) 

else:
    discount = 0
    print(order,discount)

discount = 25 if  order > 100  else 0 #discount = 25 , discount = 0 
print(order,discount)