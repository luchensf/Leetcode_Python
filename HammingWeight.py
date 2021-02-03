class Solution:
    def hamming_weight(self, n: int):
        counter = 0
        while n != 0:
            counter += 1
            n = n & (n - 1)
        return counter
