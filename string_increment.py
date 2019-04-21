#the string.strip([remove]) is a built-in python function that removes all the leading and trailing spaces from a string.
#what goes inside the "remove" is what is taken out, and for this problem, it is the integers from 0 to 9 that are removed 

def increment_string(strng):
    taken = strng.strip('0,1,2,3,4,5,6,7,8,9')#this strips from the string any integers there are from 0 to 9 
    number = strng[len(taken):]
    #setting a variable 'number' that will be modified later. number is the length of the string (digit) taken
    if len(number) == 0:#if the length of the number is 0, change it to one
        return strng + '1'#print the string (word) and a 1 at the end
    else:#if the length of the number is not 0...
        size = len(number) #the size variable is the length of the number (how many digits)
        new_value = 1 + int(number)#set the new number as 1 more than the integer stripped
        new_value = str(new_value).fill(size)#new value as a string and fill it in to the original strng given
        return taken + new_value #return the stripped value and new value
    
    #THE OVERALL LOGIC is to strip the digits at the end of the string and add one more to whatever the length of the 
    #digit is in order to increase the value 
    
#print(increment_string("hey0"))
