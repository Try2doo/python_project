"""Use bitwise operations to perform the following:
1 Check the final value when 5 is performed bitwise AND with 7
2 Check the final value when 5 is performed bitwise OR with 2
3 y = 10 * 2. Solve the same problem using bitwise shift operation.
4 Multiply and divide an integer by 4 using bitwise shift operations."""

# bitwise AND
final_value  = 5 & 7
print(final_value)           # 5


#bitwise OR
final_value = 5 | 2
print(final_value)           # 7


#bitwise SHIFT
y = 10 >> 2
z = 20 << 2
print(y)   
print(z)

#bitwise multiply
n1 = 5
m = n1 * 4
print(m)                #20

# multiply by 4 using bitwise shift left
n1 = 5
m = n1 << 2
print(m)                #  20

# divide by 4 using bitwise shift right
d1 = n1 >> 2
print(d1)           #  1



