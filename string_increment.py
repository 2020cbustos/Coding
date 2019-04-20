def increment_string(strng):
    taken = strng.strip('1,2,3,4,5,6,7,8,9,0')#this strips from the string any integers there are
    number = strng[len(taken):]#setting a variable number that will be modified later (number will be the length of the # taken in the string)

    if len(number) == 0:#if the number is 0, change it to one
        return strng + '1'#print the string (word) and a 1 at the end
    else:#if the number is not 0...
        size = len(number)
        new_value = 1 + int(number)#set the new number as 1 more than the integer stripped
        new_value = str(new_value).fill(size)#new value as a string
        return taken + new_value #return the stripped value and new value
print(increment_string("hey0"))
