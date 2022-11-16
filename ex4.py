'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

entered_list = []
sorted_name = []
marks_list = []
print("enter number of student")
student = int(input())
for i in range(student):
    print("Enter name of student ")
    name = input()
    score = float(input())
    entered_list.append([name, score])
print(entered_list)
l1 = []
for i in range(student):
    marks_list.append(entered_list[i][1])
marks_list.sort()
print(marks_list)
for i in range(student):
    if entered_list[i][1] == marks_list[1]:
        sorted_name.append(entered_list[i][0])
        sorted_name.sort()
    else:
        pass

for i in sorted_name:
    print(i)
