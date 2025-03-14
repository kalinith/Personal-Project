from cell import Cell

class Move():
    def __init__(self, cell=None, value=None, prev_move=None, next_move=None,  deadlock=False, options=None):
        self.changed_cell = cell
        self.value = value
        self.prev_move = prev_move
        self.next_move = next_move
        self.deadlock = deadlock
        if self.prev_move != None:
            prev_move.next_move = self
        self.dead_ends = list()
        self.viable_values = options
        
    def updateRef(self, ref, val):
        if ref == "prev":
            self.prev_move = val
        elif ref == "next":
            self.next_move = val
        return

    def __str__(self):
        if self.changed_cell == None and self.value == "start":
            return(f"start: start")
        elif self.changed_cell != None and self.value != None:
            return(f"{self.changed_cell.get_grid_pos()}: {self.value}")    
        else:
            return("-")

    def __repr__(self):
        output = list()
        indent = ""
        if self.changed_cell == None and self.value == "start":
            output.append(f"Changed Cell         : This is the start of the change log:")
            output.append(f"{indent}Value                : start")
        else:
            output.append(f"{indent}Changed Cell         : {self.changed_cell.get_grid_pos()}")
            output.append(f"{indent}Value                : {self.value}")
        output.append(f"{indent}Previous move        : {self.prev_move}")
        output.append(f"{indent}Next move            : {self.next_move}")
        output.append(f"{indent}Deadlocked           : {self.deadlock}")
        output.append(f"{indent}list of dead ends    :\n{self.dead_ends}")
        output.append(f"{indent}List of viable values: {self.viable_values}")
        output.append("====================================================\n")
        return "\n".join(output)


# when a move is made we need to log the cell that was changed and the value that was filled in
# we will need to know what the change before was as well.
# to track this we will have a change field in the grid that will point to the current move class.
# when a deadlock occurs we will record this as a split point
# 
# once we reach a point where the puzzle is not solved but an empty cell has no options we need to
#   work through the changes undoing what was done until we get to the last deadlock.
# we then step back one more step so we are at the point where a deadlock candidate was chosen and we pick a new candidate.
# but first we need to re-initialise the options for the grid and remove the last deadlock candidate picked as an available option.

