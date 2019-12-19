import unittest

from challenge4.GenerateFibonacci import Fibonacci
from challenge4.Challenge4_Numbertowords import NumberToWord

class Challenge4(unittest.TestCase):

    def test_fibonacci(self):

        # Get order
        order = input("Enter Fibonacci series order(integer) : ")
        try:
            order = int(order)
        except ValueError:
            assert False, "Invalid input, please enter a number > 0"

        # Get Fibonacci number
        fibonacci_number = Fibonacci.fibonacci(order)
        print(fibonacci_number)

        variable = NumberToWord.GetNumbertoWord(str(fibonacci_number))
        print(variable)
if __name__ == '__main__':
    unittest.main()