class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if matrix[i][-1]==target:
                return True
            if matrix[i][-1]>target:
                start = 0
                end = len(matrix[i])-1
                while(start<=end):
                    mid = start + (end-start)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]>target:
                        end = mid-1
                    else:
                        start = mid+1
                return False
        return False