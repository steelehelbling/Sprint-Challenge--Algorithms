'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    th_num = 0
    if len(word) < 2 :
        return th_num
    if word[0] == "t" and word[1] == "h":
        th_num = 1
        
    new_pos = word[1:]
    th_num = th_num + count_th(new_pos)
    return th_num  


count_th("")
count_th("renjwlhththththljms")
count_th("sghnlkertbthtthththt")
count_th("slohttthhtht")
count_th("nalsgb;egkj5rthjthtthhthhthlnas")