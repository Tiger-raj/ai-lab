#function to print nth fibonacci no.

#function definition to calculate nth fibonacci no.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

#user input for n
n=int(input("Enter n"))
# print fibonacci series till nth term
for i in range(n):
    print(fibonacci(i),end=" ")
