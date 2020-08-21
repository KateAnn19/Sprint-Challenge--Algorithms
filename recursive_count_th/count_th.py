'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word_len = len(word)
    sub_len = len('th')
    newWord = word
    count = 0
    #base case
    if word_len == 0:
        return 0
    
    if len(newWord) < sub_len or newWord == None:
        print(count_list)
        return count
    
    if word.find('th') != -1:
        index = word.find('th')
        count = 1
        newWord = word[index+2:]
        count += count_th(newWord)
        return count
    else:
        return count
