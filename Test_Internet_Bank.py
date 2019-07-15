
import unittest
from Internet_Bank import *


class Test_calc(unittest.TestCase):
   def setUp(self):
       self.terminal = InternetBank()
       self.terminal.enter_pin_code(333)

   def test_top_up_money(self):
       my_money = self.terminal.top_up_money(5000)
       self.assertEqual(my_money, 10000)

   def test_inccorect_top_up_money(self):
       my_money = self.terminal.top_up_money(5000)
       self.assertNotEqual(my_money, 9000)

   def test_string_top_up_money(self):
       my_money = self.terminal.top_up_money('Hello')
       self.assertEqual(my_money, 5000)

   def test_string_plus_number_top_up_money(self):
       my_money = self.terminal.top_up_money('Hefs333')
       self.assertEqual(my_money, 5000)

   def test_minus_one_top_up_money(self):
       my_money = self.terminal.top_up_money(-1)
       self.assertEqual(my_money, 5000)

   def test_zero_top_up_money(self):
       #this test should be down
       my_money = self.terminal.top_up_money(0)
       self.assertEqual(my_money, 5000)

   def test_enter_pin_code(self):
       self.assertTrue(self.terminal.enter_pin_code(333))

   def test_enter_pin_code_new(self):
       self.assertTrue(self.terminal.enter_pin_code(3333))
       self.assertTrue(self.terminal.user_can_get_money)

   def test_inccorect_pin_code(self):
       self.assertFalse(self.terminal.enter_pin_code(2131))

   def test_attempts(self):
       self.assertEqual(self.terminal.attempts, 3)

   def test_attempts_failer(self):
       incorrect_attempt_1 = self.terminal.enter_pin_code(222)
       incorrect_attempt_2 = self.terminal.enter_pin_code(222)
       incorrect_attempt_3 = self.terminal.enter_pin_code(222)
       self.assertEqual(self.terminal.attempts, 0)
       self.assertTrue(self.terminal.user_can_get_money)

   def test_user_can_get_money(self):
       user_get_money = self.terminal.get_my_money(5000)
       self.assertEqual(self.terminal.balance, 0)

   def test_user_cannot_get_money(self):
       user_cannot_get_money = self.terminal.get_my_money(-1)
       self.assertEqual(self.terminal.balance, 5000)

   def test_user_cannot_get_more_money(self):
       user_cannot_get_more_money = self.terminal.get_my_money(5001)
       self.assertEqual(self.terminal.balance, 5000)

   def test_user_cannot_get_zero_money(self):
       user_cannot_get_zero_money = self.terminal.get_my_money(0)
       self.assertEqual(self.terminal.balance, 5000)

   def test_user_can_get_half_money(self):
       user_can_get_half_mony = self.terminal.get_my_money(2500)
       self.assertEqual(self.terminal.balance, 2500)

   def test_more_get_money(self):
       user_can_get_1 = self.terminal.get_my_money(2500)
       user_can_get_2 = self.terminal.get_my_money(2500)
       self.assertEqual(self.terminal.balance, 0)

   def test_cany_more_get_money(self):
       user_can_get_1 = self.terminal.get_my_money(2500)
       user_can_get_2 = self.terminal.get_my_money(3000)
       self.assertEqual(self.terminal.balance, 2500)

   def test_more_get_money_with_minus(self):
       user_can_get_1 = self.terminal.get_my_money(2500)
       user_can_get_2 = self.terminal.get_my_money(-1)
       self.assertEqual(self.terminal.balance, 2500)

