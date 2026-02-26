class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        s = list(s)
        
        while s != ['1']:
            # Even → divide by 2
            if s[-1] == '0':
                s.pop()
                steps += 1
            else:
                # Odd → add 1
                i = len(s) - 1
                
                # Carry propagation
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                
                if i >= 0:
                    s[i] = '1'
                else:
                    s.insert(0, '1')
                
                steps += 1
        
        return steps