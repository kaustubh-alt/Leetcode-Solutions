class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        for i in range(len(gas)):
            gasre = 0
            startst = i
            chec = False            
            while gasre != -1:
                if chec and i == startst:
                        
                        return i
                gasre += gas[startst]
                chec = True
                if cost[startst] > gasre:
                    break
                else:
                    
                    gasre -= cost[startst]
                    startst  = (startst+1)%len(gas)
                    continue
        return -1
                
        
        
                
                    
        
        
obj = Solution()
a = [5,5,1,3,4]
b = [8,1,7,1,1]
print(obj.canCompleteCircuit(a,b))
