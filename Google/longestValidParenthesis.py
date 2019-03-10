def retLongestValid(input):
    stack = []
    ans = 0 
    ret = 0 
    for char in input:
        if char in set('('):
            stack.append('(')
        elif char in set(')') and len(stack) == 0:
            ret = max(ret, ans)
            ans = 0
        else:
            ans += 2
            stack.pop(-1)
    
    return max(ret,ans)

print(retLongestValid('(())()()()'))