class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        numbers = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                numbers.append(nums[i][j])
                
        if r * c != len(numbers):
            return nums
        
        results = []
        
        index = 0
        for i in range(r):
            results.append([])
            for j in range(c):
                results[i].append(numbers[index])
                index += 1

        return results