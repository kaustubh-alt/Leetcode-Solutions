class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        size = None
        if len(words) > 0:
            size = len(words[0]) 
        else:
            return []

        i = 0
        j = len(words)*size

        ans = []

        wrd = sorted(words)

        while j <= len(s):
            srt = s[i:j]
            chunk = [srt[i:i+size] for i in range(0, len(srt), size)]
            if sorted(chunk) == wrd:
                ans.append(i)
            
            i += 1
            j += 1

        return ans
        



        
