class Transactionsapp:
    def __init__(yours):
        yours.users_info_list = []
        yours.signedin = False
        yours.availablemoney = 00
        yours.TranferCash = False

    def register(yours, name , ph , password):
        availablemoney = yours.availablemoney
        contitions = True
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
            contitions = False

        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
            contitions = False

        if contitions == True:
            print("Account created successfully")
            yours.users_info_list = [name , ph , password , availablemoney]
            with open(f"{name}.txt","w") as f:
                for details in yours.users_info_list:
                    f.write(str(details)+"\n")


    def login(yours, name , ph , password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            yours.users_info_list = details.split("\n")
            if str(ph) in str(yours.users_info_list):
                if str(password) in str(yours.users_info_list):
                    yours.signedin = True

            if yours.signedin == True:
                print(f"{name} logged in")
                yours.availablemoney = int(yours.users_info_list[3])
                yours.name = name

            else:
                print("Wrong details")

    def add_cash(yours, amount):
        if amount > 0:
            yours.availablemoney += amount
            with open(f"{name}.txt","r") as f:
                details = f.read()
                yours.users_info_list = details.split("\n")

            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(yours.users_info_list[3]),str(yours.availablemoney)))

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")

    def Tranfer_cash(yours, amount , name ,ph):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            yours.users_info_list = details.split("\n")
            if str(ph) in yours.users_info_list:
                yours.TranferCash = True


        if yours.TranferCash == True:
            total_cash = int(yours.users_info_list[3]) + amount
            left_cash = yours.availablemoney - amount
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(yours.users_info_list[3]),str(total_cash)))

            with open(f"{yours.name}.txt","r") as f:
                details_2 = f.read()
                yours.users_info_list = details_2.split("\n")

            with open(f"{yours.name}.txt","w") as f:
                f.write(details_2.replace(str(yours.users_info_list[3]),str(left_cash)))

            print("Amount Transfered Successfully to",name,"-",ph)
            print("Balacne left =",left_cash)
            yours.availablemoney = left_cash

    def password_change(yours, password):
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
        else:
            with open(f"{yours.name}.txt","r") as f:
                details = f.read()
                yours.users_info_list = details.split("\n")

            with open(f"{yours.name}.txt","w") as f:
                f.write(details.replace(str(yours.users_info_list[2]),str(password)))
            print("new Password set up successfully")

    def ph_change(yours , ph):
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
        else:
            with open(f"{yours.name}.txt","r") as f:
                details = f.read()
                yours.users_info_list = details.split("\n")

            with open(f"{yours.name}.txt","w") as f:
                f.write(details.replace(str(yours.users_info_list[1]),str(ph)))
            print("new Phone number set up successfully")



if __name__ == "__main__":
    Transactionsapp_object = Transactionsapp()
    print("Welcome to my Transactionsapp")
    print("1.Login")
    print("2.Creata a new Account")
    user = int(input("Make decision: "))

    if user == 1:
        print("Logging in")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Transactionsapp_object.login(name, ph, password)
        while True:
            if Transactionsapp_object.signedin:
                print("1.Add amount")
                print("2.Check Balcane")
                print("3.Tranfer amount")
                print("4.Edit profile")
                print("5.Logout")
                login_user = int(input())
                if login_user == 1:
                    print("Balance =",Transactionsapp_object.availablemoney)
                    amount = int(input("Enter amount: "))
                    Transactionsapp_object.add_cash(amount)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 2:
                    print("Balacne =",Transactionsapp_object.availablemoney)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 3:
                    print("Balance =",Transactionsapp_object.availablemoney)
                    amount = int(input("Enter amount: "))
                    if amount >= 0 and amount <= Transactionsapp_object.availablemoney:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Transactionsapp_object.Tranfer_cash(amount,name,ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0 :
                        print("Enter please correct value of amount")

                    elif amount > Transactionsapp_object.availablemoney:
                        print("Not enough balance")

                elif login_user == 4:
                    print("1.Password change")
                    print("2.Phone Number change")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("Enter new Password: ")
                        Transactionsapp_object.password_change(new_passwrod)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new Phone Number: "))
                        Transactionsapp_object.ph_change(new_ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif login_user == 5:
                    break


    if user == 2:
        print("Creating a new  Account")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Transactionsapp_o2bject.register(name, ph, password)
