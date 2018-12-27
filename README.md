100 Natural Language Processing(NLP) exercises with python
====

A Japanese professor in the Tohoku University provides 100 practical exercises to get used to programming, data analysis, NLP and so forth.

Ref: http://www.cl.ecei.tohoku.ac.jp/nlp100/

# Description
This repo intends to put the answers of the exercises with test codes.

# Test Environment
- MacOS High Sierra v10.13.6
- Python 3.6.5

# Index of exercises
## Chapter 1: Warming Up
You can review somewhat advanced topics in the programming language while working on subjects handling texts and strings.

- Keywords: string, unicode, list type, dictionary type, aggregate type, iterator, slice, random number

### 00. Reverse order of string
Get the string which characters of the "stressed" are arranged in reverse (from the end to the beginning).

### 01.「パタトクカシーー」 (Patatokakushi)
Retrieve the 1st, 3rd, 5th and 7th characters of the string "パタトクカシーー" and get the concatenated character string.

### 02.「パトカー」＋「タクシー」=「パタトクカシーー」
Connect the characters "パトカー" + "タクシー" alternately from the beginning to obtain the string "パタトクカシーー".

### 03. Pi
Please break the sentence "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics." into words and create a list of which the number of characters of each word is arranged in order of appearance.

### 04. Element symbol
Please break the sentence "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can." into words. Get the first character of 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th in the words. Get the first and second character of the other words. Create an associative array (dictionary type or map type) from the extracted characters, which contains the position of the word (The number of words from the beginning).

### 05. n-gram
Create a function that creates an n-gram from a given sequence (string, list, etc.). Using this function, obtain the word bi-gram and the character bi-gram from the sentence "I am an NLPer".

### 06. Set
Find sets of character bi-grams included in "paraparaparadise" and "paragraph" as X and Y respectively, and find the union, intersection, and difference set of X and Y. Also check if the bi-gram 'se' is included in X and Y.

### 07. Sentence generation by template
Implement a function that accepts the arguments x, y, z and returns the string "y is z at x o'clock". Furthermore, let x = 12, y = "temperature", z = 22.4 and confirm the execution result.

### 08. Cipher text
Implement a function "cipher" which converts each character of a given character string with the following specifications.

- Replace only lowercase letters with (219 - character code)
- Other characters are output as they are

Encrypt and decrypt English messages by using this function.

### 09. Typoglycemia
Create a program that performs the followings for word strings separated by spaces.
- Leave the beginning and end letters of each word
- Rearrange randomly the rest of the letters

However, words whose length is 4 or less are not rearranged. Give an appropriate English sentence (eg "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .") and confirm the execution result.

# ToDo
- [ ] Translate texts in the exercises
