from sys import argv

script, filename =argv

txt= open(filename)

print(f" here is your file {filename}: ")
print(txt.read())

print("Type the filename adain")
file_again=input(">")

txt_again=open(file_again)
print(txt_again.read())