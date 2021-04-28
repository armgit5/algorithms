# https://www.hackerrank.com/challenges/the-story-of-a-tree/problem

import os
import sys

#
# Complete the storyOfATree function below.
#
def storyOfATree(n, edges, k, guesses):
    #
    # Write your code here.
    #
    print(n, edges, k, guesses)

def input():
    return next(f)

with open('storyOfATree.txt') as f:
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        edges = []

        for _ in range(n-1):
            edges.append(list(map(int, input().rstrip().split())))

        gk = input().split()

        g = int(gk[0])

        k = int(gk[1])

        guesses = []

        for _ in range(q):
            guesses.append(list(map(int, input().rstrip().split())))

        result = storyOfATree(n, edges, k, guesses)

