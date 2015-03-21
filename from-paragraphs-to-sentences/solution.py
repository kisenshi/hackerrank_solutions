"""
Problem: From Paragraphs to Sentences (/from-paragraphs-to-sentences)
"""

import sys


SPACE = " "
END_SENTENCE = (".")
END_SENTENCE_SPECIAL = ("?", "!")
OPEN_BLOCK_CHARACTERS = ("(")
CLOSE_BLOCK_CHARACTERS = (")")
BLOCK_CHARACTERS = ('"', "'")
SPECIAL_BLOCK_CHARACTERS = ("'")

MAX_ABBREVIATION = 4

paragraph = ""


"""
The input in this problem is conformed by a paragraph formed by sentences that it is neede to analyse and chunk into sentences 
"""
def readInput():
    global paragraph

    s = sys.stdin
    paragraph = s.readline()

"""
Executes the code that converts the unique paragraph into sentences
"""
def main():
    readInput()

    paragraph_length = len(paragraph)

    in_block = [] #It will contain the block characters found in the way. As it is not possible to distinguish between them, they will be stacked and removed just when its pair is found again
    in_block_w_closure = 0 #It is possible to chain more than one of this kind of blocks so instead of having a boolean, we will have a counter that will be increased when a open block character is found and decreased when it is found the close one
    upper_case_word = False #Abbreviations will end with a . but they should not be considered as end of sentence so we need to keep a track of when a word started with upper case
    length_upper_case_word = 0 #We wont considered as abreviation those words with a lenght bigger than 4
    skip_next = False #After a new line is added, it will be needed to skip if there is a space

    new_text = ""
    
    i = 0
    while i < paragraph_length:
        character = paragraph[i]

        if skip_next:
            if character is SPACE:
                i += 1
                continue

        skip_next = False

        #It is checked the length of the word if it stil being considered an upper_case_word
        if upper_case_word:
            length_upper_case_word += 1
            if length_upper_case_word > MAX_ABBREVIATION:
                upper_case_word = False
                length_upper_case_word = 0

        #It is added the character to the text
        new_text += character 

        """ The action will depend on the kind of character that it is being considered """
        if character in SPECIAL_BLOCK_CHARACTERS:
            if character is "'":
                #If the previous character was a character and not space it is not a block character so we shouldn't do anything
                if paragraph[i - 1] is not " ":
                    i += 1
                    continue
        if character.isupper():
            #If is upper case, it could be an abbreviation so it is needed to save upper_case_word as true until a space has found and the word has finished
            upper_case_word = True
            length_upper_case_word += 1
        elif character is SPACE:
            #If there is a space we should stop tracking the upper_case_word to be able to split from now
            upper_case_word = False #No need to track the upper case anymore
            length_upper_case_word = 0
        elif character in BLOCK_CHARACTERS:
            #If it is empty it will be added
            if not in_block:
                in_block.append(character)
            else:
                #It is obtained the last item added to the stack to check if it is the same that it is being considered
                last_block_char = in_block.pop()
                if last_block_char is not character:
                    #It is another kind of block character, the previous one is added again to the list and the new one is added at the end as we will have two chained blocks that must be considered
                    in_block.append(last_block_char)
                    in_block.append(character)
        elif character in OPEN_BLOCK_CHARACTERS:
            #It is possible to chain more than one of this kind of blocks so instead of having a boolean, we will have a counter that is increased when a open block character is found
            in_block_w_closure += 1
        elif character in CLOSE_BLOCK_CHARACTERS:
            #It is possible to chain more than one of this kind of blocks so instead of having a boolean, we will have a counter that is decreased when a closure block character is found
            in_block_w_closure -= 1
        elif character in END_SENTENCE_SPECIAL and not in_block and not in_block_w_closure > 0:
            #If the character is not . it wont have to be considered the upper_case_word restriction so it is checked before
            new_text += "\n"
            skip_next = True #It will be skipped if there is a space
        elif character not in END_SENTENCE or upper_case_word or in_block or in_block_w_closure > 0:
            #It is added the character as it cannot be splitted
            i += 1
            continue
        else:
            #The sentence has finished, it should be added a new line
            new_text += "\n"
            skip_next = True #It will be skipped if there is a space

        i += 1

    print new_text

"""
Solution
"""

main()
