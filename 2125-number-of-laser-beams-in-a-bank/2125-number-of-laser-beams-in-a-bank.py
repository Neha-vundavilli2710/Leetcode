class Solution:
    def numberOfBeams(self, bank):
        prev = 0
        result = 0

        for row in bank:
            devices = row.count('1')
            if devices > 0:
                result += prev * devices
                prev = devices

        return result
