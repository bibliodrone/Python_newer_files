import re

find=re.compile(".*ADD-FIELD.*")
filt=re.compile("(^[0-9])(\s+)(\w.+)(\s+)(\S)(\s$)\1\3\5")
fick=re.compile("^[0-9].*$")
comme=re.compile("(^)(.*)(,{1})/3")

with open('fix_txt/generic.ebook.fixstripped.txt', 'rt') as f:
    for i in range(0,101):
        if i%10 == 0:
           print("*", end="")
        else:
           print("-", end="")

    print()
    
    for line in f:
        if re.match(fick,line):
            #line=(re.sub("\s{2,}", " ", line))
            #print(line[0:5] + " " +line[27:36]+" "+line[58:68])
            line=(re.sub(comme, " wif ", line))
            print(line)
f.close()
