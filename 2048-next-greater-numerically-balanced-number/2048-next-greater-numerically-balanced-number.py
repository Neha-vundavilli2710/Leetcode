from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x):
            c = Counter(str(x))
            for d, count in c.items():
                if int(d) != count:
                    return False
            return True
        
        num = n + 1
        while True:
            if is_balanced(num):
                return num
            num += 1
