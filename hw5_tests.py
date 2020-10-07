# Christian Werner
# wernerck
# SI 507 - 003
# Worked with: N/A

import unittest
import hw5_cards

class TestCard(unittest.TestCase):

	def test_construct_Card(self):
		c1 = hw5_cards.Card(0, 2)
		c2 = hw5_cards.Card(1, 1)

		self.assertEqual(c1.suit, 0)
		self.assertEqual(c1.suit_name, "Diamonds")
		self.assertEqual(c1.rank, 2)
		self.assertEqual(c1.rank_name, "2")

		self.assertIsInstance(c1.suit, int)
		self.assertIsInstance(c1.suit_name, str)
		self.assertIsInstance(c1.rank, int)
		self.assertIsInstance(c1.rank_name, str)

		self.assertEqual(c2.suit, 1)
		self.assertEqual(c2.suit_name, "Clubs")
		self.assertEqual(c2.rank, 1)
		self.assertEqual(c2.rank_name, "Ace")
		
	def test_q1(self):
		'''
		1. fill in your test method for question 1:
		Test that if you create a card with rank 12, its rank_name will be "Queen"
		
		2. remove the pass command
		
		3. uncomment the return command and 
		3b. change X, Y to the values from your assert statement
		### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

		'''
		c1 = hw5_cards.Card(0, 12)

		self.assertEqual(c1.rank_name, "Queen")
		return c1.rank_name, "Queen"
	
	def test_q2(self):
		'''
		1. fill in your test method for question 1:
		Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
		
		2. remove the pass command
		
		3. uncomment the return command and 
		3b. change X, Y to the values from your assert statement
		### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

		'''
		c1 = hw5_cards.Card(1, 5)

		self.assertEqual(c1.suit_name, "Clubs")
		return c1.suit_name, "Clubs"        

	def test_q3(self):
		'''
		1. fill in your test method for question 3:
		Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

		2. remove the pass command
		
		3. uncomment the return command and 
		3b. change X, Y to the values from your assert statement
		### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

		'''
		c1 = hw5_cards.Card(3, 13)

		self.assertEqual(c1.__str__(), "King of Spades")
		return c1.__str__(), "King of Spades"
	
	def test_q4(self):
		'''
		1. fill in your test method for question 4:
		Test that if you create a deck instance, it will have 52 cards in its cards instance variable
		
		2. remove the pass command
		
		3. uncomment the return command and 
		3b. change X, Y to the values from your assert statement
		### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

		'''
		d1 = hw5_cards.Deck()
		
		self.assertEqual(len(d1.cards), 52)
		return len(d1.cards), 52 

	def test_q5(self):
		'''
		1. fill in your test method for question 5:
		Test that if you invoke the deal_card method on a deck, it will return a card instance.
		
		2. remove the pass command
		
		3. uncomment the return command and 
		3b. change X, Y to the values from your assert statement
		### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

		'''
		d1 = hw5_cards.Deck()

		self.assertIsInstance(d1.deal_card(), hw5_cards.Card)
		return d1.deal_card(), hw5_cards.Card
	
	def test_q6(self):
		'''
		1. fill in your test method for question 6:
		
		Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
		
		2. remove the pass command
		
		3. uncomment the return command and 
		3b. change X, Y to the values from your assert statement
		### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

		'''
		d1 = hw5_cards.Deck()
		deck_size1 = len(d1.cards) # check the original deck size
		
		d1.deal_card() # the card that was dealt
		deck_size2 = len(d1.cards) # check the new deck size; should have one fewer

		self.assertEqual(deck_size1-1, deck_size2)
		return deck_size1-1, deck_size2

	def test_q7(self):
		'''
		1. fill in your test method for question 7:
		Test that if you invoke the replace_card method, the deck has one more card in it afterwards. 
		(Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)
		
		2. remove the pass command
		
		3. uncomment the return command and 
		3b. change X, Y to the values from your assert statement
		### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

		'''
		d1 = hw5_cards.Deck() # start out with 52 cards

		c1 = d1.deal_card() # the card that was dealt
		deck_size1 = len(d1.cards) # check the new deck size; should have 51 cards now

		d1.replace_card(c1) # adds same card back in 
		deck_size2 = len(d1.cards) # should have 52 cards again

		self.assertEqual(deck_size1+1, deck_size2, 52)
		return deck_size1+1, deck_size2, 52
	
	def test_q8(self):
		'''
		1. fill in your test method for question 8:
		Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.
		(The function must silently ignore it if you try to add a card that’s already in the deck)
		
		2. remove the pass command
		
		3. uncomment the return command and 
		3b. change X, Y to the values from your assert statement
		### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

		'''
		c1 = hw5_cards.Card(1, 4) # create card

		d1 = hw5_cards.Deck()
		deck_size1 = len(d1.cards)
		
		d1.replace_card(c1)
		deck_size2 = len(d1.cards)

		self.assertEqual(deck_size1, deck_size2)
		return deck_size1, deck_size2


if __name__=="__main__":
	unittest.main()