'''
For recursion first write the step what we know
i.e number[n] = number[n-2] + number[n-1]
return it.
'''

# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 10
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))
'''
fibonachi  0 1 2 3
o/p        0 1 1 2
'''
def fibonachi(number):
    if number <= 1:
        return number
    else:
        return fibonachi(number-2) + fibonachi(number-1)
        #for 2 => fibonachi(0) + fibonachi(1)
        #for 3 => fibonachi(1) + fibonachi(2)

for i in range(11):
    print(fibonachi(i))