"""name, age, height = ("Bikash", 37, 5.9)
print("Bikash")
print(f"Hello my name is {name}. I am {age} years old. My height is {height:0.2f}ft.")
print("-" * 100)
print("=" * 60)
input = input("Enter your no.")
number = float(input)
print(number % 1)
if number <= 0 or number >= 0 and number % 1 == 0 :
    print(f"given no {number} is int")
else:
    print(f"given no {number} is not int")
"""
j = True
while j is True:
    word = input("Enter Your word:  ")
    revstr = ""
    for i in word:
        revstr = i + revstr
        # print(revstr)
    print(revstr)
    if word == revstr:
        print("IsPalindrome")
    else:
        print("IsNotPalindrome")
    
    

    print("Do wanna exit, press 'Y' ")
    value=input()
    if value=="y" or value=="Y":
        j=False
    else:
        j=True

    continue
