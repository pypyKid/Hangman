import requests
from bs4 import BeautifulSoup
from random import choice

r = requests.get("https://www.vocabulary.com/lists/52473#view=list")
s = BeautifulSoup(r.text, "html.parser")
lst = s.find_all("a", attrs={"class": "word"})
words = choice(lst).text.strip()
out = "_" * len(words)
o2 = list(out)
print("".join(o2))
pics = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]
f = -1
while f != 6:
    g = input("Your guess: ")
    if g not in words:
        f += 1
        print(pics[f])
    elif words.count(g) == o2.count(g):
        f += 1
        print(pics[f])
    else:
        count = []
        for i in range(0, len(words)):
            if g == words[i]:
                count.append(i)
        for j in count:
            if o2[j] == g:
                continue
            else:
                o2[j] = g
                print("".join(o2))
                break

    if "".join(o2) == words:
        print("You won! :)")
        break
    elif f == 6:
        print("You lost! :(")
