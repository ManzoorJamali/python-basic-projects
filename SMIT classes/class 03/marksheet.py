
# Marksheet in python
sub1  = int (input('Enter sub1 Marks = '))
sub2  = int (input('Enter sub2 Marks = '))
sub3  = int(input('Enter sub3 Marks = '))
sub4  = int(input('Enter sub4 Marks = '))
sub5  = int (input('Enter sub5 Marks = '))

total = 500
obt = sub1+sub2+sub3+sub4+sub5

precentage = obt*100/total
grade =precentage

if precentage <=100 and precentage > 80:
    print(f'You are Pass :Grade A')
elif precentage <=80 and precentage >60:
    print(f'You are Pass: Grage B')
elif precentage <=60 and precentage >50:
    print(f'You are Pass: Grage  c')
elif precentage <=50 and precentage >40:
    print(f'You are Pass: Grage  D')
else:
    print("You are Fail")
print(f'Obtained marks{obt}')
print(f"Total Marks = {total}")
print(f"percentage = {precentage}")
print(f"result {grade}")