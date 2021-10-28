# Task
# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format

# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .

# Output Format

# Print the result of .

if __name__ == '__main__':
    N = int(input())
    i = 0
    l = []
    s = 0
    while i < N:
        enter = input()
        e = list(enter)
        if e[0] == 'i':
            try:
                l.insert(int(e[7]), int(e[-2:][0])*10+int(e[-2:][1]))
            except:
                l.insert(int(e[7]), int(e[-2:][1]))
        elif e[0] == 'p':
            if e[1] == 'r':
                print(l)
            else:
                l.pop()
        elif e[0] == 'a':
            try:
                l.append(int(e[-2:][0])*10+int(e[-2:][1]))
            except:
                l.append(int(e[-2:][1]))
        elif e[0] == 's':
            l.sort()
        elif e[0] == 'r':
            if e[2] == 'm':
                try:
                    l.remove(int(e[-2:][0])*10+int(e[-2:][1]))
                except:
                    l.remove(int(e[-2:][1]))
            else:
                l.reverse()
        i = i+1
