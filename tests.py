import unittest

from cell import Cell
from grid import Grid
from puzzle import get_values, solve_puzzle

class Tests(unittest.TestCase):
    def test_create_empty_cell(self):
        cell = Cell(1,5)
        x, y = cell.get_grid_pos()
        self.assertEqual(
            x,
            1
            )
        self.assertEqual(
            y,
            5
            )
        x1, y1 = cell.get_subgrid_pos()
        self.assertEqual(
            x1,
            1
            )
        self.assertEqual(
            y1,
            2
            )
        self.assertEqual(
            cell.val,
            None
            )
        self.assertEqual(
            "the value of the cell at 1 and 5 can be one of the following:[1, 2, 3, 4, 5, 6, 7, 8, 9]",
            str(cell)
            )

    def test_options_change(self):
        cell = Cell(1,5)

        self.assertRaises(
            ValueError,
            cell.remove_option,10
            )

        cell.remove_option(5)
        self.assertEqual(
            "n",
            cell.is_option(5)
            )
        cell.remove_option(4)
        self.assertEqual(
            "n",
            cell.is_option(4)
            )

        cell.add_option(5)
        self.assertEqual(
            "y",
            cell.is_option(5)
            )

        cell.remove_option(5)
        self.assertEqual(
            "n",
            cell.is_option(5)
            )
        self.assertEqual(
            "the value of the cell at 1 and 5 can be one of the following:[1, 2, 3, 6, 7, 8, 9]",
            str(cell)
            )


    def test_value_manipulation(self):
        cell = Cell(1,5)

        cell.set_val(8)
        self.assertEqual(
            cell.val,
            8
            )
        self.assertEqual(
            cell.is_option(1),
            "n")
        self.assertEqual(
            str(cell),
            "the value of the cell at 1 and 5 is 8")


        cell.clear_val()
        self.assertEqual(
            cell.val,
            None
            )
        self.assertEqual(
            cell.is_option(8),
            "y"
            )
        self.assertEqual(
            "the value of the cell at 1 and 5 can be one of the following:[1, 2, 3, 4, 5, 6, 7, 8, 9]",
            str(cell)
            )

    def test_blank_grid_creation(self):
        grid = Grid()
        self.assertEqual(
            str(grid),
'''╔═════╦═════╦═════╗
║ │ │ ║ │ │ ║ │ │ ║
║ │ │ ║ │ │ ║ │ │ ║
║ │ │ ║ │ │ ║ │ │ ║
╠═════╬═════╬═════╣
║ │ │ ║ │ │ ║ │ │ ║
║ │ │ ║ │ │ ║ │ │ ║
║ │ │ ║ │ │ ║ │ │ ║
╠═════╬═════╬═════╣
║ │ │ ║ │ │ ║ │ │ ║
║ │ │ ║ │ │ ║ │ │ ║
║ │ │ ║ │ │ ║ │ │ ║
╚═════╩═════╩═════╝'''
            )

    def test_fill_grid(self):
        fill = {
            0: {1:8, 4:1, 7:5, 8:3,},
            1: {4:8, 5:9, 8:6,},
            2: {5:7, 8:2,},
            3: {2:4,},
            4: {7:8, 8:1,},
            5: {1:2, 2:6,},
            6: {2:9, 5:1, 6:6, 8:8,},
            7: {3:5, 5:3,},
            8: {0:1, 2:3, 3:6, 6:7,},
        }
        grid2 = Grid(fill)

        self.assertEqual(
            str(grid2),
'''╔═════╦═════╦═════╗
║ │8│ ║ │1│ ║ │5│3║
║ │ │ ║ │8│9║ │ │6║
║ │ │ ║ │ │7║ │ │2║
╠═════╬═════╬═════╣
║ │ │4║ │ │ ║ │ │ ║
║ │ │ ║ │ │ ║ │8│1║
║ │2│6║ │ │ ║ │ │ ║
╠═════╬═════╬═════╣
║ │ │9║ │ │1║6│ │8║
║ │ │ ║5│ │3║ │ │ ║
║1│ │3║6│ │ ║7│ │ ║
╚═════╩═════╩═════╝'''
            )
        self.assertEqual(
            grid2.data[0][1].val,
            8
            )

    def test_option_removal(self):
        fill = {
            0: {1:8, 4:1, 7:5, 8:3,},
            1: {4:8, 5:9, 8:6,},
            2: {5:7, 8:2,},
            3: {2:4,},
            4: {7:8, 8:1,},
            5: {1:2, 2:6,},
            6: {2:9, 5:1, 6:6, 8:8,},
            7: {3:5, 5:3,},
            8: {0:1, 2:3, 3:6, 6:7,},
        }
        grid2 = Grid(fill)
        grid2.remove_option_row_column(5, grid2.data[2][5])

        self.assertEqual(
            str(grid2.data[8][5]),
                "the value of the cell at 8 and 5 can be one of the following:[2, 4, 8]"
        )

        self.assertEqual(
            str(grid2.data[5][5]),
                "the value of the cell at 5 and 5 can be one of the following:[4, 8]"
            )

        self.assertEqual(
            str(grid2.data[4][5]),
                "the value of the cell at 4 and 5 can be one of the following:[2, 4, 6]"
            )

        self.assertEqual(
            str(grid2.data[2][6]),
                "the value of the cell at 2 and 6 can be one of the following:[1, 4, 8, 9]"
            )

        self.assertEqual(
            str(grid2.data[2][7]),
                "the value of the cell at 2 and 7 can be one of the following:[1, 4, 9]"
            )

        self.assertEqual(
            str(grid2.data[2][0]),
                "the value of the cell at 2 and 0 can be one of the following:[3, 4, 6, 9]"
            )

        self.assertEqual(
            str(grid2.data[2][1]),
                "the value of the cell at 2 and 1 can be one of the following:[1, 3, 4, 6, 9]"
            )

        self.assertEqual(
            str(grid2.data[2][2]),
                "the value of the cell at 2 and 2 can be one of the following:[1]"
            )

        self.assertEqual(
            str(grid2.data[2][3]),
                "the value of the cell at 2 and 3 can be one of the following:[3, 4]"
            )

        self.assertEqual(
            str(grid2.data[2][4]),
                "the value of the cell at 2 and 4 can be one of the following:[3, 4, 6]"
            )

        self.assertEqual(
            str(grid2.data[1][3]),
                "the value of the cell at 1 and 3 can be one of the following:[2, 3, 4]"
            )

        self.assertEqual(
            str(grid2.data[0][3]),
                "the value of the cell at 0 and 3 can be one of the following:[2, 4]"
            )

        self.assertEqual(
            str(grid2.data[0][5]),
                "the value of the cell at 0 and 5 can be one of the following:[2, 4, 6]"
            )

    def test_solve_puzzle(self):
        fill = {
            0: {1:8, 4:1, 7:5, 8:3,},
            1: {4:8, 5:9, 8:6,},
            2: {5:7, 8:2,},
            3: {2:4,},
            4: {7:8, 8:1,},
            5: {1:2, 2:6,},
            6: {2:9, 5:1, 6:6, 8:8,},
            7: {3:5, 5:3,},
            8: {0:1, 2:3, 3:6, 6:7,},
        }
        grid2 = Grid(fill)
        solve_puzzle(grid2)

        self.assertEqual(
            str(grid2),
                '''╔═════╦═════╦═════╗
║4│8│7║2│1│6║9│5│3║
║5│3│2║4│8│9║1│7│6║
║6│9│1║3│5│7║8│4│2║
╠═════╬═════╬═════╣
║9│1│4║8│3│2║5│6│7║
║3│7│5║9│6│4║2│8│1║
║8│2│6║1│7│5║3│9│4║
╠═════╬═════╬═════╣
║2│5│9║7│4│1║6│3│8║
║7│6│8║5│2│3║4│1│9║
║1│4│3║6│9│8║7│2│5║
╚═════╩═════╩═════╝'''
            )

    def test_solve_puzzle_with_deadlock(self):
        fill = {
            0: {0:5, 3:8, 6:6, 7:7,},
            1: {0:4, 2:7, 7:1,},
            2: {1:2, 5:3,},
            3: {1:7, 7:5,},
            4: {6:7, 8:3,},
            5: {0:6, 2:4,},
            6: {5:2, 6:4, 7:8,},
            7: {1:3, 2:9, 3:5, 6:1,},
            8: {3:7, 5:8, 6:5,},
        }
        grid2 = Grid(fill)
        solve_puzzle(grid2)
        self.assertEqual(
            str(grid2),
            '''╔═════╦═════╦═════╗
║5│9│3║8│4│1║6│7│2║
║4│6│7║2│5│9║3│1│8║
║1│2│8║6│7│3║9│4│5║
╠═════╬═════╬═════╣
║3│7│2║1│9│6║8│5│4║
║9│8│1║4│2│5║7│6│3║
║6│5│4║3│8│7║2│9│1║
╠═════╬═════╬═════╣
║7│1│5║9│3│2║4│8│6║
║8│3│9║5│6│4║1│2│7║
║2│4│6║7│1│8║5│3│9║
╚═════╩═════╩═════╝'''
            )
        self.assertEqual(
            grid2.deadlocks,
            1
            )
        self.assertEqual(
            grid2.passes,
            10
            )

    def test_solve_hardest_puzzle(self):
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
        solve_puzzle(grid2)
        self.assertEqual(
            str(grid2),
            '''╔═════╦═════╦═════╗
║8│1│2║7│5│3║6│4│9║
║9│4│3║6│8│2║1│7│5║
║6│7│5║4│9│1║2│8│3║
╠═════╬═════╬═════╣
║1│5│4║2│3│7║8│9│6║
║3│6│9║8│4│5║7│2│1║
║2│8│7║1│6│9║5│3│4║
╠═════╬═════╬═════╣
║5│2│1║9│7│4║3│6│8║
║4│3│8║5│2│6║9│1│7║
║7│9│6║3│1│8║4│5│2║
╚═════╩═════╩═════╝'''
            )
        self.assertEqual(
            grid2.deadlocks,
            33
            )
        self.assertEqual(
            grid2.passes,
            164
            )

if __name__ == "__main__":
    unittest.main()     

