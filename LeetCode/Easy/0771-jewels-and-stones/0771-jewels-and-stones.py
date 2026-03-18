class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
         # seperate our jewel string into individual jewels.
        sep_jewels = list(jewels)
        sep_stones = list(stones)

        # count for our actual jewels.
        my_jewels = 0

        # if a stone is actually a jewel, then we have a jewel. 
        for stone in sep_stones:
            if stone in sep_jewels:
                my_jewels = my_jewels + 1

        # return Jewel count
        return my_jewels
