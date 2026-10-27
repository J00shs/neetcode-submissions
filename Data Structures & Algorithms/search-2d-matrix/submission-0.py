class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])


        top, bottom = 0, Rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            # Check target against rightmost value in row
            if target > matrix[row][-1]:
                # shift row down
                top = row + 1
            # Check target against smaller value
            elif target < matrix[row][0]:
                # shift row up
                bottom = row - 1
            else:
                break
        # If target is not found
        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        L, R = 0, Cols - 1
        while L <= R:
            m = (L +R )//2
            if target > matrix[row][m]:
                L = m + 1
            elif target < matrix[row][m]:
                R = m - 1
            else:
                return True
        return False
        


                





         

