#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    min_word_len = float('inf')

    # List of punctuation marks
    punct_marks = [' ', ',', '-', ';', ':', '?', '!', '.']
    counter = 0

    user_str = str(input("Enter your sentence: "))
    str_list = list(user_str)

    # Loop through all characters of the input string
    for i in range(len(str_list)):

        # Checking if a symbol is a punctuation mark
        if str_list[i] in punct_marks:
            word_len = counter
            counter = 0

            # Determine the minimum length of a word
            if  0 < word_len < min_word_len:
                min_word_len = word_len
        else:
            counter += 1

    # Checking the last word, in case of a forgotten dot at the end
    word_len = counter
    if 0 < word_len <  min_word_len:
        min_word_len = word_len

    print(min_word_len)