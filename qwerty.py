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

def encrypt (text, encryptKey):
  region_one = list("qwertyuiop")
  region_two = list("asdfghjkl")
  region_three = list("zxcvbnm,.")
  region_four = list("QWERTYUIOP")
  region_five = list("ASDFGHJKL")
  region_six = list("ZXCVBNM<>")
  encryptKey = list(str(encryptKey))
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
              new = (region_one.index(x) + shift_one) % 10
              new_array_two.append(region_one[new])
          elif x in region_two:
              new = (region_two.index(x) + shift_two) % 9
              new_array_two.append(region_two[new])
          elif x in region_three:
              new = (region_three.index(x) + shift_three) % 9
              new_array_two.append(region_three[new])
          elif x in region_four:
              new = (region_four.index(x) + shift_one) % 10
              new_array_two.append(region_four[new])
          elif x in region_five:
              new = (region_five.index(x) + shift_two) % 9
              new_array_two.append(region_five[new])
          elif x in region_six:
              new = (region_six.index(x) + shift_three) % 9
              new_array_two.append(region_six[new])
          elif x in region_one or region_two or region_three or region_four or region_five or region_six:
              new_array_two.append(x)
          else:
              new_array_two.append(x)
      return "".join(new_array_two)






def decrypt (text, encryptKey):
  region_one = list("qwertyuiop")
  region_two = list("asdfghjkl")
  region_three = list("zxcvbnm,.")
  region_four = list("QWERTYUIOP")
  region_five = list("ASDFGHJKL")
  region_six = list("ZXCVBNM<>")
  encryptKey = list(str(encryptKey))
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
              new = (region_one.index(x) - shift_one) % 10
              new_array_two.append(region_one[new])
          elif x in region_two:
              new = (region_two.index(x) - shift_two) % 9
              new_array_two.append(region_two[new])
          elif x in region_three:
              new = (region_three.index(x) - shift_three) % 9
              new_array_two.append(region_three[new])
          elif x in region_four:
              new = (region_four.index(x) - shift_one) % 10
              new_array_two.append(region_four[new])
          elif x in region_five:
              new = (region_five.index(x) - shift_two) % 9
              new_array_two.append(region_five[new])
          elif x in region_six:
              new = (region_six.index(x) - shift_three) % 9
              new_array_two.append(region_six[new])
          else:
              new_array_two.append(x)
      return "".join(new_array_two)

#LOGIC

#take in encryptKey and string
#iterate through individual letters of the text
#6 IF LOOPS for each different array
  #if letter is in array 1
    #get index value of letter
    #add shift to index
    #take new index with length of array
    #put letter in new array
    #if the text is done...
       #end
    #else:
       #go to the next letter

#CODE w/ COMMENNTS
