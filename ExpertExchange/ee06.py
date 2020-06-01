"""
https://www.experts-exchange.com/questions/29183890/TypeError-'dict-keys'-object-is-not-subscriptable-Python-3.html?anchor=a43096784&notificationFollowed=252746306#a43096784
"""

import random
from urllib.request import urlopen
import sys

WORDURL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == 'English':
    PHRASE_FIRST = True

# load up the words from website
for word in urlopen(WORDURL).readlines():
    WORDS.append(word.strip().decode("utf-8"))


def convert(snippet, phrase):
    # class_names = [w.capitalize for w in
    #              random.sample(WORDS, snippet.count("%%%"))]
    class_names = []
    for w in random.sample(WORDS, snippet.count("%%%")):
        class_names.append(w.capitalize)
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    print(snippet, phrase)
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", str(word), 1)

        # fake otehr names
        for word in other_names:
            result = result.replace("***", str(word), 1)

        # fake parameter names
        for word in param_names:
            result = result.replace("@@@", str(word), 1)

        results.append(result)
    return results


# keep going until they hit Ctrl-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            tmp = convert(snippet, phrase)
            question = tmp[0]
            answer = tmp[1]
            if PHRASE_FIRST:
                question, answer = answer, question

            input(">")
            print("Answer %s\n\n:" % answer)
except EOFError:
    print("\nbye")

