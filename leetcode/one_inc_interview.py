arr = ["8,a,b,32,a", "3,c,d,e,11", "9,e,f,q,12", "1,g,2,e,x", "3,a,g,t,2", "2,i,j,o,6", "8,a,b,32,a"]

# remove duplicated tuples, sort by the first column, do upper-case for all letter columns
'''  
brute force iterate nested for loops
second thought 
third thought: move through the array add to a hashmap 
append each element to hash map and count as value if there's any values greater than zero, 
they are duplicates and we'll remove them
'''
def refine(src):
    input_as_set = set()
    for each in src:
        input_as_set.add(each)
    output = []
    for each in input_as_set:
        output.append(each.upper())
    output.sort()
    return output
    
result = refine(arr)
print(result)
