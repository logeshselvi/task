def choices():
    print("Please choose what you would like to do.")
    choice = int(input("For Sigining Up Type 1 and For Signing in Type 2: "))
    if choice == 1:
       return register()
    elif choice == 2:
       return checkdetails()
    else:
       raise TypeError

def register():
    f = open("U_S.txt" ,'r')
    un = input("create your user name:")
    u=[]
    for line in f:
        x=line.split(',')
        u.append(x[0])
    if un in u:
        print("try with another name")
        register()
    elif un.count('@') !=1 and un .count('.')!=1:
        print('invalid format try again')
        register()
    elif ((un.index('@')) -(un.index('.')))== 1:
        print('invalid format try again')
        register()
    elif un[0] in range(0,9):
        print('first letter of your username cannot be number')
        register()
    elif ( un[0] == '!' or un[0] == '@' or un[0] == '#' or un[0] == '$' or un[0] == '%'  or un[0] == '&' or un[0] == '*' or   un[0] == '?'  or un[0] == '+'):
        print('first letter of your username cannot be special character')
        register()
    else:
        print('username is created')
    pw = input("Create your password with atleast one capital letter one integer and one special character: ")
    e = False

    if len(pw) < 5 and len(pw) > 16:
        print("Password length should be atlest between 5 to 16 characters ,Please Try Again")
        register()

    if len(pw) > 5 and len(pw) < 16:
        a,b,c,d,e = 0,0,0,0,0
        for i in pw:
              if i.isdigit():
                  a += 1
              if i.islower():
                  b += 1
              if i.isupper():
                  c += 1
              if ( i == '!' or i == '@' or i == '#' or i == '$' or i == '%'  or i == '&' or i == '*' or   i == '?'  or i == '+'):
                  d += 1
              if (a >= 1 and b >= 1 and c >= 1 and d >= 1 and a + b + c + d == len(pw) ):
                  e =True


        if e :
              p = input( "confrim password:" )
              while(p != pw):
                  print("password does not match")
                  p = input('try again:')

        else:
                print("Try again")
                register()


        file = open("U_S.txt", "a")
        file.write(un + "," + pw + "\n")
        file.close()
        print("Account created successfully")


def checkdetails():
    us = input("Enter your username to login: ")
    X = us.strip()
    f = open("U_S.txt", "r")
    u = []
    for line in f:
        x = line.split(",")
        u.append(x[0])

    if X in u:
        Y = input("Please Enter your password: ")
        Y = Y.strip()
        file1 = open("U_S.txt", "r").readlines()
        for x in file1:
            x = x.strip()
            info = x.split(",")
            if X == info[0] and Y == info[1]:
                print(f"Loggin successfully, Welcome {X}")
                exit()



            else:
                F = input("Forgot Password [y/n] : ")

                if F == "N":
                    print("try")
                    login()

                if F == "Y":
                    pw = input(
                        "Create your new password with atleast one capital letter one integer and one special character: ")
                    e = False

                    if len(pw) < 5 and len(pw) > 16:
                        print("Create Password with length between 5 an 16, Try Again")
                        register()

                    if len(pw) > 5 and len(pw) < 16:

                        a, b, c, d = 0, 0, 0, 0
                        for i in pw:
                            if i.isdigit():
                                a += 1
                            if i.islower():
                                b += 1
                            if i.isupper():
                                c += 1
                            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                                d += 1
                            if (a >= 1 and b >= 1 and c >= 1 and d >= 1 and a + b + c + d == len(pw)):
                                e = True

                        if e:
                            p = input("Confirm Password: ")
                            while (p != pw):
                                print("Password not match, Try Again")
                                p = input("Try Again: ")

                        else:
                            print("Sorry,Try again to login")
                            login()

                        file = open("U_S.txt", "w")
                        file.write(X + "," + pw + "\n")
                        file.close()

    else:
        print("Unregister user you need to register first")
        register()


print(choices())