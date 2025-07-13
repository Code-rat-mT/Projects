#To find the largest palindrome for a product of two 3 digit numbers
number_word = ""
largest = 0
for i in range(1,999):
    for j in range(1,999):
        product = i*j
        number_word = str(product)
        reversed_number= number_word[::-1]
        if (number_word == reversed_number):
            if product>largest:
                largest = product


print("The largest palindrome is ", largest)



