class machine:
    def product_info(self):
        self.product1="Coke"
        self.product2="Water"
        self.product3="String"
        self.product4="Pepsi"
        self.product5="Thump ups"
        self.prod1_price=80
        self.prod2_price=30
        self.prod3_price=60
        self.prod4_price=120
        self.prod5_price=100
    def show_product_info(self):
        print("Product_Name \t Price(Rs.)")
        print(f"{self.product1} \t\t {self.prod1_price}")
        print(f"{self.product2} \t\t {self.prod2_price}")
        print(f"{self.product3} \t\t {self.prod3_price}")
        print(f"{self.product4} \t\t {self.prod4_price}")
        print(f"{self.product5} \t {self.prod5_price}")
    
    def pay_option(self):
        print("You Can Pay in Dollar!")
        print("1 Rs. \t 2 Rs. \t 5 Rs. \t 10 Rs. 20 Rs")
    
    def final_payment(self,bill):
        print()
        sum=0
        ch='y'
        print("Enter Dollar:- ")
        while(ch=='y'):
            pay=int(input())
            if pay==1 or pay==2 or pay==5 or pay==10 or pay==20:
                sum=sum+pay
                check=bill-sum
                if check!=0:
                    print(f"You Have to Pay More {bill-sum} Rs.")
                if sum==bill:
                    ch='n'
                    print()
                    print("Payment Done!")
                    print()
                    print("Take Your Product From Below")
                    print()
                    print("--------Thank You For Purchase--------")
            else:
                print("You Haven't Entered Dollar!")
                print(f"You Have to Enter More {bill-sum} Rs.")

print("--------Welcome--------")
print()
m1 = machine()
m1.product_info()
m1.show_product_info()
print()

print("1.Coke")
print("2.Water")
print("3.String")
print("4.Pepsi")
print("5.Thump ups")
inp=int(input("Which product You Want To Purchase:- "))
print()

if inp==1:
    qunt=int(input("How Many Quantity You Want:- "))
    print()
    bill=qunt*m1.prod1_price
    print(f"You Have to Pay {bill} Rs.")
    print()
    m1.pay_option()
    m1.final_payment(bill)
elif inp==2:
    qunt=int(input("How Many Quantity You Want:- "))
    bill=qunt*m1.prod2_price
    print(f"You Have to Pay {bill} Rs.")
    m1.pay_option()
    m1.final_payment(bill)
elif inp==3:
    qunt=int(input("How Many Quantity You Want:- "))
    bill=qunt*m1.prod3_price
    print(f"You Have to Pay {bill} Rs.")
    m1.pay_option()
    m1.final_payment(bill)
elif inp==4:
    qunt=int(input("How Many Quantity You Want:- "))
    bill=qunt*m1.prod4_price
    print(f"You Have to Pay {bill} Rs.")
    m1.pay_option()
    m1.final_payment(bill)
elif inp==5:
    qunt=int(input("How Many Quantity You Want:- "))
    bill=qunt*m1.prod5_price
    print(f"You Have to Pay {bill} Rs.")
    m1.pay_option()
    m1.final_payment(bill)


