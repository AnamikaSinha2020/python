## progra to check some charecter in the url
url="https://www.samsclub.com/c/dining-ware-entertaining-ware/"
'''

Its a working code

if "*" in url:
   print("Start found")
else:
    print("* not found")'''

if url.find("*")!=-1:
    print("* found")

else:
    print("* not found")