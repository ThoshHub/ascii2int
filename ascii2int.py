import sys

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
    'billion': 1000000000
}

'''
The following method converts an array of number words into an integer,
input: a list of number words, for example ["five", "hundred"]
output: a single integer, for example 500
This method is limited to generating numbers below one thousand
'''
def convert_word_to_int(ascii_arr_clean):
    # replace string with number representation
    # for example ['four', 'hundred', 'ten'] becomes [4, 100, 10]
    int_arr = [numbers_list[number_word] for number_word in ascii_arr_clean]
    
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

    # Check if the input is a string
    if type(ascii_str) is not str:
        raise ValueError("The current input is not a string, please input a string!")

    # Replace hyphens and transform input to lowercase
    ascii_str = ascii_str.replace('-', ' ')
    ascii_str = ascii_str.lower()

    ascii_arr = ascii_str.strip().split()  # strip extra spaces and split sentence into words
    ascii_arr_clean = [i for i in ascii_arr if i in numbers_list] # remove words any words not in the numbers_list, for example "and"
    
    # Raise an error if no valid words were found, valid meaning they are in numbers_list
    if len(ascii_arr_clean) == 0: raise ValueError("There were no valid number words found!") 

    # Raise an error if user enters million,billion, our thousand more than once
    if ascii_arr_clean.count('thousand') > 1 or ascii_arr_clean.count('million') > 1 or ascii_arr_clean.count('billion') > 1:
        raise ValueError("You entered a redundant word! Please check your input string.")

    # detect if the word "thousand", "million", or "billion" is in the input string
    billions_index = ascii_arr_clean.index('billion') if 'billion' in ascii_arr_clean else -1
    millions_index = ascii_arr_clean.index('million') if 'million' in ascii_arr_clean else -1
    thousands_index = ascii_arr_clean.index('thousand') if 'thousand' in ascii_arr_clean else -1
    
    sum = 0 # value of the number that will be returned

    if len(ascii_arr_clean) == 1: # if the number is just one word, return the corresponding number
        return numbers_list[ascii_arr_clean[0]]
    else: # if the number has more than one word, feed it into the convert_word_to_int function
        
        # if the number has a billions, then get the billions multiplier using everything preceding the billions_index
        # for example ["forty", "billion"] will return 40 which is multiplied by 1,000,000
        # millions places and less are processed below
        if billions_index > -1:
            billion_multiplier = convert_word_to_int(ascii_arr_clean[0:billions_index])
            sum += billion_multiplier * 1000000000

        # if the number has a millions, then get the millions multiplier using everything preceding the millions_index
        # for example ["four", "million"] will return 4 which is multiplied by 1,000,000
        # thousands places and less are processed below
        if millions_index > -1:
            if billions_index > -1:
                # if there is a billions place, then process numbers between billions place and millions place
                million_multiplier = convert_word_to_int(ascii_arr_clean[billions_index+1:millions_index])
            else:
                # otherwise, just process from the beginning of the list to the million splace
                million_multiplier = convert_word_to_int(ascii_arr_clean[0:millions_index])
            sum += million_multiplier * 1000000
            
        # if the number does have a thousands, then get the thousands multiplier using everything preceding the thousands_index
        # for example ["four", "hundred", "thousand"] will return 400 which will be multiplied by 1000
        # hundreds and less are processed below
        if thousands_index > -1:
            # if the string has a billions place, but not a millions place, then calculate everything between the billions and thousands place
            if billions_index > -1 and millions_index == -1:
                thousand_multiplier = convert_word_to_int(ascii_arr_clean[billions_index+1:thousands_index])
            # if there is a thousands place, then process numbers between millions place and thousands place
            elif millions_index > -1:
                thousand_multiplier = convert_word_to_int(ascii_arr_clean[millions_index+1:thousands_index])
            # otherwise, just process from the beginning of the list to the thousands place
            else:
                thousand_multiplier = convert_word_to_int(ascii_arr_clean[0:thousands_index])
            sum += thousand_multiplier * 1000

        if(ascii_arr_clean[-1] != 'thousand' and ascii_arr_clean[-1] != 'million' and ascii_arr_clean[-1] != 'billion'):
            # if the string has thousands, calculate hundreds alone by omitting the thousands place
            if thousands_index > -1 and thousands_index != len(ascii_arr_clean)-1:
                hundreds = convert_word_to_int(ascii_arr_clean[thousands_index+1:])
            # if the string has millions, calculate hundreds alone by omitting the millions place
            elif millions_index > -1 and millions_index != len(ascii_arr_clean)-1:
                hundreds = convert_word_to_int(ascii_arr_clean[millions_index+1:])
            # if the string has billions, calculate hundreds alone by omitting the billions place
            elif billions_index > -1 and billions_index != len(ascii_arr_clean)-1:
                hundreds = convert_word_to_int(ascii_arr_clean[billions_index+1:])
            # process hundreds alone
            elif thousands_index == -1 and millions_index == -1 and billions_index == -1:
                hundreds = convert_word_to_int(ascii_arr_clean)
            # no hundreds
            else:
                hundreds = 0
            sum += hundreds

    return sum

# Driver code, with default case
default_case = "one hundred"

def main():
    if(len(sys.argv) > 1):
        num = " ".join(sys.argv[1:])
    else:
        num = default_case
    print("Input: \n" + num + " \nOutput: \n" + str(ascii2int(num)))

if __name__ == "__main__":
    main()