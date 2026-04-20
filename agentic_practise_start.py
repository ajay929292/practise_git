#Determine ticket prices based on age and "Member Status."

user_age=int(input("Enter your age : "))

if user_age>=18:
    membership=input("Do you have membership y/n : ")
    if membership=="y":
        print("Price is 10$")
    elif membership=="n":
        print("Price is 15$") 
    else:
        print("Pls write y or n")       
else:
    print("Price is 8$")


#Create a nested security check for a bank withdrawal.

pin=int(input("Enter your security pin : ")) 
if pin==1234:
    Balance=500
    Amount=int(input("Enter the withdrawl amount : "))
    if Amount<=Balance:
        print("Transaction successful")
    else:
        print("Insufficient Funds")    

else:
    print("Wrong pin")   
