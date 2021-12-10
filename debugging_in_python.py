#! python3 

# ----------  Handling Exceptions

# def BoxPrint(symbol, length, width):
#     if len(symbol)!= 1:
#         raise Exception("Symbol length should be one")
#     if length<=3:
#         raise Exception("Length must be greater than three")
#     if width<=3:
#         raise Exception('Width must be greater than three')
    
#     print(symbol*width)
#     for i in range(length-2):
#         print(symbol + (" "*(width-2)) + symbol)
#     print(symbol*width)

# for sym, l, w in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         BoxPrint(sym, l, w)
#     except Exception as err:
#         print('An exception happened: ' + str(err))

# All the error types and error lines and all information about the error occurances
# is stored in the traceback stack which is a module 
# import traceback

# def Hello():
#     print("this is Hello() function")
#     raise Exception("This is error in Hello() function")

# def ErrorCase():
#     Hello()
#     print("This is ErrorCase function")
#     raise Exception("ErrorCase function is stopped")
# try:
#     ErrorCase()
# except:
#     # print(f"_cause_message = {traceback._cause_message}\n")

#     # print(f"_context_message = {traceback._context_message}\n")

#     # print(f"extract_stack = {traceback.extract_stack()}\n")

#     print(f"format_exc = {traceback.format_exc()}\n")

#     print(f"format_list = {traceback.format_list()}\n")

#     # print(f"format_stack = {traceback.format_stack()}\n")

# assertions examples -------------------
# say = True
# assert say == True, "This is error due to assignment of True"
# assert say == False, "This is error due to assignment of False"


# # ----------------- logging usage
# import logging
# # logging.disable(logging.CRITICAL) # to disable all the log statements in the program
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
# logging.debug('Start of program')

# def factorial(n):
#     logging.debug(f'Start of factorial {n}')
#     total = 1
#     for i in range(1,n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug(f'End of factorial {n}')
#     return total

# print(factorial(5))
# logging.debug('End of program')


# -------------project chapter 10
import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.disable()

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

choices = {"heads": 1, "tails": 0}

toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == choices[guess]:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug(f"Your guess input is guess = {guess}")
    if toss == choices[guess]:
        logging.debug(f"Your guess is correct guess = {guess}, toss = {toss}")
        print('You got it!')
    else:
        logging.debug(f"Your guess is in-correct guess = {guess}, toss = {toss}")
        print('Nope. You are really bad at this game.')