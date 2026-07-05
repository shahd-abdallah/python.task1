# instant distant system
print("Welcome to the client")
price = float(input("Enter the price"))
if price < 100 :
 discount = 0.0
elif price < 500 :
 discount = 0.1
else  :
 discount = 0.2
discountValue = price * discount 
totalPrice = price - discountValue 
print ("Your discount is" , discountValue)
print ("Your total price is" , totalPrice)
print("#" * 30)
