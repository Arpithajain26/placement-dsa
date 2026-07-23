from typing import List

def markrow(i,matrix):
    for j in range(len(matrix)):
        if matrix[i][j]!=0:
            matrix[i][j]=-1
def markcol(j,matrix):
    for i in range(len(matrix)):
        if matrix[i][j]!=0:
            matrix[i][j]=-1

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    markrow(i,matrix)
                    markcol(j,matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==-1:
                    matrix[i][j]=0
        return matrix
a=Solution()
print(a.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))






class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=[0]*len(matrix)
        col=[0]*len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] or col[j]:
                    matrix[i][j]=0
        return matrix
a=Solution()
print(a.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))

        