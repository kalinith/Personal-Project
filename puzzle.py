import time
from grid import Grid
from movelog import Move

def get_values(v_type):
    if v_type == "grid":
        pass
    if v_type == "parms":
        nums = input("How many numbers would you like from 27 to 39:")
        try:
            nums = int(nums)
        except:
            print(f"{nums} is not a number")
            nums = get_values("parms")
        if nums < 27:
            print(f"{nums} is below 27, setting to 27")
            nums = 27
        if nums > 39:
            print(f"{nums} is above 39, setting to 39")
            nums = 39
        return nums

def solve_puzzle(puzzle):
    if puzzle == None:
        return
    while puzzle.solved == False and puzzle.updated == True:
        solve_puzzle_r(puzzle)
        if puzzle.updated == False:
            solve_pick_deadlock(puzzle)

def solve_puzzle_r(puzzle):
    puzzle.passes += 1
    puzzle.updated = False
    for row in puzzle.data.values():
        for column in row.values():
            # for each number go through each cell one by one
            for option in range(1,10):
                #loop through the numbers 1 to 9
    
                if column.val == option:
                    # if the cell has a value check if that value matches the number,
                    # if it does call grid.remove_option_row_column
                    puzzle.remove_option_subgrid(option, column)
                    puzzle.remove_option_row_column(option, column)
                    break
                    # skip the rest of the range

                if column.val == None and column.is_option(option) == "y":
                    only_option = True
                    # for this cell, if this value is an option.
                    for cell in row.values():# if the value is an option in this row but only for this subgrid
                        if cell.get_subgrid() != column.get_subgrid() and cell.is_option(option) == "y":
                            only_option = False
                    if only_option == True:
                        # clear it from the rest of the subgrid.
                        puzzle.remove_option_subgrid(option, column, "row")

                    x, y = column.get_grid_pos()
                    only_option = True
                    for c_row in puzzle.data.values():
                        for c_col in c_row.values():
                            c_x, c_y = c_col.get_grid_pos()
                            if c_y == y and c_col.get_subgrid() != column.get_subgrid() and c_col.is_option(option) == "y":
                                # if the value is an option in this column, but only for this subgrid
                                only_option = False
                    if only_option == True:
                        # clear it from the rest of the subgrid.
                        puzzle.remove_option_subgrid(option, column, "col")
                    
                    # see if the value is only an option for this cell in this row or column
                    if puzzle.check_if_option_exists_row_column(option, column) == False:
                        puzzle.set_option_as_value(option, column)
                        break
                        
                    # or this subgrid
                    if puzzle.check_option_subgrid(option, column) == False:
                        puzzle.set_option_as_value(option, column)
                        break

                    if column.has_options() == 1:
                        # if the cell has no value check the potential numbers
                        # if the number is one of the potential ones check if there are any other potential numbers
                        # if not set the cell to the number and call remove_option_row_column
                        puzzle.set_option_as_value(option, column)
                        break

                if column.val == None and column.has_options() == 0:
                    if puzzle.origin == dict():
                        print("bad solve")
                        return
                    else:
                        rollback(puzzle)
                        return

    solved = True
    for row in puzzle.data.values():
        for col in row.values():
            if col.val == None:
                solved = False
    puzzle.solved = solved

def solve_pick_deadlock(puzzle):
    if puzzle == None:
        return
    if puzzle.solved == True:
        return
    puzzle.pick_deadlock()
    puzzle.deadlocks += 1

def rollback(puzzle):
    if puzzle.change == None:
        raise Exception("No moves made")
    if puzzle.change.value == "start":
        raise Exception("this is the start move")
    old_move = puzzle.change
    while old_move.deadlock != True:
        old_move = rollback_r(old_move)
        if old_move.value == "start":
            raise Exception("invalid move")

    puzzle.change = Move(old_move.changed_cell,None,old_move.prev_move,None,True,old_move.viable_values)
    puzzle.dead_ends = old_move.dead_ends
    puzzle.dead_ends.append(old_move)
    puzzle.change.viable_values.remove(old_move.value)
    if len(puzzle.change.viable_values) == 0:
        old_move = rollback_r(old_move)
        puzzle.change = old_move
        rollback(puzzle)
        return

    val = puzzle.change.viable_values[0]
    puzzle.change.changed_cell.set_val(val)
    puzzle.change.value = val

    puzzle.fix_options() # I think this function is fucked
    puzzle.updated = True

def rollback_r(move):
    if move == None:
        raise Exception("No moves made")
    cell = move.changed_cell
    if cell == None:
        raise Exception("no cell stored")
    cell.clear_val()
    return move.prev_move


def main():
    start = time.time()
    # https://abcnews.go.com/blogs/headlines/2012/06/can-you-solve-the-hardest-ever-sudoku
    fill = {
        0: {0:8,},
        1: {2:3, 3:6,},
        2: {1:7, 4:9, 6:2},
        3: {1:5, 5:7,},
        4: {4:4, 5:5, 6:7,},
        5: {3:1, 7:3,},
        6: {2:1, 7:6, 8:8,},
        7: {2:8, 3:5, 7:1,},
        8: {1:9, 6:4,},
    }
    grid2 = Grid(fill)
    print(repr(grid2))
    solve_puzzle(grid2)
    print(grid2)
    print(f"the solve took {grid2.passes} passes and had {grid2.deadlocks} deadlocks")
    end = time.time() #somewhere later
    print("The time of execution of above program is :",
          (end-start) * 10**3, "ms")
    #grid2.print_log()

if __name__ == "__main__":
    main()


