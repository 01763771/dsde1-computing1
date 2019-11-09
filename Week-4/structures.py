'''
structures.py

Simple functions performing operations on basic Python data structures.
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list".
def first_and_last(the_list):
    '''Returns the first and last value of the list.'''
    my_list = []
    my_list = my_list + [the_list[0]]
    my_list = my_list + [the_list[-1]]
    return my_list


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list".
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception.
def part_reverse(the_list, beginning, end):
    '''Returns part of a list given by paramenters in reverse.'''
    if end < beginning:
        raise ValueError
    else:
        my_list = the_list[beginning: end]
        my_list = my_list[::-1]
    return my_list # hint this is incomplete


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4].
def repeat_at_index(the_list, index):
    '''Inserts the the index value three times.'''
    for i in range(3):
        new_list = the_list+[index]
        new_list.sort()
    return new_list



# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    '''Checks whether the word is a pallindrome.'''
    word = word.lower()
    word1 = str(word)
    word2 = word[::-1]
    if word1 != word2:
        return False
    else:
        return True

    return

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not.
def palindrome_sentence(sentence):
    '''Checks whether the sentence is a pallindrome.'''
    a = sentence.lower().strip().replace(" ", "")
    b = a[::-1]
    if a == b:
        return True
    else:
        return False
    return

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence.
def concatenate_sentences(sentenece1, sentence2):
    '''Joins two sentences together.'''
    a = list(sentenece1.strip())
    b = list(sentence2.strip())

    condition_1_a = a[0].isupper
    if a[-1] == '.' or '?' or'!':
        condition_2_a = True
    else:
        condition_2_a = False
    if condition_1_a and condition_2_a == True:
        one = 'yes'
    else:
        one = 'no'
        raise ValueError

    condition_1_b = b[0].isupper
    if b[-1] == '.' or '?' or '!':
        condition_2_b = True
    else:
        condition_2_b = False
    if condition_1_b and condition_2_b == True:
        two = 'yes'
    else:
        two = 'no'
        raise ValueError

    return one+two

# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    '''Checks whether there is a record with given key in the dictionary.'''
    if key in dictionary:
        return True
    else:
        return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    '''Checks whether a given value is stored in the dictinary.'''
    if value in dictionary.values():
        return True
    else:
        return False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    '''Combines two dictionaries together.'''
    dict3 = {**dictionary1, **dictionary2}
    return dict3
