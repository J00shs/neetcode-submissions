class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = number of given hours to eat bananas, 
        # k = number of bananas we eat per hour
        # piles[i] is the number of bananas at that pile    
        # we could do i/k(rounding up)
        
        # h = 9
        # k = [1,2,3,4], the highest k can go is the max i
        # We need to find the first value of k where all bananas are consumed < h 

        L, R = 1, max(piles)
        res = R

        while L <= R:
            k = (L + R )//2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res,k)
                R = k - 1
            else:
                L = k + 1
        return res
        
    