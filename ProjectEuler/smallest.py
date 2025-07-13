numbers = [i for i in range(1,21)]
print(numbers)

smallest = 1
found = False

while not found:
    smallest+=1
    for number in numbers:
      if smallest%number !=0:
        break
      elif (number == numbers[-1]) and smallest%number ==0:
         found = True
    

print("The smallest positive integer evenly divisible by 1-20 is ", smallest)