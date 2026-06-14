class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        n = len(numbers)
        

        for i in range(n):
            l = i+1
            r=n-1
            need = target-numbers[i]
            while l<=r:
                mid = ((r-l)//2)+l
                if numbers[mid]==need:
                    return [i+1,mid+1]
                elif numbers[mid]<need:
                    l=mid+1
                else:
                    r=mid-1

        return []