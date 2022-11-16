'''You are given a positive integer N . Print a numerical triangle of height  N-1 like the one below:
1
22
333
4444
55555'''

print("Enter the value of N")
N=int(input())
for i in range(1,N):

   print(i*(((10**i)-1)//9))
