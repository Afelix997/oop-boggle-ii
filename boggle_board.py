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

      def include_word(self, word):
            count=0
            word_list=list(word.upper())
            while count<4:
                  horz= [self.board[count][0],self.board[count][1],self.board[count][2],self.board[count][3]]
                  vert= [self.board[0][count],self.board[1][count],self.board[2][count],self.board[3][count]]
                  if vert== word_list or vert.reverse()== word_list or horz== word_list or horz.reverse() == word_list:
                        return True
                  count+=1
            diag_1=[self.board[0][0],self.board[1][1],self.board[2][2],self.board[3][3]]
            diag_2=[self.board[0][3],self.board[1][2],self.board[2][1],self.board[3][0]]
            print(word_list)
            print(diag_1)
            if word_list==diag_1 or word_list==diag_1.reverse()or word_list== diag_2.reverse()or word_list== diag_1:
                        return True
            return print(False)

                        


board = BoggleBoard()

board.shake()

board.include_word("EeoA")

