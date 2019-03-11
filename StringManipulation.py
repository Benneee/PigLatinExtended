# Algorithm for StringManipulation

# Declare variables to hold "ay", "way", user's input and an array of vowels

# First if statement:
## conditions to check if user's entry is valid - is it greater than 0 and is it alphabet

# Convert the user's entry to lowercase

# Run a for loop and state a nested if statement t append the vowels into an array new_list

# Also, save the index of the vowels

## Next if:
### check if the index of vowel in word is 0,
### slice from the second positioned character of the string to the length of the word and save to the variable: the_word
### append the_word to first and pig

## the elif statement
### index of the vowel is greater than 0
### slice from the first character of string to the index and save to the variable pre_vowel
### slice from the index to the length of the word and save the characters to the variable "the_word"
### new_word holds the new word formed


# when there is no vowel in the string entered by user
## print the string entered by the user back to the user

# Run through the restart scenario
## If user enters the string "done", user is allowed to exit the program.


def main():
    print("Welcome to StringManipulation")

    users_input = input("Kindly enter a word: ")

    pyg = "ay"

    pig = "way"

    vowels = ['a', 'e', 'i', 'o', 'u']

    original = users_input

    if (len(original) > 0) and (original.isalpha()):
        word = original.lower()
        new_list = []
        for el in word:
            if el in vowels:
                new_list.append(el)
                index = word.index(el)
                if (index == 0):
                    first = word[0]
                    the_word = word[1: len(word)]
                    new_word = the_word + first + pig
                    print(new_word)
                elif(index > 0):
                    pre_vowel = word[0 : index]
                    the_word = word[index : len(word)]
                    new_word = the_word + pre_vowel + pyg
                    print(new_word)
                    break
            elif el not in vowels:
                index = word.rindex(el)
                print(original)
    else:
        print(original)
    restart = input("enter the word 'done' if you do not wish to continue: ")
    if restart == 'done':
        exit()
    else:
        main()

main()


