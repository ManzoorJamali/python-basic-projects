

# If ifelse loop while loop combine assignment

menu ={
    'pizza':40,
    'Burger':60,
    'coffee':80,
    'salad': 60,

}
print("Welcome to Python restaurant")
print('available Items')
for items in menu:
  
   print(f' => {items}')
order_total = 0 
item1 = input("enter your first Item = ")
if item1 in menu:
    order_total +=menu[item1]
    print(f"your item {item1} has been added ")

else:
    print(f"order item {item1} not availabel yet")

another = input("do you want to another order (Yes/No)")

if another == "Yes":
    item2 = input("enter your another order = ")
    if item2 in menu:
       order_total += menu[item2]
       print(f"order item2 {item2} has been aded")
    else:
     print(f"order item {item2} not available")
print(f"the total amount is : {order_total} ")

# while Statemet

order = 0
print('while statmemt')
while order <4:
   print(order)
   order +=1
   
