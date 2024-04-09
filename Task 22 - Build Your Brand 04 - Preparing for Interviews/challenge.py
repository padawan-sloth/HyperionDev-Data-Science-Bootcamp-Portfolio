# Add a prefix to a word

def add_prefix_un(word):
    return "un" + word

# Add prefixes to word groups

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return ' :: '.join([prefix] + [prefix + word for word in vocab_words[1:]])

# Remove a suffix from a word

def remove_suffix_ness(word):
    root = word[:-4]
    if root.endswith('i'):
        root = root[:-1] + 'y'
    return root

# Extract and transform a word

def adjective_to_verb(sentence, index):
    words = sentence.strip('.').split()
    adjective = words[index]
    return adjective + 'en'
