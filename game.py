import random
export LC_ALL=en_US.UTF-8
export LANG = en_US.UTF-8
"""
Traditional gawi-bawi-bo game

@author Eunsu Jeong
@created 12-10-2016
"""
def determine_winner(my_hand, com_hand):
	"""
	Determine winner of the game.
	
	:param my_hand: my hand parameter
	:param com_hand: predefined computer choice
	:return None: None is returned. (void)
	===============
	Gawi, Bawi, Bo
	===============

	----------------
	Gawi, Bawi, Bo
	----------------

	Chapter 1 What is this game
	---------------------------
	It's Rock Scissors Paper


	Chapter 1.1 Definition
	~~~~~~~~~~~~~~~~~~~~~~~
	One person and other person can play this game.

	"""
	a = com_hand - my_hand
	if a>0 or a==-2:
		print "You Win"
	elif a == 0:
		print "Draw"
	else:
		print "You Lose"
if __name__ == '__main__':
	com_hand = random.randint(0,2)

	print("Show your hand (0: gawi, 1:bawi, 2:bo)")
	my_hand = int(input())
	determine_winner(my_hand, com_hand)
