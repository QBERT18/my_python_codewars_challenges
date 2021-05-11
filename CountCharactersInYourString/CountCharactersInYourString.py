def count(string):
    dictionary = {}
    for s in string:
        if s in dictionary:
            dictionary[s] += 1
        else:
            dictionary[s] = 1
    return dictionary
