# return a list of fibonacci numbers
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
    l = []

    print("Fibonacci sequence:")
    for i in range(nterms):

       l.append(recur_fibo(i))
print(l)