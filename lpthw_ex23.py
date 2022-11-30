# Learning Python3 the Hard Way. Excercise 23. Strings, Bytes and Character Encoding.

# Download languages.txt
# https://learnpythonthehardway.org/python3/languages.txt

# Example:
# 'python3 lpthw_ex23.py utf-8 strict' Will use utf-8 encoding and return an error if it fails. 
# 'python3 lpthw_ex23.py big5 replace' Will use big5 encoding and replace errors with question marks.
#  
import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)