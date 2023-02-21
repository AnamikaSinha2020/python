# emailvalidation program by string

email= input("Enter your email : ")
k=0
j=0
d=0
# email must have min 6 char a@a.co
if len(email)>=6:
    if email[0].isalpha(): # first charecter should be alphabet
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."): # . will be at -4 or -3 position either one
                for i in email:
                    if i== i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                     print("wrong email")
                else:
                    print("right email")
            else:
                print("wrong position of .")
        else:
            print("Either none or more that one @ in mail")
    else:
        print("First character is not a alphabet")
else:
    print("length is too short to be an email")