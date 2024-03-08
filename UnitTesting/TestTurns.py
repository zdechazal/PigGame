import unittest
from unittest.mock import patch
from Turn import Turn

class test_turns(unittest.TestCase):
    
    def set_up_class(self):
        self.player = "Player_One"
        self.winning_score = 15   
        self.turn = Turn(self.player, self.winning_score)
    
    @patch ('PigGame.Turn.py.randint', return_value = 4)
    
    def test_roll_dice(self, mock_randint):
        result = self.turn.roll_dice()
        
        self.assertEqual(result, 4)
        
        


if __name__ == '__main__':
    unittest.main()
