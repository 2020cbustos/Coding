#LOGIC

#take in key and string
#iterate through individual letters of the word
#6 IF LOOPS for each different array
  #if letter is in array 1
    #get index value of letter
    #add shift to index
    #take new index with length of array
    #put letter in new array
    #if the word is done...
       #end
    #else:
       #go to the next letter

def encrypt (text, encryptKey): #create a function
  #first region of the keyboard
  region_one = ("qwertyuiop") 
  #second region of keyboard
  region_two = ("asdfghjkl") 
  #third region of keyboard
  region_three = ("zxcvbnm,.")
  #first region of keyboard uppercase
  region_four = ("QWERTYUIOP") 
  #second region of keyboard uppercase
  region_five = ("ASDFGHJKL")
  #third region of keyboard
  region_six = ("ZXCVBNM<>") 
  new_array = [] #create the first empty array 
  #set variable key to a string that will be given 
  encryptKey = str(encryptKey)
  #use a for loop for w in key 
  for w in encryptKey:
      w = int(w)
      new_array.append(w)
      #add the integers that are being looped through to the empty array 
  #if statement for 1 and 2 as the length of the array 
  if len(new_array) == 1:
    new_array.append(0)
  if len(new_array) == 2:
    new_array.append(0)
    #create the second empty array where the final values will go 
  new_array_two = []
  text = list(text)
  #set the index values for each shift 
  shift_one = new_array[0]
  shift_two = new_array [1]
  shift_three = new_array[2]
  #nested for loop 
  for y in region_one or region_two or region_three or region_four or region_five or region_six:
      for x in text:
          #six different if statements for each different array
          #the index value is added to the shift and all divided by the length of the array (10 or 9)
          if x in region_one:
              #new value of word will be equal to ... 
              new = (region_one.index(x) + shift_one) % len(region_one)
              #add value to the array 
              new_array_two.append(region_one[new])
          elif x in region_two:
              new = (region_two.index(x) + shift_two) % len(region_two)
              #add value to the array 
              new_array_two.append(region_two[new])
          elif x in region_three:
              new = (region_three.index(x) + shift_three) % len(region_three)
              #add value to the array 
              new_array_two.append(region_three[new])
          elif x in region_four:
              new = (region_four.index(x) + shift_one) % len(region_four)
              new_array_two.append(region_four[new])
          elif x in region_five:
              new = (region_five.index(x) + shift_two) % len(region_five)
              new_array_two.append(region_five[new])
          elif x in region_six:
              new = (region_six.index(x) + shift_three) % len(region_six)
              new_array_two.append(region_six[new])
          elif x in region_one or region_two or region_three or region_four or region_five or region_six:
              new_array_two.append(x)
          else:
              new_array_two.append(x)
              #join it all together 
      return "".join(new_array_two)


    #the logic of this is the same thing except it is minus the shift rather than adding the shift 

def decrypt (text, encryptKey):
  region_one = ("qwertyuiop")
  region_two = ("asdfghjkl")
  region_three = ("zxcvbnm,.")
  region_four = ("QWERTYUIOP")
  region_five = ("ASDFGHJKL")
  region_six = ("ZXCVBNM<>")
  encryptKey = str(encryptKey)
  new_array = []
  for w in encryptKey:
      w = int(w)
      new_array.append(w)
  if len(new_array) == 1:
    new_array.append(0)
  if len(new_array) == 2:
    new_array.append(0)
  new_array_two = []
  text = list(text)
  shift_one = new_array[0]
  shift_two = new_array [1]
  shift_three = new_array[2]
  for y in region_one or region_two or region_three or region_four or region_five or region_six:
      for x in text:
          if x in region_one:
              new = (region_one.index(x) - shift_one) % len(region_one)
              new_array_two.append(region_one[new])
          elif x in region_two:
              new = (region_two.index(x) - shift_two) % len(region_two)
              new_array_two.append(region_two[new])
          elif x in region_three:
              new = (region_three.index(x) - shift_three) % len(region_three)
              new_array_two.append(region_three[new])
          elif x in region_four:
              new = (region_four.index(x) - shift_one) % len(region_four)
              new_array_two.append(region_four[new])
          elif x in region_five:
              new = (region_five.index(x) - shift_two) % len(region_five)
              new_array_two.append(region_five[new])
          elif x in region_six:
              new = (region_six.index(x) - shift_three) % len(region_six)
              new_array_two.append(region_six[new])
          else:
              new_array_two.append(x)
      return "".join(new_array_two)
