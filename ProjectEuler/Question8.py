def findProduct(numbers):
   product = 1
   for number in numbers:
      product = product * number
   return product

data = open("data.txt", "r")
input = ""

for line in data.readlines():
    input+=line

charlist = list(input)
numberlist = []
for element in charlist:
    if element.isdigit():
      numberlist.append(int(element))

productlist = []
length = len(numberlist)
count = 0
STEP= 13

while (count < length):
   searchlist = numberlist[count:count+STEP]
   productlist.append(findProduct(searchlist))
   count+=1

#We check for the largest number
largest = max(productlist)
print("The largest ", STEP, " point product is ", largest)
