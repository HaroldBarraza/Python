import random
def main():
    print(make_sentense(1, "past"))
    print(make_sentense(1, "present"))
    print(make_sentense(1, "future"))
    print(make_sentense(2, "past"))
    print(make_sentense(2, "present"))
    print(make_sentense(2, "future"))
#=====================================================================================================
def make_sentense(quantity, tense):
    word = get_determinate(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    phrase = get_prepositional_phrase(quantity)
    sentense = sentense = (f"{word} {noun} {verb} {phrase}.")
    return sentense.capitalize()
#=====================================================================================================
def get_determinate(quantity):
    if quantity == 1:
        words = ("a", "an", "the")
    else:
        words = ("some", "many", "the")
    word = random.choice(words)
    return word
#=====================================================================================================
def get_noun(quantity):
    if quantity == 1:
        nouns = ("bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman")
    else:
        nouns = ("birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women")
    noun = random.choice(nouns)
    return noun
#=====================================================================================================
def get_verb(quantity, tense):
    if tense == "past":
        verbs = ("drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote")
    elif tense == "present" and quantity == 1:
        verbs = ("drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes")
    elif tense == "present" and quantity != 1:
        verbs = ("drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write")
    elif tense == "future":
        verbs = ("will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write")
    verb = random.choice(verbs) 
    return verb
#=====================================================================================================
def get_preposition():
    preposition = ("about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without")
    prepositions = random.choice(preposition)
    return prepositions
#=====================================================================================================
def get_prepositional_phrase(quantity):
    if quantity == 1:
        prepositions_2 = get_preposition()
        word_2 = get_determinate(quantity)
        noun_2 = get_noun(quantity)
        phrase = prepositions_2 + " " + word_2 + " " + noun_2
        return phrase
    else:
        phrase = " "
        return phrase
main()




