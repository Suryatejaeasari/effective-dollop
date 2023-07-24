s = str(input())
l = len(s)
i = 0
ans = ''
print("Before Stuffing:",s)
while(i< l):
    if s[i] == 'f' and i+4 <= l:
        if s[i:i+4] == 'flag':
            ans += "esc "+s[i]
        else:
            ans+=s[i]
    elif s[i] == 'e' and i+3<=l:
        if s[i:i+3] == 'esc':
            ans+="esc "+s[i]
        else:
            ans+=s[i]
    else:
        ans+=s[i]
    i+=1
print("After stuffing: ", ans)
