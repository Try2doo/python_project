#Q02010 answers:

#check whether the number 12 is an integer or not
number = 12
print(type(number))   # class 'int'
# print(type(12))      # class 'vfhgvhgvnb;

#divide 100 by 12 and check whether the number is float or not
d = 100
x = 12
r = d / x
print(r)
if isinstance(r, float):
    print("the number is float")
else:
    print("the number is not float")   # the number is float and 8.333333333334


#Is x identical to y? Is x identical to z?
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = x
print("x is identical to y:", x is y)   #False
print("x is identical to z:", x is z)   #True


#Check programmatically whether lion is in the zoo or not.
#Check programmatically whether horse is in the zoo or not.
zoo = ["elephant", "tiger", "zebra", "lion", "wolf"]
if "lion" not in zoo:
    print("yes, lion is not in the zoo")
else:
    print("No, lion is in the zoo")  # yes, lion is in the zoo

if "horse" in zoo:
    print("yes, horse is in the zoo")
else:
    print("No,horse is not in the zoo")   # No, horse is not in the zoo


#Create a list of first 7 prime numbers and check whether 9 is a prime number or not using membership operation.


prime_numbers = [2,3,5,7,11,13,17]
if 9 in prime_numbers:
    print("yes, 9 is a prime number")
else:
    print("9, is not a prime number")  # 9 is not a prime number.

