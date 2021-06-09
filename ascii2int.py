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

def convert_word_to_int(ascii_arr_clean):
    # replace string with number representation
    # for example ['four', 'hundred', 'ten'] becomes [4, 100, 10]
    int_arr = [numbers_list[number_word] for number_word in ascii_arr_clean]
    
    print(int_arr) # debug statement
    
    if len(int_arr) == 4:
        # this case is for four digits, for example ['four', 'hundred', 'forty', 'two']
        # the first two digits are multiplied, and the rest are added => 4(100) + 40 + 2 = 442
        return (int_arr[0] * int_arr[1]) + int_arr[2] + int_arr[3]
    elif len(int_arr) == 3:
        # if there are three words, then the first must always be multiplied by the second,
        # for example ['two', 'hundred', 'twelve'] => 2(100) + 12 => 12
        return int_arr[0] * int_arr[1] + int_arr[2]
    elif len(int_arr) == 2:
        # if the array contains a 100, then multiply it by the preceding number
        # for example: ['two', 'hundred] => 2 * 100 => 200
        if 100 in int_arr:
            return int_arr[0] * int_arr[1]
        # otherwise, return the two numbers added together
        # example: ['forty', 'two'] => 42
        else:
            return int_arr[0] + int_arr[1]
    else: # return that number if a list of length one is passed in
        return int_arr[0]

# converts text to integers
def ascii2int(ascii_str):
    ascii_arr = ascii_str.strip().split()  # strip extra spaces and split sentence into words
    ascii_arr_clean = [i for i in ascii_arr if i in numbers_list] # remove words any words not in the numbers_list, for example "and"
    
    # detect if the word "thousand" is in the input string
    thousands_index = ascii_arr_clean.index('thousand') if 'thousand' in ascii_arr_clean else -1
    sum = 0 # value of the number that will be returned

    if len(ascii_arr_clean) == 1: # if the number is just one word, return the corresponding number
        return numbers_list[ascii_arr_clean[0]]
    else: # if the number has more than one word, feed it into the convert_word_to_int function
        
        # if the number does have a thousands, then get the thousands multiplier
        # for example ["four", "hundred", "thousand"] will return 400 which will be multiplied by 1000
        # hundreds and less are processed belwo
        if thousands_index > -1:
            thousand_multiplier = convert_word_to_int(ascii_arr_clean[0:thousands_index])
            print(thousand_multiplier)
            sum += thousand_multiplier * 1000
        
        # if the string has thousands, calculate hundreds alone by omitting the thousands place
        if thousands_index > -1 and thousands_index != len(ascii_arr_clean)-1:
            hundreds = convert_word_to_int(ascii_arr_clean[thousands_index+1:])
        # process hundreds alone
        elif thousands_index == -1:
            hundreds = convert_word_to_int(ascii_arr_clean)
        else:
            hundreds = 0
        sum += hundreds
    return sum

# Driver code, with test cases
a = "one hundred"
b = "four hundred"
c = "five hundred and twenty one"
d = "two"
e = "forty"
f = "five hundred and twelve"
g = "six hundred and one"
h = "four hundred forty two"
i = "four thousand four hundred and twelve"
j = "four thousand four hundred and twenty one"
k = "forty thousand four hundred and twenty one"
l = "four hundred and twenty thousand four hundred and twenty one"
print(ascii2int(l))