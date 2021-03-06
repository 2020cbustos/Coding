# task: Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements
# https://www.codewars.com/kata/54e6533c92449cc251001667/

#Present Wed Feb 20th with Ishani 

def unique_in_order(iterable):
    result = [] # empty list for the result
    last = None #

    for item in iterable: # going over the array
        if item == last: # if the value is equal to the previous term
            continue    #we do nothing
        else:
            #if current item is different then previous one
            result.append(item) # add the item into results
            last = item #and set previous item to current one

    return result

