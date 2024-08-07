arr = ["8,a,b,32,a", "3,c,d,e,11", "9,e,f,q,12", "1,g,2,e,x", "3,a,g,t,2", "2,i,j,o,6", "8,a,b,32,a"]

# remove duplicated tuples, sort by the first column, do upper-case for all letter columns
'''  
brute force iterate nested for loops
second thought 
third thought: move through the array add to a hashmap 
append each element to hash map and count as value if there's any values greater than zero, 
they are duplicates and we'll remove them
'''
def refine(src: list[str]) -> list[str]:
    input_as_set: set[str] = set()
    for each in src:
        input_as_set.add(each)
    output: list[str] = []
    for each in input_as_set:
        output.append(each.upper())
    output.sort()
    return output

def refine_fun(src: list[str]) -> list[str]:
    input_as_map: dict[str, int] = {}
    for each in src:
        input_as_map[each.upper()] = 1
    return list(sorted(input_as_map.keys()))
    
    
result = refine(arr)
print(result)
print(refine_fun(arr))

# FINALLY GOT THE FUN ONE WORKING PROPERLY WITH MINIMAL SPACE USED
'''
def refine_fun(src: list[str]) -> list[str]:
    input_as_map: dict[str, int] = {}
    for each in src:
        input_as_map[each.upper()] = 1
    return list(sorted(input_as_map.keys()))
'''
# pasting here in case i decide to change it in the future :)
