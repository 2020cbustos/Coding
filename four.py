#encrypt a message with a shift in letters. Takes into accounts letters 1 to 26.

#LOGIC of INCRIPTION

#main idea: loop through a string and shift 
#create hash with each letter and their numeric value (of the alphabet) 
#create function that takes in string and returns the same string with shift 
#create empty array (for output) 
#get value from key in hash 
#implement shifting 
#use .join to turn array into string 
#add to array
#return encrypted message with shift 

#LOGIC of DECRIPTION 
#take in word with shift 
#reverse shift 
#return initial value (output) 

#call a function with string (message) and shift (input of how many letters to shift) 
def encrypt(string,shift):
   #create hash of letters and their numeric value 
   letters_hash = {
   'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
   'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15',
   'p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22',
   'w':'23','x':'24','y':'25','z':'26'
   }
   #empty array where output will go 
   answer = []
   nums = []
   #take string into list 
   string = list(string)
   for x in string:
       #loop through the hash 
       for key, value in letters_hash.items():
           num = letters_hash[x]
           num = int(num)
           shift = int(shift)
           #define variable shifting 
           shifting = num + shift
       #add the shifting 
       nums.append(shifting)
   #starting the second array 
   number_one = [ str(item) for item in nums]
   letters_hash_1 = {y:x for x,y in letters_hash.items()}
   #loop over the second hash 
   for n in number_one:
       for key, value in letters_hash_1.items():
           alpha = letters_hash_1[n]
       #add with .append
       answer.append(alpha)
       #join 
       output = " ".join(answer)
   return output
#these are the user inputs 
string = input()
string = str(string)
shift = input()
shift = str(shift)
#call the function and print
print(encrypt(string, shift))
