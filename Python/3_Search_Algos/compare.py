def __lt__(self, other):
    """ Less than comparison operator"""
    return self.value < other.value

def __eq__(self, other):
    """ Equality comparison operator"""
    return self.value == other.value

def __gt__(self, other):
    """ Greater than comparison operator"""
    return self.value > other.value