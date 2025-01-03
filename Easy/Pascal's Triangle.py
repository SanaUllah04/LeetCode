class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:  # Base case for one row
            return [[1]]
        
        triangle = [[1]]  # Start with the first row
        
        for i in range(1, numRows):
            row = [1]  # Every row starts with 1
            for j in range(1, i):
                # Calculate the sum of the two elements above
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Every row ends with 1
            triangle.append(row)
        
        return triangle