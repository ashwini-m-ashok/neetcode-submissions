class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,n,m = 0, len(matrix), len(matrix[0])
        r=n-1
        res = False
        while l<r: # 0,2 1
            mid = l+(r-l)//2
            if matrix[mid][m-1]<target:
                l=mid+1
            else:
                r=mid
        row_mid = r
        l,n = 0, len(matrix[0])
        r= n-1
        while l<=r:
            mid = l+(r-l)//2
            
            if matrix[row_mid][mid]<target:
                l=mid+1
            elif matrix[row_mid][mid]>target:
                r=mid-1
            else:
                res = True
                break
        return res