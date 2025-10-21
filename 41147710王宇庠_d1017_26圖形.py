iLevel= int(input())
iCount =int(0)
i2Level = iLevel-1
while (iCount < iLevel):#直線
    print("*")
    iCount += 1
print()
iCount =int(0)
while (iCount < iLevel):#橫線
    print("*", end="")
    iCount += 1
print()
print()
iCount =int(0)
while (iCount < iLevel):#直角三角
    n = iCount+1
    m = iLevel - iCount 
    print("*"*n+" "*(m*2)+"*"*n,"*"*m+" "*(n*2)+"*"*m)
    iCount += 1
print()
iCount =int(0)
aCount =int(0)
bCount =int(0)
#奇偶判定
if iLevel%2==0:
    inLevel = i2Level   
else:
    inLevel = iLevel
while (iCount < inLevel):#正三角+橫式正三角
    if(aCount < inLevel):
        n = aCount+1
        m = inLevel - aCount
        n2 = int(n/2)
        m2 = int((m+1)/2) 
        print(" "*m2+"*"*n+" "*m2," "*n2+"*"*m+" "*n2,end="  ")
        aCount += 2
    else:
        print(" "*(m2+n+m2)," "*(n2+m+n2),end="  ")
    n = bCount+1
    m = inLevel - bCount
    print("*"*n+" "*m," "*m+"*"*n)
    if(iCount<inLevel/2-1):
        bCount += 1
    else:    
        bCount -= 1
    iCount += 1
print()
iCount =int(0)
aCount =int(0)
bCount =int(0) 
while (iCount < iLevel*2-1):#正三角+1,#橫式正三角+1
    nA = aCount+1
    nB = bCount+1
    m = iLevel*2 - aCount-1
    mB = iLevel - bCount
    n2 = int(nA/2)
    m2 = int(m/2) 
    if iCount < iLevel:
        print(" "*m2+"*"*nA+" "*m2," "*n2+"*"*m," "*n2,end="  ")
    else:
        print(" "*(m2+nA+m2)," "*(n2+m+n2),end=" ")
    print("*"*nB+" "*mB," "*mB+"*"*nB)
    if(iCount< iLevel-1):
        bCount += 1 
    else:    
        bCount -= 1
    aCount += 2
    iCount += 1
print()
iCount =int(0)
inCount =int(0)
while (iCount < iLevel*2-1):#正三角間隔1,#橫式正三角間隔1
    n = inCount+1
    nB = int((inCount/2)+1)
    m = iLevel - inCount
    n2 = int(n/2)
    m2 = int(m/2) 
    if iCount < iLevel:
        print(" "*m+"* "*n+" "*m," "*n+"* "*m+" "*n,end="  ")
    else:
        print(" "*(m+n*2+m)," "*(n+m*2+n),end="  ")
    if(iCount % 2 != 0):
        print(end=" ")
    print("* "*nB+" "*m," "*m+" *"*nB)
    if(iCount< iLevel-1):
        inCount += 1 
    else:    
        inCount -= 1
    iCount += 1
print() 
iCount =int(0)
aCount =int(iLevel*2-4)
bCount =int(0)
while (iCount < (iLevel*2-1)):#房形反白
    n = aCount+1
    m = iLevel*2 -1 - aCount
    m2 = int(m/2)
    if iCount < (iLevel-1):
        print("*"*m2+" "*n+"*"*m2,"*"*(m+n-1),end=" ")
    elif iCount == (iLevel-1) :
        print("*"*(m+n-1),"*"*(m+n-1),end=" ")
    else:
        print("*"*(m+n-1),"*"*m2+" "*n+"*"*m2,end=" ")
    n = bCount+1   
    m = iLevel*2 - bCount -1
    print(" "*n+"*"*m,"*"*m+" "*n)
    if(iCount<iLevel-1):
        aCount -= 2
        bCount += 1
    else:    
        aCount += 2
        bCount -= 1
    iCount += 1
print() 
iCount =int(0)
aCount =int(0)
bCount =int(0)
while (iCount < (iLevel*2-1)):#房形
    n = aCount+1
    m = iLevel*2 -1 - aCount
    m2 = int(m/2)
    if iCount < iLevel:
        print(" "*m2+"*"*n+" "*m2,"*"*(m+n-1),end="  ")
    else:
        print("*"*(m+n-1)," "*m2+"*"*n+" "*m2,end="  ")
    n = iLevel+bCount   
    m = iLevel - bCount -1
    print("*"*n+" "*m," "*m+"*"*n)
    if(iCount<iLevel-1):
        aCount += 2
        bCount += 1
    else:    
        aCount -= 2
        bCount -= 1
    iCount += 1
print()
iCount =int(0)
while (iCount < iLevel):#空心直角三角
    n = iCount-1
    m = iLevel - iCount -2
    if (iCount==0):
        print("*"+" "*((m+2)*2)+"*","*"+"*"*m+"*"+" "*((n+2)*2)+"*"+"*"*m+"*")
    elif(iCount==iLevel-1):
        print("*"+"*"*n+"*"+" "*((m+2)*2)+"*"+"*"*n+"*","*"+" "*((n+2)*2)+"*")
    else:
        print("*"+" "*n+"*"+" "*((m+2)*2)+"*"+" "*n+"*","*"+" "*m+"*"+" "*((n+2)*2)+"*"+" "*m+"*")
    iCount += 1
print()
iCount =int(0)
aCount =int(0)
bCount =int(0)
#奇偶判定
if iLevel%2==0:
    inLevel = i2Level   
else:
    inLevel = iLevel
while (iCount < inLevel):#空心正三角+空心橫式正三角
    if(aCount < inLevel):
        n = aCount+1
        m = inLevel - aCount
        n2 = int(n/2)
        m2 = int((m+1)/2)
        if iCount == 0:
            print(" "*m2+"*"*n+" "*m2," "*n2+"*"*m+" "*n2,end="  ")
        elif iCount == (inLevel+1)/2 -1:  
            print(" "*m2+"*"*n+" "*m2," "*n2+"*"*m+" "*n2,end="  ")
        else: 
            print(" "*m2+"*"+" "*(n-2)+"*"+" "*m2," "*n2+"*"+" "*(m-2)+"*"+" "*n2,end="  ")
        aCount += 2
    else:
        print(" "*(m2+n+m2)," "*(n2+m+n2),end="  ")
    n = bCount+1
    m = inLevel - bCount
    if (iCount == 0) or (iCount == inLevel-1):
        print("*"*n+" "*m," "*m+"*"*n)
    else:
        print("*"+" "*(n-2)+"*"+" "*m," "*m+"*"+" "*(n-2)+"*")
    if(iCount<inLevel/2-1):
        bCount += 1
    else:    
        bCount -= 1
    iCount += 1
print()
iCount =int(0)
aCount =int(0)
bCount =int(0) 
while (iCount < iLevel*2-1):#空心正三角+1,#空心橫式正三角+1 
    nA = aCount+1
    nB = bCount+1
    m = iLevel*2 - aCount-1
    mB = iLevel - bCount
    n2 = int(nA/2)
    m2 = int(m/2) 
    if iCount < iLevel:
        if (iCount == 0) or (iCount == iLevel-1) :
            print(" "*m2+"*"*nA+" "*m2," "*n2+"*"*m," "*n2,end="  ")
        else:
            print(" "*m2+"*"+" "*(nA-2)+"*"+" "*m2," "*n2+"*"+" "*(m-2)+"*"," "*n2,end="  ")
    else:
        print(" "*(m2+nA+m2)," "*(n2+m+n2),end=" ")
    if (iCount == 0) or (iCount == iLevel*2-2) :
        print("*"*nB+" "*mB," "*mB+"*"*nB)
    else:
        print("*"+" "*(nB-2)+"*"+" "*mB," "*mB+"*"+" "*(nB-2)+"*")
    if(iCount< iLevel-1):
        bCount += 1 
    else:    
        bCount -= 1
    aCount += 2
    iCount += 1
print()
iCount =int(0)
inCount =int(0)
while (iCount < iLevel*2-1):#空心正三角間隔1,#空心橫式正三角間隔1 
    n = inCount+1
    nB = int((inCount/2)+1)
    m = iLevel - inCount
    n2 = int(n/2)
    m2 = int(m/2) 
    if iCount < iLevel:
        if (iCount == 0) or (iCount == iLevel-1):
            print(" "*m+"* "*n+" "*m," "*n+"* "*m+" "*n,end="  ")
        else:
            print(" "*m+"* "+"  "*(n-2)+"* "+" "*m," "*n+"* "+"  "*(m-2)+"* "+" "*n,end="  ")
    else:
        print(" "*(m+n*2+m)," "*(n+m*2+n),end="  ")
    if(iCount % 2 != 0):
        print(end=" ")
    else:
        print(end="")
    if(iCount < 3) or (iCount > iLevel*2-5):
        print("* "*nB+" "*m," "*m+" *"*nB)
    elif(iCount %2 == 0):
        print("* "+"  "*(nB-2)+"* "+" "*m," "*m+" *"+"  "*(nB-2)+" *")
    else:
        print("  "*(nB-1)+"* "+" "*m," "*m+" *"+"  "*(nB-1))
    if(iCount< iLevel-1):
        inCount += 1 
    else:    
        inCount -= 1
    iCount += 1
print() 
iCount =int(0)
aCount =int(iLevel*2-4)
bCount =int(0)
while (iCount < (iLevel*2-1)):#空心房形反白
    n = aCount+1
    m = iLevel*2 -1 - aCount
    m2 = int(m/2)
    if(iCount == 0):
        print("*"*m2+" "*n+"*"*m2,"*"*(m+n-1),end=" ")
    elif(iCount == iLevel*2-2):
        print("*"*(m+n-1),"*"*m2+" "*n+"*"*m2,end=" ")
    else:
        if iCount < (iLevel-1):
            print("*"+" "*(m2-2)+"*"+" "*n+"*"+" "*(m2-2)+"*","*"+" "*(m+n-3)+"*",end=" ")
        elif iCount == (iLevel-1) :
            print("*"+" "*int((m+n-2)/2-1)+"*"+" "*int((m+n-2)/2-1)+"*","*"+" "*int((m+n-2)/2-1)+"*"+" "*int((m+n-2)/2-1)+"*",end=" ")
        else:
            print("*"+" "*(m+n-3)+"*","*"+" "*(m2-2)+"*"+" "*n+"*"+" "*(m2-2)+"*",end=" ")
    n = bCount+1   
    m = iLevel*2 - bCount -1
    if (iCount == 0) or (iCount == iLevel*2-2):
        print(" "*n+"*"*m,"*"*m+" "*n)
    else:
        print(" "*n+"*"+" "*(m-2)+"*","*"+" "*(m-2)+"*"+" "*n)
    if(iCount<iLevel-1):
        aCount -= 2
        bCount += 1
    else:    
        aCount += 2
        bCount -= 1
    iCount += 1
print() 
iCount =int(0)
aCount =int(0)
bCount =int(0)
while (iCount < (iLevel*2-1)):#空心房形
    n = aCount+1
    m = iLevel*2 -1 - aCount
    m2 = int(m/2)
    if iCount < iLevel:
        if iCount == 0:
            print(" "*m2+"*"*n+" "*m2,"*"*(m+n-1),end="  ")
        else:
            print(" "*m2+"*"+" "*(n-2)+"*"+" "*m2,"*"+" "*(m+n-3)+"*",end="  ")
    else:
        if iCount == (iLevel*2-2):
            print("*"*(m+n-1)," "*m2+"*"*n+" "*m2,end="  ")
        else:
            print("*"+" "*(m+n-3)+"*"," "*m2+"*"+" "*(n-2)+"*"+" "*m2,end="  ")
    n = iLevel+bCount   
    m = iLevel - bCount -1
    if (iCount == 0) or (iCount == iLevel*2-2):
        print("*"*n+" "*m," "*m+"*"*n)
    else:
        print("*"+" "*(n-2)+"*"+" "*m," "*m+"*"+" "*(n-2)+"*")
    if(iCount<iLevel-1):
        aCount += 2
        bCount += 1
    else:    
        aCount -= 2
        bCount -= 1
    iCount += 1