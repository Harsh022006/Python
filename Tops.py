class Tops:
    def admission(self,sname,contact,course,fees):
        self.sname=sname
        self.contact=contact
        self.course=course
        self.fees=fees
        
        print("Name :",sname)
        print("Contact No : ",contact)
        print("Course Details : ",course)
        print("Your Course Fees is : ",fees)

    def installment(self,amount):
        if self.fees<amount:
            print("you can't pay over the Fees !, Please check Fees Details.")

        else:
            print(amount,"Received Money successfully..!")

    def remainingfees(self):
        self.fees=self.fees-amount
        if self.fees==0:
            print("Your Fees is Fullfilled")

        else:
             print("Your pending fees :",self.fees)
       
t1=Tops()

print("*"*50)
print("Hello, Welcome to Tops Technologies..!")

while True:
    print("*"*50)
    print("1. Check Out Your Profile")
    print("2. Pay fees")
    print("3. Check pending fees")
    print("4. Exit")

    print("*"*50)
    choice=int(input("Enter Your Choice : "))

    
    if choice==1:
        t1.admission("Harsh Amburkar",7096097144,"Full Stack-Python",100000)

    elif choice==2:
        amount=int(input("Enter Your Fees installments : "))
        t1.installment(amount)

    elif choice==3:
        print("Remaining Fees :")
        t1.remainingfees()

    elif choice==4:
        print("Thank You For Using Our Service.")
        break

else:
    print("Invalid choice. Please Choose Between 1 to 4")
    
        


        
        

    

        
            
