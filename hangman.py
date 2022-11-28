# Problem Set 2, hangman.py
# Name: Danylo Voychenko 
# Collaborators: -
# Time spent: +-5h

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import re
WORDLIST_FILENAME = "words.txt"
rules= """ Rules:
1.The user starts with 3 warnings.
2. If the user inputs anything besides an alphabet (symbols, numbers), tell the
user that they can only input an alphabet.
  a. If the user has one or more warning left, the user should lose one
warning. Tell the user the number of remaining warnings.
  b. If the user has no remaining warnings, they should lose one guess.
3. If the user inputs a letter that has already been guessed, print a message
telling the user the letter has already been guessed before.
  a. If the user has one or more warning left, the user should lose one
warning. Tell the user the number of remaining warnings.
  b. If the user has no warnings, they should lose one guess.
4. If the user inputs a letter that hasn’t been guessed before and the letter is in
the secret word, the user loses no​ guesses.
5. Consonants:​ If the user inputs a consonant that hasn’t been guessed and the
consonant is not in the secret word, the user loses one​ guess if it’s a
consonant.
6. Vowels:​ If the vowel hasn’t been guessed and the vowel is not in the secret
word, the user loses two​ guesses. Vowels are a, e, i, o, and u. y does not
count as a vowel.
 """

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    return set(letters_guessed) >= set(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word = list(secret_word)
    for i in range(len(secret_word)): 
      if secret_word[i] in letters_guessed:
        pass
      else:
        secret_word[i]='_ '
    return ''.join(secret_word)




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = set(string.ascii_lowercase)
    letters_guessed = set(letters_guessed)
    result = list(alphabet ^ letters_guessed)
    result.sort()
    return ''.join(result)

def get_good_input(letter, letters_guessed):
    
    if letter in letters_guessed and str.isalpha(letter):
      return "Oops! You've already guessed that letter."
    elif letter == '?':
      return 0  
    elif str.isalpha(letter) and len(letter)==1:
      return True 
    else:
      return 'Oops! That is not a valid letter.'  

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = [] 
    guesses_remaining = 6
    warnings_remaining = 3

    print('Welcome to the game Hangman!')
    print(rules)
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warnings_remaining} warnings left.')
    print(secret_word)
    while not is_word_guessed(secret_word, letters_guessed):
      print('-------------')
      if guesses_remaining <= 0:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
        break

      print(f'You have {guesses_remaining} guesses left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')
      letter = input('Please guess a letter: ')

      if get_good_input(letter, letters_guessed) == True:
        letters_guessed.append(letter)
        if letter in set(secret_word):
          print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
        else:
          
          if letter in set('aeiou'):
            guesses_remaining -=  2
          else:
            guesses_remaining -=  1
          print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
      elif get_good_input_hint(letter, letters_guessed) == 0:
        print(rules)
      else:
        warnings_remaining -=  1
        if warnings_remaining >= 0:
          print(f'{get_good_input(letter, letters_guessed)} You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
        else:
          print(f'{get_good_input(letter, letters_guessed)} You have no warnings left')
          print(f'so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}')
          guesses_remaining -=  1
        pass
          
    if is_word_guessed(secret_word, letters_guessed):
      print('-------------')
      print(f'Congratulations, you won! Your total score for this game is: {len(set(secret_word))*guesses_remaining}')



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if other_word in list((show_possible_matches(my_word)).split()):
      return True
    else:
      return False  
    


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    my_word = my_word.split(' ')
    my_word = ''.join(my_word)
    point_without = set(my_word) ^ set('_')
    point_without = ''.join(point_without)
    pattern = ''
    
    for i in range(len(my_word)):
      if my_word[i] == '_':
        pattern += f"[^{point_without} ]"
      else:
        pattern += my_word[i]
    
    pattern = r'\b(' + pattern + r')\b' 
    pattern = re.compile(pattern)
    matches = ' '.join(pattern.findall(' '.join(wordlist)))
    if matches == []:
      return 'No matches found'
    else:  
      return ' '.join(pattern.findall(' '.join(wordlist)))
    

def get_good_input_hint(letter, letters_guessed):
    if letter == '*':
      return "hint"
    elif letter == '?':
      return 0
    elif letter in letters_guessed and str.isalpha(letter)==True:
      return "Oops! You've already guessed that letter."
    elif str.isalpha(letter) and len(letter)==1:
      return True 
    else:
      return 'Oops! That is not a valid letter.'  



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = [] 
    guesses_remaining = 6
    warnings_remaining = 3

    print('Welcome to the game Hangman!')
    
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warnings_remaining} warnings left.')

    while not is_word_guessed(secret_word, letters_guessed):
      print('-------------')
      if guesses_remaining <= 0:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
        break

      print(f'You have {guesses_remaining} guesses left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')
      letter = input('Please guess a letter: ')

      if get_good_input_hint(letter, letters_guessed) == True:
        letters_guessed.append(letter)
        if letter in set(secret_word):
          print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
        else:
          if letter in set('aeiou'):
            guesses_remaining -=  2
          else:
            guesses_remaining -=  1
          print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
      elif get_good_input_hint(letter, letters_guessed) == "hint":
        if set(get_guessed_word(secret_word, letters_guessed)) == set('_'):
          f'It gonna be every {len(secret_word)} letter word in list :)'
        else:
          print(f'Possible word matches are: {show_possible_matches(get_guessed_word(secret_word, letters_guessed))}')
      elif get_good_input_hint(letter, letters_guessed) == 0:
        print(rules)
      else:
        warnings_remaining -=  1
        if warnings_remaining >= 0:
          print(f'{get_good_input_hint(letter, letters_guessed)} You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
        else:
          print(f'{get_good_input_hint(letter, letters_guessed)} You have no warnings left')
          print(f'so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}')
          guesses_remaining -=  1
        pass
          
    if is_word_guessed(secret_word, letters_guessed):
      print('-------------')
      print(f'Congratulations, you won! Your total score for this game is: {len(set(secret_word))*guesses_remaining}')
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
