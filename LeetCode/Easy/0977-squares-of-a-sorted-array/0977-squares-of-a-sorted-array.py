class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # Create a result list of placeholders
        squared_nums = [0] * n
        # pointer fors the beginning and end of nums
        start = 0
        end = n - 1
        # position pointer in squared_nums
        position = n - 1
        
        # Basically, if the number at the start is bigger square it and place in array
        # if the number at the end is bigger do the same
        # move the start or end of the array in and do it again
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                squared_nums[position] = nums[start] ** 2
                start += 1  

            else:
                squared_nums[position] = nums[end] ** 2
                end -= 1 
            
            # Move position pointer down a spot
            # We are working from greatest to least
            position -= 1
            
        return squared_nums