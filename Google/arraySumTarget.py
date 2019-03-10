def retArrayWithSum(items, sum):
    tmp = 0
    ans = ()
    start = 0
    if (len(items) == 0):
        return ans
    for index,item1 in enumerate(items):
        tmp += item1
        while (tmp > sum and start < len(items)-1):
            tmp -= items[start]
            start += 1
        
            
        if (tmp == sum):
            return (start+1, index+1)
        

    return ()

print(retArrayWithSum([1,2,2,4], 10))

