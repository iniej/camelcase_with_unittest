
def camel_case(sentence):

# word = input('Enter a sentence ')
    accumulator = ""

    word_list = sentence.split()
    for x in range(len( word_list)):
        if x == 0:
            firstword = word_list[x].lower()
            accumulator = accumulator + firstword

        else:
            other_words = word_list[x]
            if other_words[0].isdigit():
                print('Wrong variable name.')
            else:
                first_letter = other_words[0].upper()
                other_letters = other_words[1:].lower()
                the_word = first_letter + other_letters

                accumulator = accumulator + the_word
    return accumulator


def main():
    sentence = input('Enter a sentence ')
    camelcased = camel_case(sentence)
    print(camelcased)
if __name__ == '_main_':
     main()
