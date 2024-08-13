def upDown(n):
    line = ""

    for num in range(1, n, 2):
        line += '-'*((n*3-num*3)//2)
        line += ".|."*num
        line += '-'*((n*3-num*3)//2)
        print(line)
        line = ""

def downUp(n):
    line = ""

    for num in range(n-2, -1, -2):
        line += '-'*((n*3-num*3)//2)
        line += ".|."*num
        line += '-'*((n*3-num*3)//2)
        print(line)
        line = ""

def welcomeLine(n):
    line = ""
    line += '-'*((n*3-7)//2)
    line += "WELCOME"
    line += '-'*((n*3-7)//2)
    print(line)

if __name__ == '__main__':
    n = input()

    upDown(n)
    welcomeLine(n)
    downUp(n)