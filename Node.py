class Node:
    index = 0
    value = None
    left = None
    right = None

    def __init__(self, ind, val=None):
        self.value = val
        self.index = ind

    def __lt__(self, other):
        if self.index < other.index:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.index > other.index:
            return True
        else:
            return False
