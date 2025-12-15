from arrays import Array

class Grid(object):
    def __init__(self, rows, columns, fill_value=None):
        """Initialize a 2D grid."""
        self.data = Array(rows)

        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        """Return the number of rows in the grid."""
        return len(self.data)

    def get_width(self):
        """Return the number of columns in the grid."""
        return len(self.data[0])
    
    def __getitem__(self, index):
        """Supports two-dimensional indexing with [row][col]."""
        return self.data[index]
    
    def __str__(self):
        """Return a string representation of the grid."""
        grid_str = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                grid_str += str(self.data[row][col]) + " "
            grid_str += "\n"
        return grid_str

def iterate_grid(grid):
    """Iterate through each element in the 2D grid."""
    for row in range(grid.get_height()):        # Iterate through each row
        for col in range(grid.get_width()):     # Iterate through each column
            yield grid[row][col]        