class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        parts = []
        
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1
            
            # found a primitive special substring
            if count == 0:
                # recursively process inside
                inner = self.makeLargestSpecial(s[start+1:i])
                parts.append('1' + inner + '0')
                start = i + 1
        
        # sort descending for lexicographically largest
        parts.sort(reverse=True)
        
        return ''.join(parts)