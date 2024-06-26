import random
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    # Randomly choose and return a determiner.
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense=='past':
        verbs=["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense=='present':
        if quantity==1:
            verbs=["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs=["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense=='future':
        verbs=["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    else:
        raise ValueError('Invalid tense')
    return random.choice(verbs)

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
    quantity: an integer that determines if the
    determiner and noun in the prepositional
    phrase returned from this function should
    be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition=get_preposition()
    determiner=get_determiner(quantity)
    noun=get_noun(quantity)
    phrase=f"{preposition} {determiner} {noun}"
    return phrase

def get_adjective():
    adjectives=["attractive","beautiful","dazzling","fancy","muscular",
                "plump","shapely","short","skinny","ugly","unsightly"]
    return random.choice(adjectives)

def get_adverb():
    adverbs=["certainly","finally","besides","also","always",
                "usually","often","ever","seldom","generally","normally"]
    return random.choice(adverbs)

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner1=get_determiner(quantity)
    adjective1=get_adjective()
    noun1=get_noun(quantity)
    adverb=get_adverb()
    verb=get_verb(quantity, tense)
    preposition_phrase1=get_prepositional_phrase(quantity)
    determiner2=get_determiner(quantity)
    adjective2=get_adjective()
    noun2=get_noun(quantity)
    preposition_phrase2=get_prepositional_phrase(quantity)
    
    sentence=(f"{determiner1.capitalize()} {adjective1} {noun1} {preposition_phrase1} "
    f"{adverb} {verb} {determiner2} {adjective2} {noun2} {preposition_phrase2}.")
    return sentence
def main():
    sentences=[
        make_sentence(1, 'past'),
        make_sentence(1, 'present'),
        make_sentence(1, 'future'),
        make_sentence(2, 'past'),
        make_sentence(2, 'present'),
        make_sentence(2, 'future')]
    for sentence in sentences:
        print(sentence)
if __name__=="__main__":
    main()