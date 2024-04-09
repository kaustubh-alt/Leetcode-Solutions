class Solution:
    def timeRequiredToBuy(self, tickets, k: int) -> int:
        count = 0
        ab = tickets[k]
        for i,a in enumerate(tickets):
            if i <= k:
                if a < ab:
                    count += a
                else:
                    count += ab
            else:
                if a < ab:
                    count += a
                else:
                    count += ab-1
                    
        return count
