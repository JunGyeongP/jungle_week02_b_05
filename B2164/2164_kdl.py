import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

cards = deque([i for i in range(1, int(input())+1)])

while len(cards) > 1:
    cards.popleft()
    return_card = cards.popleft()
    cards.append(return_card)

print(cards[0])
