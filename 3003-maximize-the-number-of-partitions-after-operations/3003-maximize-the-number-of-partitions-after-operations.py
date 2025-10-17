import string

def solve_partitions(s: str, k: int) -> int:
    """
    Calculates the number of partitions for a given string s' and integer k.
    This is the standard greedy partitioning algorithm.
    """
    n = len(s)
    count = 0
    i = 0
    while i < n:
        count += 1
        j = i
        distinct_chars = set()
        while j < n:
            char = s[j]
            
            # Check if adding the current character would exceed the k limit
            is_new_distinct = char not in distinct_chars

            if is_new_distinct and len(distinct_chars) == k:
                # The longest valid prefix ends at j-1
                break

            distinct_chars.add(char)
            j += 1
        i = j
    return count

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        # 1. Determine the optimal replacement character delta (δ)
        s_chars = set(s)
        delta = None
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if char not in s_chars:
                delta = char
                break
        
        # If all 26 characters are present, delta will remain None, but the optimal 
        # replacement logic (which is to maximize distinct count) still holds.
        # If all 26 are present, changing any s[i] to any other character c!=s[i] 
        # will result in the same set of 26 distinct characters, so we can just 
        # use an arbitrary replacement like 'a' if s[i] is 'b', etc.
        if delta is None:
            # All 26 letters are in s. Use a character different from s[0] as the replacement.
            # E.g., if s[0] is 'a', use 'b'. If s[0] is 'z', use 'a'.
            # The logic inside the loop will handle the case where delta is already in the string.
            delta = 'a' if s[0] != 'a' else 'b'

        # 2. No change case (Baseline)
        max_p = solve_partitions(s, k)

        # 3. Change at each index i
        for i in range(n):
            original_char = s[i]
            
            # Choose the optimal replacement:
            # If a character outside s exists, use it to guarantee max distinct increase.
            # Otherwise, use an arbitrary character different from s[i].
            if original_char == delta:
                # If s[i] is already our chosen delta, use a different arbitrary character
                replacement_char = 'a' if original_char != 'a' else 'b'
            else:
                replacement_char = delta

            # Create the modified string s_temp
            s_temp_list = list(s)
            s_temp_list[i] = replacement_char
            s_temp = "".join(s_temp_list)
            
            current_p = solve_partitions(s_temp, k)
            max_p = max(max_p, current_p)
            
        return max_p