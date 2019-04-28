def bound_check(number_in_rgb):
    #this first function checks the bounds
    #if the number is smaller than 0 it makes it 0 (because it is closest)
    if number_in_rgb < 0:
        return 0
    #if the number is greater than 255 it makes it 255 (because it is closest)
    if number_in_rgb > 255:
        return 255
    else: #otherwise it returns the number inputed
        return number_in_rgb

def rgb(r, g, b): #this creates the function
    return "{:02X}{:02X}{:02X}".format(bound_check(r), bound_check(g), bound_check(b))
    #already built-in method that formats three numbers as 2 digit hexadecimal strings with leading 0s
    #it relates back to first function and the bounds returned (0,255 or the number inputed)


#LOGIC:
#rgb(220,20,60)
#FOR FIRST VALUE
#1. take the first value (220) and divide it by 16
#2. 220/16 = 13.75
#3. this means the 1st digit is 13 (or D)
#4. the remainder is 0.75
#5. multiply 0.75 by 16
#6. 0.75*16 = 12
#7. second digit is then 12 (or C)
#8. as of now, we have DC

#FOR SECOND VALUE
#1. take second number (20) and divide by 16
#2. 20/16 = 1.25
#3. the third digit of the code is 1
#4. take remained (0.25) and times by 16
#5.0.25* 16 = 4
#6. the 4th digit is 4

#FOR THIRD VALUE
#1. take third number and divide by 16
#2. 60/16 = 3.75
#3. fifth digit is 3
#4.take remainder (0.75) and multiply by 16
#5. 0.75*16 = 12
#6. sixth digit is 12 (or C)
