from cell import Cell, Plot
from movelog import Move

class Grid():
    def __init__(self,fill = dict()):
        self.data = dict()
        for r in range(9):
            row = dict()
            if r in fill:
                row_data = fill[r]
            else:
                row_data = dict()
            for c in range(9):
                if c in row_data:
                    cell = Cell(r, c,row_data[c])
                    cell.init_option("n")
                else:
                    cell = Cell(r, c)
                row[c] = cell
            self.data[r] = row
        for rowkey in fill:
            for colkey in fill[rowkey]:
                self.remove_option_row_column(fill[rowkey][colkey], self.data[rowkey][colkey])
        self.origin = fill
        self.solved = False
        self.passes = 0
        self.updated = True
        self.resets = 0
        self.change = Move()
        self.change.value = "start"
        self.start = self.change

    def remove_option_row_column(self, option, cell):# also removes this option from cells in subgrid
        x, y = cell.get_grid_pos()
        for row_data in self.data.values():
            for cell_ in row_data.values():
                x1, y1 = cell_.get_grid_pos()
                if cell != cell_:
                    if (cell.get_subgrid() == cell_.get_subgrid() or x1 == x or y1 == y) and cell_.is_option(option) == "y":
                        cell_.remove_option(option)
                        self.updated = True
                
    def remove_option_subgrid(self, option, cell, direction=None):# removes the option from all cells in the subgrid excluding those in the direction
        x, y = cell.get_grid_pos()
        x_sub, y_sub = cell.get_subgrid()
        for i in range((x_sub * 3), (x_sub * 3) + 3):
            for j in range((y_sub * 3), (y_sub * 3) + 3):
                if (direction == "row" and i != x) or (direction == "col" and j != y) or (direction == None):
                    if self.data[i][j].is_option(option) == "y":
                        self.data[i][j].remove_option(option)
                        self.updated = True

    def check_if_option_exists_row_column(self, option, cell):
        x, y = cell.get_grid_pos()
        for value in self.data.values():
            for cell_ in value.values():
                x1, y1 = cell_.get_grid_pos()
                if cell != cell_:
                    if (x1 == x or y1 == y) and cell_.is_option(option) == 'y':
                        return True
        return False

    def check_option_subgrid(self, option, cell):
        x, y = cell.get_grid_pos()
        x_sub, y_sub = cell.get_subgrid()
        for i in range((x_sub * 3), (x_sub * 3) + 3):
            for j in range((y_sub * 3), (y_sub * 3) + 3):
                if ((i != x or j != y) and self.data[i][j].is_option(option) == "y"):
                        return True
        return False

    def set_option_as_value(self, option, cell, deadlock=False):
        cell.set_val(option)
        self.remove_option_row_column(option, cell)
        self.remove_option_subgrid(option, cell)
        self.updated = True
        move = Move(cell, option, self.change, None,  deadlock)
        self.change = move

    def pick_deadlock(self):
        least_options = 10
        least_cell = None
        for row in self.data.values():
            for col in row.values():
                nr_options = len(col.get_options())
                if nr_options < least_options and col.val == None:
                    least_options = nr_options
                    least_cell = col
        if least_options == 1:
            option = least_cell.get_options()
        elif least_options == 0 or least_options == 10:
            raise Exception(f"Error: least_options = {least_options}, nr_options = {nr_options}, getoptions = {col.get_options()}")
        else:
            options = least_cell.get_options()
            for option in options:
                used = False
                if self.change.value == "start":
                    # the puzzle has started on a deadlock
                    break
                if self.change.next_move != None:
                    print("why is next move not none?")
                    for next_move in self.change.next_move:
                        if next_move.changed_cell == least_cell and next_move.change == option:
                            used = True
                if used == False:
                    break
        print(f"--------------------------------------------Deadlock--------------------------------------------")
        print(f"{least_cell}. the option chosen was {option}")
        print(f"------------------------------------------------------------------------------------------------")
        self.set_option_as_value(option, least_cell, True)

    def fix_options(self):
        for row in self.data.values():
            for cell in row.values():
                if cell.val != None:
                    cell.init_option("n")
                    self.remove_option_subgrid(cell.val, cell)
                    self.remove_option_row_column(cell.val, cell)
                    continue
                for option in range(1,10):
                    if cell.is_option(option) == "y":
                        only_option = True
                        for cell in row.values():# if the value is an option in this row but only for this subgrid
                            if cell.get_subgrid() != cell.get_subgrid() and cell.is_option(option) == "y":
                                only_option = False
                        if only_option == True:
                            # clear it from the rest of the subgrid.
                            self.remove_option_subgrid(option, cell, "row")

                        x, y = cell.get_grid_pos()
                        only_option = True
                        for c_row in self.data.values():
                            for c_col in c_row.values():
                                c_x, c_y = c_col.get_grid_pos()
                                if c_y == y and c_col.get_subgrid() != cell.get_subgrid() and c_col.is_option(option) == "y":
                                    # if the value is an option in this column, but only for this subgrid
                                    only_option = False
                        if only_option == True:
                            # clear it from the rest of the subgrid.
                            self.remove_option_subgrid(option, cell, "col")

#########Printing the move log#######

    def print_log(self, currentmove=None, depth=0):
        if currentmove == None:
            currentmove = self.start
        while currentmove.next_move != None:
            currentmove = self.print_log_r(currentmove, depth)

    def print_log_r(self, currentmove, depth):
        if currentmove.value == "start":
            print(repr(currentmove))
        else:
            print(repr(currentmove), depth)
        if currentmove.dead_ends != []:
            for dead_end in currentmove.dead_ends:
                depth += 1
                print_log(dead_end, depth)
            print("===========")
        return currentmove.next_move

##########end##########
                    
    def __str__(self):
        top    = f"╔═════╦═════╦═════╗"
        mid    = f"╠═════╬═════╬═════╣"
        bottom = f"╚═════╩═════╩═════╝"
        output = list()
        output.append(top)
        for r in range(9):
            line = ["║",]
            for c in range(9):
                cell_value = self.data[r][c].val
                if cell_value == None:
                    line.append(" ")
                else:
                    line.append(str(cell_value))
                if c % 3 == 2:
                    line.append("║")
                else:
                    line.append("│")
            line = "".join(line)
            output.append(line)
            if r == 2 or r == 5:
                output.append(mid)
            if r == 8:
                output.append(bottom)

        return "\n".join(output)

    def __repr__(self):
        top    = f"╔═════╦═════╦═════╗"
        mid    = f"╠═════╬═════╬═════╣"
        bottom = f"╚═════╩═════╩═════╝"
        output = list()
        output.append(top)
        for r in range(9):
            line = ["║",]
            line2 = []
            for c in range(9):
                cell_value = self.data[r][c].val
                if cell_value == None:
                    line.append(" ")
                else:
                    line.append(str(cell_value))
                line2.append(str(repr(self.data[r][c])))
                if c % 3 == 2:
                    line.append("║")
                    line2.append("║")
                else:
                    line.append("│")
                    line2.append("│")
            line = "".join(line)
            line2 = "".join(line2)
            output.append(line+line2)
            if r == 2 or r == 5:
                output.append(mid)
            if r == 8:
                output.append(bottom)

        return "\n".join(output)
