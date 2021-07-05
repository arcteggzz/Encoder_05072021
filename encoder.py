"""
This code asks the user for his or her name,
And generates an encoded output based on the length of the name.
"""
def main():
    confirmed_word = string_checker()
    print (confirmed_word)

def string_checker():
    while True:
        if is_valid_word(user_word):
            return user_word #function ends automatically once we hit return
        print ("Strings are not allowed")
            
def is_valid_word(user_word):
    """
    This function takes in the user's input.
    Then checks if the input is valid.
    For an Input to be valid, it must contain only letters (numbers,space,punctuations are not allowed)
    It then returns True or False
    """
    #adding not() to the line reverses the boolean(true or false)
    #the line "any(char.isdigit() for char in user_word) generates a true or false"
    return not(any(char.isdigit() for char in user_word))
    

if __name__ == '__main__':
    main()