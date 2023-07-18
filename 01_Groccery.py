Grossery={ 'product1':{'product_id':1,'product_name':'Maggie','stock':1000,'price':10},
           'product2':{'product_id':2,'product_name':'Biscuit','stock':1000,'price':10},
           'product3':{'product_id':3,'product_name':'Salt','stock':1000,'price':20},
           'product4':{'product_id':4,'product_name':'Chips','stock':1000,'price':10},
           'product5':{'product_id':5,'product_name':'Soap','stock':1000,'price':25}
        }
ch='yes'
while(ch=='yes'):
    print("Menu:-")
    print("1.Add New Product")
    print("2.Show All Product")
    print("3.Update Specific Product")
    print("4.Delete Product")
    print("5.Purchase Product")
    print("6.Exit From The Store")

    inp=int(input("Enter The Choice from Menu:- "))
    new_dict={}
    upd_dict={}
    del_dict={}
    check=0
    count=0
    delete=0

    if inp==1:
        key=input("Enter The New Product Code:- ")
        for i in range(0,1):
            k='product_id'
            v=int(input("Enter The Product Id: "))
            new_dict.update({k:v})
        for i in range(0,1):
            k='Product_name'
            v=input("Enter The Product Name: ")
            new_dict.update({k:v})
        for i in range(0,1):
            k='stock'
            v=int(input("Enter The Product Stock: "))
            new_dict.update({k:v})
        for i in range(0,1):
            k='price'
            v=int(input("Enter The Product Price: "))
            new_dict.update({k:v})
        Grossery.update({key:new_dict})
        print("Your Product Has Been Added Sucessfully.")
        print()
        for key,val in Grossery.items():
            print(f"{key}:{val}")
        print("Do You Want to Return To The Main Menu")
        ch=input("Yes or No:- ")
    elif inp==2:
        for key,val in Grossery.items():
            print(f"{key}:{val}")
        print("Do You Want to Return To The Main Menu")
        ch=input("Yes or No:- ")
    elif inp==3:
        upd=input("Enter The Product Code You Want to Update:-")
        for key,val in Grossery.items():
            if check==0:
                if key==upd:
                    for i in range(0,1):
                        k='product_id'
                        v=int(input("Enter The Product Id: "))
                        upd_dict.update({k:v})
                    for k,v in val.items():
                        if count==0:
                            for i in range(0,1):
                                k1='product_name'
                                v1=input("Enter The Product Name:")
                                if k1=='product_name' and v==v1:
                                    upd_dict.update({k1:v1})
                                    count=1
                                else:
                                    print("This Product is not Present in this id!")
                                    print("Enter The Product Name Again!")
                    for i in range(0,1):
                        k='stock'
                        v=int(input("Enter The  New Stock: "))
                        upd_dict.update({k:v})
                    ch1=input("Do You Want to Update The Price also:- ")
                    if ch1=='yes':
                        for i in range(0,1):
                            k='price'
                            v=int(input("Enter The New Price: "))
                            upd_dict.update({k:v})
                    else:
                        for key,val in Grossery.items():
                            if key==upd:
                                for k,v in val.items():
                                    if k=='price':
                                        upd_dict.update({k:v})
                    check=1
        if check==1:
            Grossery.update({upd:upd_dict})
            print("Your Product Has Been Updated Sucessfully.")
            print()
            for key,val in Grossery.items():
                print(f"{key}:{val}")
        else:
            print("You have entered Wrong Product Code!")
        print("Do You Want to Return To The Main Menu")
        ch=input("Yes or No:- ")
    elif inp==4:
        dele=input("Enter The Product Code You Want to delete:- ")
        print()
        for key,val in Grossery.items():
                if key==dele:
                    del Grossery[dele]
                    delete=1
                    break
        if delete==1:
            print("Your Product has been deleted successfull.")
            print()
            for key,val in Grossery.items():
                print(f"{key}:{val}") 
        else:
            print("The Product You Want to Delete is not Present in the Store!")
        print("Do You Want to Return To The Main Menu")
        ch=input("Yes or No:- ")
    elif inp==5:
        ch1='yes'
        temp=1234
        pur=0
        while(ch1=='yes'):
            print("Which Product You Want To Purchase From The List:- ")
            print()
            for key,val in Grossery.items():
                print(f"{key}:{val}")
            print()
            key1=input("Enter The Product Code:- ")
            v1=int(input("Enter The Product id:- "))
            buy=int(input("How many Quantity You Want:- "))
            for key,val in Grossery.items():
                for k,v in val.items():
                    if key==key1:
                        if k=='price':
                            bill=v*buy
                            print(f"You Have Bought {buy} Quantity of {val['product_name']}")
                            print(f"Your Total Bill is {bill}Rs.")
                            print(f"You Have to Pay = {bill}Rs.")
                            pur=1
            while(pur==1):
                pay=int(input("For Payment Enter Your bill:- "))
                if bill==pay:
                    print("Payment Done.")
                    pur=0
                else:
                    rem=bill-pay
                    print(f"You have to pay more {rem}Rs.")
                    pay=int(input("For Payment Enter Your remaining bill:- "))
                    print("Payment Done.")
                    pur=0
            for key,val in Grossery.items():
                for k,v in val.items():
                    if key==key1:
                        if k=='stock':
                            v=v-buy
                            Grossery[key]['stock']=v
            print("Do You Want to Purchase Again:- ")
            ch1=input("Yes or No:- ")
            if ch1=='no':
                print("Thank You For Visiting The Store.")
        print("Do You Want to Return To The Main Menu")
        ch=input("Yes or No:- ")
    elif inp==6:
        ch3=input("Are You Sure You Want to Exit From Store:- ")
        if ch3=='yes':
            ch='no'

