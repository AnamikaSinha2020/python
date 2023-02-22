# program to slice the email adress

email= input("Enter your email address: ")
(usename,domain) = email.split("@")
(domain,extnsion)= domain.split(".")
print("Username :", usename)
print("Domain :", domain)
print("Extension : ", extnsion)