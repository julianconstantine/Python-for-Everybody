import os
import re

__author__ = 'j_caracotsios'

path = os.getcwd()

# To match the end of a string, you use the DOLLAR SIGN ($) but it has to be put at the end of the regular expression
if re.search('week-2-assignment$', path) is None:
    os.chdir('week-2-assignment')


file_name = 'regex_sum_210560.txt'

# Open file and initialize list of numbers/sum to 0
f = open(file_name, 'rb')
numbers = []
sum_numbers = 0

# Go through each line in the file, find all the numbers in that line, and store them in the list 'numbers'
for line in f:
    numbers_in_line = re.findall('[0-9]+', line)
    numbers += numbers_in_line

print("There are %i numbers in the file '%s'" % (len(numbers), file_name))
print("\n")

# Go through list 'numbers' and sum up all elements
for i in range(len(numbers)):
    sum_numbers += int(numbers[i])

print("The numbers in '%s' sum to %i" % (file_name, sum_numbers))

