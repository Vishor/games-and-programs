words = ["super", "hot", "guacamole", "hot"]
words = set(words)
answer = []
from itertools import permutations

answer = [perm for perm in permutations(words)]
answer_list = []
for x in answer:
    answer_list.append(" ".join(list(x)))

print(answer_list)
