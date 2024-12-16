z = """
        Welcome to The Puchik App version 1.0
        Please select which operation you will like to proceed with
    """
print (z)

def buy_data(b):
    x = b
    return x
#a method named buy data

def phone_number(a):
    x = a
    return x
#a method named phone number


while True:
#This makes the operation run over and over again

    print(str("Possible operations are : \n phone number \n buy data \n stop"))  

    operations=str(input("Enter operation : "))

    if operations.lower() == "stop":
        break        
    if operations.lower() == 'phone number':
        x = str(input("Enter phone number : "))
        if len(x) == 11:
            first_three = x[0:3]
            first_four = x[0:4]
            first_five = x[0:5]
            if operations == "phone number":
                if first_three == "073" or first_four == "0803" or first_four == "0806"or first_four == "0703" or first_four == "0706" or first_four == "0813" or first_four == "0816" or first_four == "0810" or first_three == "083" or first_four == "0814" or first_four == "0903" or first_four == "0906" or first_four == "0913" or first_four == "0916" or first_five == "07025" or first_five == "07026" or first_four == "0704" or first_four == "0702":
                    print("MTN sim")
                elif first_four == "0802" or first_four == "0808" or first_four == "0708" or first_four == "0812" or first_four == "0701" or first_four == "0902" or first_four == "0901" or first_four == "0904" or first_four == "0907" or first_four == "0912":
                    print("Airtel sim")
                elif first_four =="0905" or first_four == "0805" or first_four == "0807" or first_four == "0705" or first_four == "0815" or first_four == "0811" or first_four == "0915": 
                    print("Glo sim")
                elif first_four =="0909" or first_four == "0908" or first_four == "0818" or first_four == "0809" or first_four == "0817":
                    print("9Mobile sim")
                else:
                    print("Invalid digits")
        else: 
            print("Invalid phone number \nCheck input and try again")
            
    if operations.lower() == "buy data":
        d = """
            Available balance is $1000
            Dial sim code to buy data
            Hint: MTN - *131#
                  Airtel - *141#
                  Glo - *777#
                  9 mobile - *917#
            All other sims are not accepted
            Enter anything to restart.
            """
        print (d)
        q = str(input("Enter sim code : "))
        while True:
            if len(q) == 5:
                allowed = q[0:5]
                if allowed == "*131#"or allowed == "*141#"or allowed == "*777#" or allowed == "*917#":
                    print("1. Daily"
                            "\n2. Weekly"
                            "\n3. Change operation"
                            )
                    h = str(input("Enter plan number : "))
                    if h == "1":
                        print("1. 50$ for 40mb 1 day"
                              "\n2. 100$ for 100mb 1 day"
                              "\n3. 300$ for 1gb 1 day"
                              "\n4. return to main menu"
                              )
                        e = str(input("Enter option : "))
                        if len(e) == 1:
                            okay = e[0:1]
                            
                            if okay == "1":
                                print ("1. one_off_purchase"
                                       "\n2. auto_renewal"
                                       "\n Enter any other number to cancel")
                                c = str(input("Enter option : "))
                                if c == "1" or c == "2":
                                    print ("Successful")
                                    break
                            if okay == "2":
                                print ("1. one_off_purchase"
                                       "\n2. auto_renewal"
                                       "\n Enter any other number to cancel")
                                c = str(input("Enter option : "))
                                if c == "1" or c == "2":
                                    print ("Successful")
                                    break
                            if okay == "3":
                                print ("1. one_off_purchase"
                                       "\n2. auto_renewal"
                                       "\n Enter any other number to cancel")
                                c = str(input("Enter option : "))
                                if c == "1" or c == "2":
                                    print ("Successful")
                                    break
                        else:
                            print("Invalid option")
                            break
                    elif h == "2":
                        print("1. 200$ for 200mb 3 days"
                                "\n2. 500$ for 1.2gb 2 days"
                                "\n3. 300$ for 350mb 7days"
                                "\n4. enter 4 to go back"
                                )
                        e = str(input("Enter option : "))
                        if len(e) == 1:
                            okay = e[0:1]
                            if okay == "1":
                                print ("1. one_off_purchase"
                                       "\n2. auto_renewal"
                                       "\n Enter any other number to cancel")
                                c = str(input("Enter option : "))
                                if c == "1" or c == "2":
                                    print ("Successful")
                                    break
                        
                            if okay == "2":
                                print ("1. one_off_purchase"
                                       "\n2. auto_renewal"
                                       "\n Enter any other number to cancel")
                                c = str(input("Enter option : "))
                                if c == "1" or c == "2":
                                    print ("Successful")
                                    break
                            if okay == "3":
                                print ("1. one_off_purchase"
                                       "\n2. auto_renewal"
                                       "\n Enter any other number to cancel")
                                c = str(input("Enter option : "))
                                if c == "1" or c == "2":
                                    print ("Successful")
                                    break
                        else:
                            print("Invalid option")
                            break
                    elif h == "3":
                        break
                    else:
                        print("wrong selection")
                else:
                    print ("I do not know this sim code")
                    break
            else:
                print ("I do not know this sim code")
                break
            
