class Solution:
    def validate_columns(self, board: List[List[str]]) -> bool:
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                value = board[row][col]
                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)
        return True

    def validate_rows(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for value in row:
                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)
        return True

    def validate_blocks(self, board: List[List[str]]) -> bool:
        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        value = board[block_row + i][block_col + j]
                        if value != ".":
                            if value in seen:
                                return False
                            seen.add(value)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.validate_rows(board)
            and self.validate_columns(board)
            and self.validate_blocks(board)
        )
