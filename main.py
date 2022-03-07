import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Morse_code"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

hrefs = []

rows = soup.find_all(name="tr")

for row in rows:
    hrefs.append((row.find('b')))

hrefs_without_none =[]

for href in hrefs:
    if href != None:
        hrefs_without_none.append(href)

alphabet = []

for i in range(2,54):
    alphabet.append(hrefs_without_none[i])



alphabet_letters = []
alphabet_symbols = []
alphabet_letters_upgrade = []

for i in range(len(alphabet)):
    if i%2 ==0 or i ==0:
        alphabet_letters.append(alphabet[i].getText())
    else:
        alphabet_symbols.append(alphabet[i])

for alpha_letter in alphabet_letters:
    alphabet_letters_upgrade.append(alpha_letter.split(',')[0])


users_input = input("Welcome to Mors'e code translator please put in the sentence you would like to translate")

words = users_input.split(' ')
sentence_morse = []
for word in words:
    word_letters = [char for char in word]
    word_morse = ""
    for letter in word_letters:
        index = alphabet_letters_upgrade.index(letter.upper())
        morse_symbol = alphabet_symbols[index].getText()
        word_morse += morse_symbol
    sentence_morse.append(word_morse.replace(u'\u200a', ' '))

print(f"your word in Morse alphabet is {sentence_morse}")




















