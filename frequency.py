import re
import string 
import sys

from colorama import init, Fore, Back, Style        # pip install colorama
init()                                              # initialize colorama

document = open('input.txt', 'r')                   # input file to read from
output = open('results.txt', 'w')                   # output file to print results to
text = document.read()                              # read contents of input file
match_pattern = re.findall(r'\b[A-Z0-9]+\b', text)  # get all words, ignoring hyphens
document.close()                                    # close input file

# Variables needed for analysis
words = {}       # list of words from input
chars = {}       # list of chars from each word
word_count = 0   # total num of words in input
char_count = 0   # total num of chars in input
max_freq = 0     # keeps track of highest frequency
sec_max = 0      # keeps track of 2nd highest frequency
min_freq = 1000  # keeps track of lowest frequency

# Getting the frequencies of each word and char
for word in match_pattern:  
    words[word] = words.get(word, 0) + 1
    word_count = word_count + words[word]
    for key in word: 
        chars[key] = chars.get(key, 0) + 1
        char_count = char_count + 1

# Outputting the words
output.write("\n  (Word, Frequency):\n")
i = 0
for x in words:
    if i == 0:
        output.write("  ")
    if i == 10:
        output.write("\n  ")
        i = 0
    output.write("(" + str(x) + ", " + str(words[x]) + ") ")
    i = i + 1
output.write("\n  " + str(word_count) + " Words in total\n")

# Getting the most frequent and least frequent chars
for c in sorted(chars):
    if chars[c] > max_freq: 
        max_freq = chars[c]
    elif chars[c] < min_freq:
        min_freq = chars[c]

# Getting the second most frequent char
for c in chars:
    if chars[c] > sec_max and chars[c] < max_freq:
        sec_max = chars[c]

# Outputting the chars and their frequencies
output.write("\n  Chars : Frequency\n")
print(Fore.MAGENTA + ' Chars  : Frequency')        
for x in sorted(chars):
    if chars[x] == max_freq:
        print(Fore.GREEN + '    ' + str(x) + '   :   ' + str(chars[x]) + '   (HIGHEST FREQUENCY)')
    elif chars[x] == sec_max:
        print(Fore.CYAN + '    ' + str(x) + '   :   ' + str(chars[x]) + '   (SECOND HIGHEST FREQUENCY)')
    elif chars[x] == min_freq:
        print(Fore.RED + '    ' + str(x) + '   :   ' + str(chars[x]) + '    (LOWEST FREQUENCY)')
    else:
        print(Fore.WHITE + '    ' + str(x) + '   :   ' + str(chars[x]))
    output.write("    " + str(x) + "   :    " + str(chars[x]) + "\n")

output.write("\n  " + str(char_count) + " Chars in total")
output.close()
