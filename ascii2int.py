numbers_list = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'trillion': 10000000000
}

# converts text to integers
def ascii2int(ascii_str):
    ascii_arr = ascii_str.strip().split()  # strip extra spaces and split sentence into words
    ascii_arr_clean = [i for i in ascii_arr if i in numbers_list] # remove words any words not in the numbers_list, for example "and"
    
    return 0


# create some temporary test cases
a = "one hundred"
b = "four hundred"
c = "five hundred and twenty one"
print(ascii2int(c))