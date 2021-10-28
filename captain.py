# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of  members per group where  ≠ .

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of  and the room number list.

# Input Format

# The first line consists of an integer, , the size of each group.
# The second line contains the unordered elements of the room number list.


# Constraints


# Output Format

# Output the Captain's room number.

if __name__ == '__main__':
    k = int(input())
    integer_list = map(int, input().split())
    l = list(integer_list)
    l.sort()

    for i in range(len(l)+1):
        if i % k == 0:
            try:
                if l[i] != l[i+1]:
                    print(l[i])
                    break
            except:
                print(l[i])
                break
