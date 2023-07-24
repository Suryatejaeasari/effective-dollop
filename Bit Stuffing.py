l = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
ans = []
c =0
i =0
while (i<len(l)):
    if l[i] == 1:
        c+=1

    else:
        c=0
    ans.append(l[i])
    if c==5:
        c=0
        ans.append(0)
    i+=1
print("After Stuffing:", ans)
j =0
c1=0
while(j<len(ans)):
    if ans[j] == 1:
        c1+=1
    else:
        c1=0
    if c1 == 5:
        c1=0
        ans.pop(j+1)
    j+=1
print("After Destuffing:",ans)
