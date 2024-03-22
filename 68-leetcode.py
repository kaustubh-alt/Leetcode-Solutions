word = ["This", "is", "an", "example", "of", "text", "justification."]
maxwidth = 16
word.append(101)
ls = []
templs = []
lentemp = 0
for i in word:
    if i == 101:
        remspace = maxwidth - lentemp
        a = ' '*remspace
        templs.append(a)
        srt = ''.join(templs)
        ls.append(srt)
        templs = []
        lentemp = 0
        continue
        
        
    if lentemp+len(i) >= maxwidth:
        templs.pop()
        lentemp -= 1
        a , b = divmod(maxwidth,lentemp)
        it = int(len(templs)/2)
        b = int(b/(it))+1
        a = ' '*b
        odd = [num for num in range(1, it+2) if num % 2 != 0]
        for j in odd:
            templs[j] = a
        
        srt = ''.join(templs)
        ls.append(srt)
        templs = []
        lentemp = 0
        
        

    templs.append(i)
    templs.append(' ')
    lentemp += len(i)+1
    
for i in ls:
    print(len(i))
