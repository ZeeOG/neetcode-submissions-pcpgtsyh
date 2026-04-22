class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = [[] for _ in range(len(nums) + 1)]
        returned = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
            
        for i in count:
            output[count[i]].append(i)
        for i in range(len(output) - 1, 0, -1):
            for num in output[i]:
                returned.append(num)
                if len(returned) == k:
                    return returned


            
                
      
           



                     


        