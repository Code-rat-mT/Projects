first = 1 
second = 1

fib = [1,1] 


run = True
number = ''
while (run):
    next_fib = fib[-1] + fib[-2]
    fib.append(next_fib)
    number = str(next_fib)
    if len(number) >= 1000:
        break
length = len(fib)
print("The length is ", length)
    
