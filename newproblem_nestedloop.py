rows=int(input("enter the number of rows:")) #another program practice for nested loop
col=int(input("enter the no of col:"))
sym=input("enter the symbol:")
for x in range(rows):
    for y in range(col):
        print(sym,end="")#end="" iska mtlb ha jo inner loop ha wo 1 hi line ma answer dy by default to python ma esa hota print(y,end="\n") means new line
    print()#this is used for new line jab 1 value outer loop ki complete aur next value new line ma ho
