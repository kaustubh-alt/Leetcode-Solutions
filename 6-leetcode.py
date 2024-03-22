class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = numRows
        s = s
        ls = []
        ack = a
        temp = []
        pointer = 0
        block = False
        while True:
            if ack == 1:
                ack = a
            
            elif block:
                break
                
            if ack == a:
                ak = 0
                for i in range(pointer,pointer+(a)):
                    if i >= len(s):
                        temp.append('')
                        block = True
                        
                    else:
                        temp.append(s[i])
                    ak = i
                ls.append(temp)
                temp = []
                pointer = ak+1
                ack-=1
                
                
            
            elif ack != a:
                ak = 0
                for i in range(pointer,pointer+(a)):
                    if i >= len(s):
                        temp.append('')
                    elif ak == ack-1:
                        temp.append(s[pointer])
                        
                    else:
                        temp.append('')
                    ak += 1
                
                ls.append(temp)
                temp = []
                ack-=1
                pointer += 1
                
        newst = ""  
        for i in range(a):
            acc = i
            for j in range(len(ls)):
                if i >= len(s):
                        continue
                newst += ls[j][acc]

        return newst
        
