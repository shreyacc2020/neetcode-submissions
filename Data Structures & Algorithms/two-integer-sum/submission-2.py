class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            firstNumber = nums[i]
            secondNumber = target-firstNumber

            if secondNumber not in hashMap:
                hashMap[firstNumber] = i
                # print(hashMap)
            else:
                temp = []
                temp.append(hashMap[secondNumber])
                temp.append(i)
                return temp