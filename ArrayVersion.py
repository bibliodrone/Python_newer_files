import re

a=[]
b=[]
c=[]
d=[]
e=[a, b, c, d]
dPrime=""

#g=open('sliced.txt', 'w')
with open('cleansprgr.txt', 'rt') as f:

    for line in f:
        a.append(str(line[2:5].rstrip()))
        b.append(str(line[13:16].rstrip()))
        c.append(str.title((line[27:57].rstrip())))       
        d.append(str(line[58:100].rstrip()))

leng = str(len(e))
print("Length: " + leng)
print(len(a))

count = (len(a))
index = (len(a))
while (count > 0):
    print (a[(index-count)]+ " ", end='')
    print (b[(index-count)]+ " ", end='')
    print (c[(index-count)]+ " ", end='')
    print (d[(index-count)]) 
    count -= 1

for i,value in enumerate(d):
    d[i] = value.partition(',')
    d[i] = d[i].format()
    
for i, value in enumerate(c):
    matchObj=re.match("Replace|Change", c[i])
    if matchObj:
 #       d[i]=(matchObj, "with ")
    print(c[i] + d[i])
 
##    value = value.partition(',')
##    print (value, end='')
##    print (d)
##    s = re.search (".+,\s*", value)
##    if s:
##        print (s.group())

#        d = d.replace("#", "*any* ")
#        if d.endswith(","):
#            d = (d + "with blank")
                  
#        g.write("Field " + a)
#        g.write(" " + b)
#        g.write(" " + c.title())
#        g.write(" " + d + "\n")

#g.close()
