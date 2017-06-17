# https://www.interviewcake.com/question/python/shuffle?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email
import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling+1)

def shuffle(the_list):

    if len(the_list) <= 1:
        return the_list

    last_index = len(the_list)-1
    for choosen_index in xrange(len(the_list)-1):
        random_index = get_random(choosen_index, last_index)

        if random_index != choosen_index:
            the_list[choosen_index], the_list[random_index] = \
            the_list[random_index], the_list[choosen_index]


the_list = [1,2,3,4,5,6,7]
shuffle(the_list)
print the_list