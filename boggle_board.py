import random

def print_board(board):
      for row in board:
            print(row[0], row[1], row[2], row[3])
def rand_dice_list(list):
      dice_num_list=[]
      for dice in list:
            dice_num_list.append(random.choice(dice))
      return dice_num_list

class BoggleBoard:
      dice = [
            'AAEEGN','ELRTTY','AOOTTW','ABBJOO','EHRTVW','CIMOTU','DISTTY','EIOSST',
            'DELRVY','ACHOPS','HIMNQU','EEINSU','EEGHNW','AFFKPS','HLNNRZ','DEILRX'
      ]

      def __init__(self):
            self.board = [
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_']      
            ]
            return print_board(self.board)

  

      def shake(self):
            self.dice_list=rand_dice_list(BoggleBoard.dice)
            count=0
            while count<16:
                  for row in range(len(self.board)):
                        for col in range(len(self.board[row])):
                              if self.dice_list[count] == 'Q':
                                    self.dice_list[count]='Qu'
                        self.board[row][col]= self.dice_list[count]
                        count+=1
            return print_board(self.board)
      
      def include_word(self):
            pass
