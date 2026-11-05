class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = set()
        seenCol = set()
        seenBox= set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]

                if num == ".":
                    continue

                row = (i, num)
                col = (j, num)
                box = (i // 3, j // 3, num)

                if row in seenRow or col in seenCol or box in seenBox:
                    return False
                seenRow.add(row)
                seenCol.add(col)
                seenBox.add(box)
        
        return True 