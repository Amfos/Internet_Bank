# from Exceptions import *


class InternetBank (object):
   balance = 5000
   attempts = 3
   user_can_get_money = False

   def top_up_money(self, my_money):
       return self.balance + my_money

   def enter_pin_code(self, pin_code):
       correct_pin_cod = 333
       if self.attempts == 0:
           return ("Your card has been blocked")
           # raise AttemptsOver

       if pin_code != correct_pin_cod:
           self.attempts = self.attempts - 1

       if pin_code == correct_pin_cod:
           self.user_can_get_money = True
           return True

   def get_my_money(self, user_get_money):

       if self.user_can_get_money:
           if user_get_money <= self.balance:
               self.balance = self.balance - user_get_money
               return user_get_money

           # if self.balance == 0:
           #      return "You haven't money"
           #
           # if user_get_money > self.balance:
           #     return "You haven't money in your card"

           else:
               return "You don't have enough money!!"
