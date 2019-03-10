def findMaxIndex(items):
    start = 0 
    if (len(items) <= 1):
        return 0
    ans = 0
    for index1,item1 in enumerate(items):
        for index2,item2 in enumerate(items[index1+1:]):
            if (item1 <= item2):
                ans = max(ans, index2+1)

    return ans

print(findMaxIndex([34,8,10,3,2,80,30,33,1]))


        

