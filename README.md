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

## Chapter 2: Basics of UNIX commands
`hightemp.txt` is a file that stores the record of the highest temperature in Japan in tab-delimited format of "prefecture" "point" "℃" "day". Create a program to perform the following processing and execute hightemp.txt as an input file. Furthermore, execute the same process with the UNIX command and check the execution result of the program.

### 10. Count the number of rows
Count the number of rows. Use the wc command to confirm results.

### 11. Replace tabs with spaces
Replace one tab space with one space. To confirm, use sed command, tr command, or expand command.

### 12. Save column 1 to col1.txt and column 2 to col2.txt
Save only the first column of each row to col1.txt, and extract only the second column as col2.txt in a file. To check, use the cut command.

### 13. Merge col1.txt and col2.txt
Merge col1.txt and col2.txt created in the "12" and create a text file in which the first and second columns of the original file are arranged in tab separator. Use the paste command for confirmation.

### 14. Output N rows from the beginning
Receive the natural number N by means such as command line argument and display only the first N lines of the input. Use the head command for confirmation.

### 15. Output the last N rows
Receive the natural number N by means such as command line argument and display only the last N lines of the input. Use the tail command for confirmation.

### 16. Divide the file into N
Receive the natural number N by means such as command line argument and divide the input file into N by row. Realize the same processing with the split command.

### 17. Different character strings in the first column
Find the type of string (string of different strings) in the first column. To confirm, use sort, uniq command.

### 18. Sort each row by descending numerical value of column 3
Arrange each line in the reverse order of the third column number (note: sort the contents of each line without changing it). Use the sort command for confirmation (this problem does not have to match the result when executed with command).

### 19. Find frequency of occurrence of character strings in the first column of each line and arrange them in descending order of appearance frequency
Find the appearance frequencies of character strings in the first column of each line, and arrange them in descending order of their appearance. To check, use cut, uniq, sort command.

# ToDo
- [ ] Translate texts in the exercises
