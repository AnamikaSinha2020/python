'''Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
'''


def sort(str):
    L = list(str)
    len(L)
    l_upper = []
    l_lower = []
    l_integer = []

    l_upper = [data for data in L if data.isupper()]
    l_lower = [data for data in L if data.islower()]
    l_integer = [data for data in L if data not in l_upper and data not in l_lower]

    l_upper.sort()
    l_lower.sort()
    l_integer.sort()
    print(l_upper)
    print(l_lower)
    leven = [num for num in l_integer if int(num) % 2 == 0]
    lodd = [num for num in l_integer if int(num) % 2 != 0]
    newl = l_lower + l_upper + lodd + leven
    news = "".join(newl)
    return news


print("storing sort the string")

print("Enter a alphanumeric string:")
str1 = input()
sorted_String=sort(str1)
print("Sorted String value: "+sorted_String)

