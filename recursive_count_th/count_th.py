'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    print(word)
    if 'th' not in word:
        return 0
    word = word.split("th", 1)
    return 1 + count_th(word[1])
