Sudoku Project

this project is written in python.
To run the program you will need a python enterpreter v 3.12.
also needed will be the following packages:


simply run "python main.py" from a cmd prompt in the project folder.
This consists of 3 parts.

1. accept a sudoku grid as input and attempt to solve it.
    for example:given a list of dictionaries
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

2. Accept parameters for an unsolved sudoku and generate it.
    for example fill:9 or perhaps a difficulty(easy, medium, hard)
    2.1 use text input to allow the user to solve.
    
3. given a partially solved sudoku with multiple outcomes, return the number of possible solutions.
    
    for example, in the grid below 1:5 and 1:6 can hold 1 or 4, 7:9 and 9:9 can hold 6 or 9. 4:7 and 6:7 can hold 8 or 2.

       1 2 3 4 5 6 7 8 9
      ╔═════╦═════╦═════╗
    0 ║5│9│3║8│ │ ║6│7│2║
    1 ║4│6│7║ │ │ ║3│1│8║
    2 ║1│2│8║6│7│3║9│4│5║
      ╠═════╬═════╬═════╣
    3 ║3│7│ ║ │ │ ║ │5│4║
    4 ║9│ │ ║4│ │ ║7│6│3║
    5 ║6│ │4║ │ │7║ │9│1║
      ╠═════╬═════╬═════╣
    6 ║7│ │ ║ │ │2║4│8│ ║
    7 ║8│3│9║5│ │ ║1│2│7║
    8 ║2│4│ ║7│ │8║5│3│ ║
      ╚═════╩═════╩═════╝
