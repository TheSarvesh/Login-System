class NewLogin:
    def check(self):
        c3=0
        print("1)Log In\t2)Sign In")
        choice=int(input("Enter your choice: "))
        # Few number of Usernames and their respective Passwords are provided for demostration.
        if (choice==1):
            #Login Username
            fo = open("Username", "r")
            file_contents = fo.read()
            user2 = input('Enter your Username: ')
            c = 0
            for i in file_contents.split('\n'):
                if user2 == i:
                    c = 1
            #Login Password
            for a in range(3):
                fo = open("Password", "r")
                file_contents = fo.read()
                user2 = input("Enter your Password: ")
                c1 = 0
                for i in file_contents.split('\n'):
                    if user2 == i:
                        c1 = 1

                if c1==1:
                        break
                else:
                    print("Incorrect Password!!!")
                    c3=c3+1
                fo.close()

            if c3==3:
                print("Incorrect Password has been entered repeatedly.\nA verification email will be sent")
            else:
                if(c>=1 and c1>=1):
                    print("Logging In.....")
                else:
                    print("Incorrect Username!!!")

        elif (choice==2):
            #Sign In Username
            fo = open("Username", "r")
            file_contents = fo.read()
            user2 = input("Enter your Username: ")
            c2 = 0
            for i in file_contents.split('\n'):
                if user2 == i:
                    c2 = 1
            if c2 == 1:
                print('Username already taken')
            else:
                Username = open("Username", "a")
                Username.write(f"{user2}\n")
                Username.close()
                # Sign In Password
                pass2 = input("Enter a Password: ")
                Password = open("Password", "a")
                Password.write(f"{pass2}\n")
                Password.close()


        else:
            print("Enter a valid Choice!!!")

login2=NewLogin()
login2.check()
