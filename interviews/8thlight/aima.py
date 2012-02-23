#!/bin/python
opponent = -1
def print_game_state(game_state):
	d = {-1:' ',0:'O',1:'X'}
	print "\n" 
	for x,i in enumerate(game_state):
		if x%3==2:
			print "%s" % d[i], "\n-------"
		if x%3==0 or x%3==1:
			print "%s|" % d[i],

def minimax_decision(game_state):
	print "Calling min_value from minimax_decision"
	return min_value(game_state)

	

def actions(game_state):
	return False	

def utility(game_state,piece):
	wins = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
	#wins_with_position = [ i for i in wins if position in i]
	#count = 0
	for i in wins:
		three_moves = [game_state[i[0]],game_state[i[1]],game_state[i[2]]]
		#print "Three_move:",three_moves
		if ((three_moves[0]==three_moves[1]==three_moves[2])):
		#or (three_moves[0]==three_moves[1] and (three_moves[2]==-1 or three_moves[2]==piece))
		#or ((three_moves[0]==-1 or three_moves[0]==piece) and three_moves[1]==three_moves[2])
		#or (three_moves[0]==three_moves[2] and (three_moves[1]==-1 or three_moves[1]==piece))):
			#print "Win/Possible win:",three_moves
			if piece == three_moves[0]:
				return 1
			else:
				return -1
	
	return 0


def result(a,game_state):
	#input action, game_state
	new_game_state = game_state[:]
	new_game_state[a[0]]=a[1]
	return new_game_state

def terminal_test(game_state):
	#print "In terminal test, game_state:", print_game_state(game_state)
	if not any(i for i in game_state if i==-1):
		print "Found terminal state"
		return True
	if((game_state[0]==game_state[1]==game_state[2]!=-1)
	or(game_state[0]==game_state[3]==game_state[6]!=-1)
	or(game_state[0]==game_state[4]==game_state[8]!=-1)
	or(game_state[1]==game_state[4]==game_state[7]!=-1)
	or(game_state[2]==game_state[4]==game_state[6]!=-1)
	or(game_state[2]==game_state[5]==game_state[8]!=-1)
	or(game_state[3]==game_state[4]==game_state[5]!=-1)
	or(game_state[6]==game_state[7]==game_state[8]!=-1)):
		print "Found terminal state"
		return True
	return False

def successors(game_state, piece):
	visited_nodes =[]	
	successors = []
	for x,i in enumerate(game_state):
		if i==-1 and x not in visited_nodes:
			successor = game_state[:]
			visited_nodes.append(x)
			successor[x] = piece
			successors.append(successor)
	return successors
	 

def max_value(game_state):
	print "In max state:", print_game_state(game_state)
	if terminal_test(game_state):
		util = utility(game_state,opponent^1)
		print "Max:The utility value for this one was", util
		return util
	v = []
	for s in successors(game_state,opponent^1):
		print "Processing successor",s,"in max_value"
		v.append(min_value(s))
	print "Returning max value from",v
	return max(v)

def min_value(game_state):
	
	print "In min state:", print_game_state(game_state)
	if terminal_test(game_state):
		util = utility(game_state,opponent^1)
		print "Min:The utility value for this one was", util
		return util

	
	v = []
	for s in successors(game_state,opponent):
		print "Processing successor",s,"in min_value"
		v.append(max_value(s))
	print "Returning min value",v
	return min(v)



if __name__ == '__main__':
	r = []
	opponent = 0
	game_board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
	for i in range(0,9):
		_game_board = game_board[:]
		_game_board[i]=1
		r.append(min_value(_game_board))
		print _game_board,"Completed",r
	print r, max(r)

##	game_state = [-1]*8
#	x=input('Play first[0], play second[1]')
#	print x
#	if x == 0:
#		while(terminal_test(game_state)):
#			x=input('Your move')	
#			game_state[x]= 1
#			print game_state
#			print 'My move'
#			minimax_decision(game_state)
#			game_state[x]= 0
#			
#			print game_state
#	else:
#		while(terminal_test(game_state)):
#			print game_state
#			minimax_decision(game_state)
#			game_state[x]=1
#			print 'My move'	
#			
