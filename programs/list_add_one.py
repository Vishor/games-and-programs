# Given a list of numbers that represent a integer, you have to add one.
# E.g. [1, 4, 9] = [1, 5, 0] You have to use arbitrary precision increment.

a = [1, 4, 9]
b = [9, 9, 9]

#simple solution
s = "".join(map(str, a))
print(int(s)+1)

#recursive (arbitrary precision increment)
def plus_one_recursive(l, ind=-1):
    l[ind] += 1
    if abs(ind) == len(l) and l[ind] == 10:
        l[0] = 1
        l.append(0)
        return l
    elif abs(ind) == len(l) or l[ind] != 10:
        return l
    else:
        l[ind] = 0
        return plus_one_recursive(l, ind-1)

