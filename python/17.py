import time
import math

start_time = time.time()

# takes a number and says whether it is in ones, tens, hundreds or thousands range
# for example: 5 => 'ones', 15 => 'tens', 150 => 'hundreds'
# will return total number of digits in the number
def find_digits_in_number(n):

	digits = 0
	num = n

	if (num == 0):
		return 1

	while (num != 0):
		# trim the digit by one
		num = num/10
		# add one to digit
		digits = digits + 1

	return digits

# returns the naming rule for numbers which have unique numbers
def basic_rule(n):
	RULES = {
		0: '',
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',
		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		14: 'fourteen',
		15: 'fifteen',
		16: 'sixteen',
		17: 'seventeen',
		18: 'eighteen',
		19: 'nineteen',
		20: 'twenty',
		100: 'onehundred',
		1000: 'onethousand'
	}
	return RULES[n]

# naming rule for tens position
def tens_rule(n):
	RULES = {
		0: '',
		1: 'ten',
		2: 'twenty',
		3: 'thirty',
		4: 'forty',
		5: 'fifty',
		6: 'sixty',
		7: 'seventy',
		8: 'eighty',
		9: 'ninety'
	}
	return RULES[n]

# main module which decides the naming rule of this number depending on its digits
def naming_rules(num):
	
	digits = find_digits_in_number(num)
	name = ''

	if (num <= 20):
		name = basic_rule(num)

	elif (num > 20 and num < 100):
		ones_digit = num%10
		tens_digit = num/10
		# generate the name
		name = tens_rule(tens_digit) + basic_rule(ones_digit)
	
	elif (num == 100):
		name = basic_rule(num)
	
	elif (num > 100 and num < 1000):
		
		connecting_word = 'and'

		ones_digit = num%10
		quotient = num/10
		tens_digit = quotient%10
		
		# handle a special case for tens and ones digit in the range of 11 to 19
		last_two_digits = tens_digit*10 + ones_digit
		
		if (last_two_digits >=10 and last_two_digits <= 19 ):
			# reset the tens digit
			tens_digit = 0
			# which will give the basic rule
			ones_digit = last_two_digits

		if (tens_digit == 0 and ones_digit == 0):
			# do not display the connecting word
			connecting_word = ''

		hundreds_digit = quotient/10

		# generate the name
		name = basic_rule(hundreds_digit) + "hundred" + connecting_word + tens_rule(tens_digit) + basic_rule(ones_digit)
	
	elif (num == 1000):
		name = basic_rule(num)

	return name


NAMES_LENGTH = 0
# calculate the length for numbers till 1000
for i in range(1000, 0, -1):
	NAMES_LENGTH = NAMES_LENGTH + len(naming_rules(i))

print "TOTAL LENGTH: ", NAMES_LENGTH

print time.time() - start_time, " seconds"

































