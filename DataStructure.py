class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.value)