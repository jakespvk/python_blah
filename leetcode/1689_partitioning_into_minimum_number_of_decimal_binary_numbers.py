#example_input
n = "32"

def minPartitions(n: str):
    highest = len(n) * "1"
    index_of_zero = n.index("0")
    if (index_of_zero != -1):
        highest = ""
        for i in range(len(n)):
            if (i == index_of_zero):
                highest = highest + "0"
            else:
                highest = highest + 1

    print(highest)


def minPartitions_iter3(n: str, highest: str = ""):
    count = 0
    n = str(int(n) - int(highest))
    count += 1
    if (n > highest):
        n = str(int(n) - int(highest))
        count += 1
    else:
        highest = "10"
    if (n > highest):
        n = str(int(n) - int(highest))
        count += 1
    else:
        highest = "1"
    if (n > highest):
        n = str(int(n) - int(highest))
        count += 1
    return count
    

def minPartitions_iter2(n: str, count: int, highest: str = "11") -> int:
    while (int(n) > 0):
        count += 1
        print(str(int(n) - int(highest)))
        n = str(int(n) - int(highest))
    highest = 0
    if highest[len(highest) - 1] == "0":
        highest = highest[1:len(highest)]
    else:
        highest = highest[0:len(highest) - 2] + "0"

    return minPartitions(n, count, highest)


def minPartitions_iter1(n : str):
    '''
        if we split 32 into 30 and 2, dumb approach would be 10 + 10 + 10 + 1 + 1 so how do we realize
        (obviously realize in our program) that instead of 10 we can do 11
        lets start doing it with 10s and 1s and see what happens
    ''' 
    elevens = 0
    tens = 0
    ones = 0
    ones = int(n)
    if ones > 10:
        tens = ones // 10
        ones = ones - (tens * 10)
    while ones != 0:
        elevens += 1
        tens -= 1
        ones -= 1
        
    print(elevens, tens, ones)

print(minPartitions(n))
