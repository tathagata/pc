def terminal_test(game_state):
	if not any(i for i in game_state if i==-1):
		return True
	
	for i in wins:
		win_moves = [game_state[i[0]],game_state[i[1]],game_state[i[2]]]
		if win_moves[0]==win_moves[1]==win_moves[2] and not any(i for i in win_moves if i==-1):
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
	
	
def heuristic(game_state,player):
	for i in wins:
		win_moves = [game_state[i[0]],game_state[i[1]],game_state[i[2]]]
		if all(win_moves[0]==i for i in win_moves):
			if win_moves[0]==max_player:
				return 1
			else:
				return -1
	return 0


def print_game_state(game_state):
	d = {-1:' ',0:'O',1:'X'}
	print "\n" 
	for x,i in enumerate(game_state):
		if x%3==2:
			print "%s" % d[i], "\n-------"
		if x%3==0 or x%3==1:
			print "%s|" % d[i], 

def alphabeta(game_state, depth, alpha, beta, player):
	if depth == 0 or terminal_test(game_state):
		h= heuristic(game_state,player)
		return h
	if player == max_player:
		max_nodes =[]
		for s in successors(game_state,player):
			val = max(alpha, alphabeta(s,depth-1,alpha,beta,player^1))	
			max_nodes.append((s,val))
			alpha = max(alpha,val)
			if beta<=alpha:
				break
		return alpha
	else:
		min_nodes = []
		for s in successors(game_state, player):
			val = min(beta, alphabeta(s,depth-1,alpha, beta, player^1))
			min_nodes.append((s,val))
			beta = min(beta,val)
			if beta <= alpha:
				break
		return beta


def decide_move(game_state):
	max_val = -float('inf')
	max_nodes = []
	for s in successors(game_state,max_player):
		
		val=alphabeta(s,15,-float('inf'),float('inf'),max_player^1)
		max_nodes.append((s,val))
		if val>max_val:
			max_val=val
			_game_state = s
	return _game_state
 	
if __name__ == '__main__':
	game_state = [-1]*9	
	wins = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
	x= input('Who plays first?(Computer:0/you:1)')
	if x == 0:
		max_player = 1
		game_state=decide_move(game_state)
	else:
		max_player = 0
	
	print_game_state(game_state)
	while(not terminal_test(game_state)):
		move=input('Your move, specify square[0,8]:')
		if game_state[move]!=-1:
			print "That square is taken"
			continue
		game_state[move]=max_player^1
		print_game_state(game_state)
		game_state=decide_move(game_state)
		print "My move:"
		print_game_state(game_state)
