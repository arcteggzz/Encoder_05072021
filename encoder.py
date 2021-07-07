"""
This code asks the user for his or her name,
And generates an encoded output based on the length of the name.
"""
import string

def main():
    alphabet_list = list(string.ascii_lowercase)
    confirmed_word = string_checker()
    print (confirmed_word)
    coded_word_list = []
    for  ch in confirmed_word:
        ch_i = alphabet_list.index(ch)
        new_ch_i = get_new_index(ch_i)
        new_letter = alphabet_list[new_ch_i]
        coded_word_list.append(new_letter)
    final_string = string_from_list(coded_word_list)
    print (coded_word_list)
    print (final_string)


def string_from_list(new_letter):
    """
    This function creates a string from a list passed into it,
    element after element.
    The list can contain letters or numbers as it's elements.
    """
    final_string = ""
    for x in new_letter:
        final_string += x
    return final_string

def get_new_index(ch_i):
    new_ch_i = ch_i + 5
    if new_ch_i <= 25:
        return new_ch_i
    else:
        new_ch_i = new_ch_i - 26
        return new_ch_i

def string_checker():
    while True:
        user_word = input("Type your word: ")
        user_word = user_word.lower()      
        if is_valid_word(user_word):
            return user_word #function ends automatically once we hit return
        print ("Numbers are not allowed")
            
def is_valid_word(user_word):
    """
    This function takes in the user's input.
    Then checks if the input is valid.
    For an Input to be valid, it must contain only letters (numbers,space,punctuations
    are not allowed)
    It then returns True or False
    """
    #adding not() to the line reverses the boolean(true or false)
    #the line "any(char.isdigit() for char in user_word) generates a true or false"
    return not(any(char.isdigit() for char in user_word))
    

if __name__ == '__main__':
    main()