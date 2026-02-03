"""
ASSIGNMENT OPERATOR
-the assignment operator is "="
- it is used to assign values on the right to the variable on the left.
Example:
    total= 100
    the assignment operator "=" takes the value 100 and stores it on the left
    which is the address to  a storage location termed as "variable" total.


Compound assiggment operators
-this is a combination of assigment operators and arithmetic operators. 
  a) += addition equal to
  b) -= subtraction equal to
  c) *= multiplication equal to
  d) /= divition equal to 
  e) **= exponent equal to
  f) //= floor division  equal to
  g) %= modulus equal to

Example
    k = 7
    k += 2 this  is like saying :
        k = k + 2
        the  new value stored in "k" will be - 9  
"""

j = 6
print(f"the old value of j is {j}")
j+=4 # j = j + 4
print(f"the new value of j is {j}")

k = 5
k//= 2 # k=k // 2
print(k)