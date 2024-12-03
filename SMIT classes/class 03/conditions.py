age = {
    'manzoor :20',
    'ayaz: 18',
    'Kamran : 16'

}

for members in age:
    print(f'Name of Members age : {members}')

match = 0

check = (input('enter member name '))


if check in age >18:
    match +=age[check]
    print(f"You are age  {check} your are  eligible ")
else:
    print(f"order item {check} not eligible yet")

another = input("do you want to check another member age (Yes/No)")

if another == "Yes":
    check2 = input("enter your another member = ")
    if check2 in age >20:
       match += age[check2]
       print(f"order item2 {check2} has eligible")
    else:
     print(f"order item {check2} not eligible")
print(f"the total members mathched are : {match} ")

# While statement
i = 0
while i <= 10:
    print(i)
    i +=1