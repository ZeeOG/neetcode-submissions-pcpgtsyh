class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i in range(k):
            output.append(max(count, key = count.get))
            del(count[max(count, key = count.get)])
        return output    



                     


        