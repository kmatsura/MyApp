import ui
import subprocess

score_a = 0
score_b = 0
game_a = 0
game_b = 0
freeze = 0 #flag of end
point_list = [] #history of the point
point_hist_a = []
point_hist_b = []
back = 0 #depth of undo


print('play')
print('Game Count 0-0')
print('0-0')


def calc_score(score):
	score_list = (0, 15, 30, 40, 'Ad', 0)
	n = score_list.index(score)
	return score_list[n+1]
	
def undo_score(score):
	score_list = (0, 15, 30, 40, 'Ad')
	n = score_list.index(score)
	return score_list[n-1]
	
def calc_tie(a, b):
	global freeze
	a = a + 1
	if a > 6 and (a - b) >= 2:
		freeze = 1
	return a
	
		
def plus_a(sender):
	global score_a
	global score_b
	global game_a
	global game_b
	global freeze
	global point_list
	global back
	if freeze == 1:
		return
		
	point_list.append(1)
	back = 0
	label_a = sender.superview['label1']
	label_b = sender.superview['label2']
	label_game_a = sender.superview['game_a']
	
	if freeze == 2:
		score_a = calc_tie(score_a, score_b)
		label_a.text = str(score_a)
		label_b.text = str(score_b)
		print(str(score_a)+'-'+str(score_b))
		if freeze == 1:
			label_fin = sender.superview['fin']
			label_fin.text = str('Game Set')
			print('Game Set')
		return
	
	score_a = calc_score(score_a)
	if score_a == 'Ad' and score_b == 'Ad':
		score_b = 40
		score_a = 40
		
	if score_a == 'Ad' and score_b != 40:
		score_a = calc_score(score_a)
	
	if score_a == 0:
		game_a = game_a + 1
		label_game_a.text = str(game_a)
		print('Game Count '+str(game_a)+'-'+str(game_b))
		score_b = 0
		
		if game_a == 6 and game_b == 6:
			print('Tie Break')
			freeze = 2
			label_fin = sender.superview['fin']
			label_fin.text = str('Tie Break')
			score_a = 0
			
		if game_a == 6 and game_b < 5:
			print('Game Set')
			freeze = 1
			label_fin = sender.superview['fin']
			label_fin.text = str('Game Set')
			return
		if game_a == 7 and game_b == 5:
			print('Game Set')
			freeze = 1
			label_fin = sender.superview['fin']
			label_fin.text = str('Game Set')
			print('Game Set')
			return
			
	label_a.text = str(score_a)
	label_b.text = str(score_b)
	print(str(score_a)+'-'+str(score_b))
	
	
def plus_b(sender):
	
	global score_a
	global score_b
	global game_a
	global game_b
	global freeze
	global point_list
	global back
	
	if freeze == 1:
		return
		
	point_list.append(2)
	back = 0
	
	label_a = sender.superview['label1']
	label_b = sender.superview['label2']
	label_game_b = sender.superview['game_b']
	
	if freeze == 2:
		score_b = calc_tie(score_b, score_a)
		label_a.text = str(score_a)
		label_b.text = str(score_b)
		print(str(score_a)+'-'+str(score_b))
		if freeze == 1:
			label_fin = sender.superview['fin']
			label_fin.text = str('Game Set')
		return
		
	score_b = calc_score(score_b)
	if score_a == 'Ad' and score_b == 'Ad':
		score_b = 40
		score_a = 40
		
	if score_b == 'Ad' and score_a != 40:
		score_b = calc_score(score_b)
		
	if score_b == 0:
		game_b = game_b + 1
		label_game_b.text = str(game_b)
		print('Game Count '+str(game_a)+'-'+str(game_b))
		score_a = 0
		
		if game_b == 6 and game_a == 6:
			print('Tie Break')
			freeze = 2
			label_fin = sender.superview['fin']
			label_fin.text = str('Tie Break')
			score_b = 0
		
		if game_b == 6 and game_a < 5:
			print('Game Set')
			freeze = 1
			label_fin = sender.superview['fin']
			label_fin.text = str('Game Set')
			return
			
		if game_b == 7 and game_a == 5:
			print('Game Set')
			freeze = 1
			label_fin = sender.superview['fin']
			label_fin.text = str('Game Set')
			return
	label_b.text = str(score_b)
	label_a.text = str(score_a)
	print(str(score_a)+'-'+str(score_b))
	
	
def undo(sender):
	global point_list
	last_win = point_list[-1]
	if last_win == 1:
		end
		
	return
	


def reset(sender):
	global score_a
	global score_b
	global game_a
	global game_b
	global freeze
	global point_list
	global back
	score_a = 0
	score_b = 0
	game_a = 0
	game_b = 0
	freeze = 0
	point_list = []
	back = 0
	label_a = sender.superview['label1']
	label_b = sender.superview['label2']
	label_game_a = sender.superview['game_a']
	label_game_b = sender.superview['game_b']
	label_b.text = str(score_b)
	label_a.text = str(score_a)
	label_game_a.text = str(game_a)
	label_game_b.text = str(game_b)
	
	label_fin = sender.superview['fin']
	label_fin.text = str('')
		
	print('The game has been reset.')
	print('-'*30)
	print('Game Count 0-0')
	print('0-0')

	
v = ui.load_view()
v.present('sheet')
