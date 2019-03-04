#make a library/hash with all of the colors and their value
library = {"black": 0,
"brown": 1,
"red": 2,
"orange": 3,
"yellow": 4,
"green": 5,
"blue": 6,
"violet": 7,
"gray": 8,
"white": 9,
"gold": 5,
"silver": 10}

#call the function
def decode_resistor_colors(bands):
  #use the split function to split the input(#) given
  bands = bands.split()
  #set variable ohms to values
  ohms = (10 * library[bands[0]] + library[bands[1]]) * 10 ** library[bands[2]]
  #if ohms is greater than 1000000
  if ohms > 1000000: 
      #the ohms value is divided by 1000000 w/ an "M" for unit 
      ohms = str(ohms/1000000) + "M"
  #if ohms is greater than 1000
  elif ohms > 999:
      #the ohms value is divided by 1000 w/ a "k" for unit 
      ohms = str(ohms/1000) + "k"
  #else ohms is smaller than 1000
  else:
      #return strings of ohms (first color, second color, third color + gold)
return 

