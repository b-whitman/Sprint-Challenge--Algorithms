'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    count = 0
    # Base case: cease recursion when function is passed an empty string
    if len(word) == 0:
        return 0
    count += count_th(word[1:])
    if word[:2] == 'th':
        count += 1
    return count

print(count_th('athletics'))
    
