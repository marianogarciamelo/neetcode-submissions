class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #rows
        n = len(matrix[0]) #cols
        t = m * n
        l, r = 0, t - 1

        while l <= r:
            m = (l+r) // 2
            i = m // n #row index
            j = m % n  #col index

            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                r = m - 1
            else:
                l = m + 1
        
        return False