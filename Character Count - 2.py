n = int(input())
l = []
l1 = []
s=''
for i in range(n):
    x = input()
    l.append(x)
    l1.append(len(x)+1)
for i in range(n):
    s+=str(l1[i])+str(l[i])
print(s)
data = input(r'Enter \n')
i=0
while (i<len(data)):
    if data[i].isnumeric():
        length = int(data[i])
        start = i+1
        end = start + length
        print(data[start:end])
        i = end
    else:
        i+=1
