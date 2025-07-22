data = open("data18.txt", "r")
input = []
for line in data.readlines():
    input.append(line.strip().split())


numbers= []
numberInput=[]
for element in input:
    if element:
        for elem in element:
            numbers.append(int(elem))
        numberInput.append(numbers)
    numbers=[]

sum = 0
print(numberInput)
#going in each row, I only add the maximum number to the sum
pivot = numberInput[0][0]
total = pivot
col = 0

for row in range(0,len(numberInput)):
        left = numberInput[row][col] if col < len(numberInput[row]) else float('-inf')
        right = numberInput[row][col + 1] if col + 1 < len(numberInput[row]) else float('-inf')

        if right > left:
            col += 1
            total += right
        else:
            total += left

        
    

print("The maximum sum is ", total)