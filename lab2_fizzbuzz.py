def fizz_buzz(n):
    """
    Returns a  value in repect to a nuber's divisiblity by three and five
    """
    if not (divisible_five(n)) and not divisible_three(n):
        return n
    elif divisible_three(n) and divisible_five(n):
		return 'FizzBuzz'
    elif divisible_five(n) or divisible_three(n):
		if divisible_five(n):
		 return 'Buzz'
		elif divisible_three(n):
			return 'Fizz'

def divisible_five(n):
	"""Returns true if number divisible by five"""
	if n%5 ==0:
		return True
def divisible_three(n):
	"""Returns true if number divisible by five"""
	if n%3 == 0:
		return True


print fizz_buzz(11)
