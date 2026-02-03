"""
LOGICAL OPERATORS 
They are usad to evaluate two different operations
The result of the operation is always boolean expression (True or False).

examples 
a) and 
> This operators indicates that the two operation that is operation _1 and operation_2 
must be true ,in order for the entire statement to be true.
b)This operator indicate that the either or two operations that is operation_1 and operation_2
can de true in oder for the entire statement to be true.
c) not 
>This operators revers the outcome of the operation.

operation_1  p
a=6
b=2
p=a > b

operation_2 q
c=9
d=15
q = c> d

print(operation_1 and operation_2)

print(q and p)


True Table 
p       q         P AND Q       P OR Q     NOT P     NOT Q
True   True        True         True        False    False      
True   False       False        True        False    True   
False  True        False        False       True     False
False  False       False        False       True     True 

"""

# operation 1
p=5<4
print(p)

# operation 2
q=9>6
print(q)

# AND
print(p and q)

# OR 
print(p or q)

# NOT 
print(not(p or q))