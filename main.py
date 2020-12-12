board = [[ 5 , 3 , 0 , 0 , 7 , 0 , 0 , 0 , 0 ],
[ 6 , 0 , 0 , 1 , 9 , 5 , 0 , 0 , 0 ],
[ 0 , 9 , 8 , 0 , 0 , 0 , 0 , 6 , 0 ],
[ 8 , 0 , 0 , 0 , 6 , 0 , 0 , 0 , 3 ],
[ 4 , 0 , 0 , 8 , 0 , 3 , 0 , 0 , 1 ],
[ 7 , 0 , 0 , 0 , 2 , 0 , 0 , 0 , 6 ],
[ 0 , 6 , 0 , 0 , 0 , 0 , 2 , 8 , 0 ],
[ 0 , 0 , 0 , 4 , 1 , 9 , 0 , 0 , 5 ],
[ 0 , 0 , 0 , 0 , 8 , 0 , 0 , 7 , 9 ]]

#Sudoku Solver


  
       
def print_board(board):
 numrows = len(board)
 numcols= len(board[0])
 j=0
 for i in range(numrows):
   for j in range(numcols):
     print(board[i][j], end= "  ")
   print("\n")


def find_zero(board):
 d = []
 for i in board:  
    if 0 in i:
     d.append(board.index(i))
     d.append(i.index(0))
     return d

  
  
def is_valid(board, row, col, value):
  #Checking row
  if value in board[row]:
    return False
  #Checking column
  for i in board:
    if i[col] == value:
      return False
 
  #Defining where the inner matrix (3x3) with the value begins. (The start position is always the top-left corner)
  x = (row//3)*3
  y = (col//3)*3
 
  #Going through the matrix (3x3) - 
  #0,0 - 0,1 - 0,2
  #1,0 - 1,1 - 1,1
  #2,0 - 2,1 - 2,2
  #It checks ALL values inside the matrix (3x3)
  for j in range(0, 3):
    for k in range(0, 3):
      if board[x+j][y+k] == value:
        return False
  return True
def solve(board):
  zPoint = find_zero(board)
  if zPoint == None:
    return print_pretty(board)
  x = zPoint[0]
  y = zPoint[1]
  for i in range(1,10):
    if is_valid(board,x,y,i):
      board[x][y] = i
      solve(board)
      #Reset the value if the number was wrong
      board[x][y] = 0
  return None

def print_pretty(board):
  if board is None:
     return 'There is no numbers here'
  
  print ('-'*25)
 
  for i in range(len(board)):
    colDiv = '| '
 
    if i != 0 and i % 3 == 0:
      print ('-'*25)
 
    for j in range(len(board)):
      if board[i][j] == 0:
        board[i][j] = ' '
 
      if j != 0 and j % 3 == 0:
        colDiv += '| ' + str(board[i][j]) + ' '
          
      else:
        colDiv += str(board[i][j]) + ' '
 
    print(colDiv + '|')
 
  print('-'*25)