#!/bin/python


def gen_next_move(game_board,piece):
	visited_nodes =[]	
	next_move_set = []
	for x,i in enumerate(game_board):
		if i==-1 and x not in visited_nodes:
			next_move = game_board[:]
			visited_nodes.append(x)
			next_move[x] = piece
			next_move_set.append(next_move)
	return next_move_set
	 
def count_num_wins(game_board,position,piece):
	wins = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
	wins_with_position = [ i for i in wins if position in i]
	#print "Wins with position:",wins_with_position
	new_game_board = game_board[:]
	new_game_board[position] = piece
	#print "Game board with the move",new_game_board
	count = 0
	for i in wins_with_position:
		three_moves = [new_game_board[i[0]],new_game_board[i[1]],new_game_board[i[2]]]
		#print "Three_move:",three_moves
		if ((three_moves[0]==three_moves[1]==three_moves[2])
		or (three_moves[0]==three_moves[1] and (three_moves[2]==-1 or three_moves[2]==piece))
		or ((three_moves[0]==-1 or three_moves[0]==piece) and three_moves[1]==three_moves[2])
		or (three_moves[0]==three_moves[2] and (three_moves[1]==-1 or three_moves[1]==piece))):
			#print "Win/Possible win:",three_moves
			count=count+1
	
	return count

def start():
	game_board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
	t=check_end_game(game_board)
	print "check:",t
	game_board = [0,1,0,0,1,0,0,1,0]
	t= check_end_game(game_board)
	print "check",t

def check_end_game(game_board):
	if((game_board[0]==game_board[1]==game_board[2]!=-1)
	or(game_board[0]==game_board[3]==game_board[6]!=-1)
	or(game_board[0]==game_board[4]==game_board[8]!=-1)
	or(game_board[1]==game_board[4]==game_board[7]!=-1)
	or(game_board[2]==game_board[4]==game_board[6]!=-1)
	or(game_board[2]==game_board[5]==game_board[8]!=-1)
	or(game_board[3]==game_board[4]==game_board[5]!=-1)
	or(game_board[6]==game_board[7]==game_board[8]!=-1)):
		return True
	else:
		return False

if __name__ == '__main__':
	#game_board = [0,1,1,-1,1,-1,-1,0,-1]
	#for i in gen_next_move(game_board,1):print i
	
	game_board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
	for i in range(0,9):
		print i," has ",number_of_wins(game_board,i,1)," wins"
	
def maxmove(game_board):
	if check_end_game(game_board):
		print "Game over!"
		return
	num_wins = 0
	moves = gen_next_move(game_board,1)
	for move in moves:
		move=minmove(apply_move(game_board,move))	
		if num_wins(game_board,move,1)
			
