Sudoku Project

this project is written in python.
To run the program you will need a python enterpreter v 3.12.


simply run "python main.py" from a cmd prompt in the project folder.

1. accept a sudoku grid as input and attempt to solve it.
     the grid can be edited in sudokugrid.py and works as follows:

    (
      0:{1:8,4:1,7:5,8:3,},
      1:{4:8,5:9,8:6,},
      2:{5:7,8:2,}
      3:{2:4,},
      4:{7:8,8:1,},
      5:{1:2,2:6,},
      6:{2:9,5:1,6:6,8:8,},
      7:{3:5,5:3,},
      8:{0:1,2:3,3:6,6:7,}.
    )
    
    will result in a grid drawn like this

       0 1 2 3 4 5 6 7 8 
      ╔═════╦═════╦═════╗
    0 ║ │8│ ║ │1│ ║ │5│3║
    1 ║ │ │ ║ │8│9║ │ │6║
    2 ║ │ │ ║ │ │7║ │ │2║
      ╠═════╬═════╬═════╣
    3 ║ │ │4║ │ │ ║ │ │ ║
    4 ║ │ │ ║ │ │ ║ │8│1║
    5 ║ │2│6║ │ │ ║ │ │ ║
      ╠═════╬═════╬═════╣
    6 ║ │ │9║ │ │1║6│ │8║
    7 ║ │ │ ║5│ │3║ │ │ ║
    8 ║1│ │3║6│ │ ║7│ │ ║
      ╚═════╩═════╩═════╝

    the program will then attempt to solve this.

