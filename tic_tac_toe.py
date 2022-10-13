

def print_board(first, second):

    one = 'X' if first[0] else ('0' if second[0] else '1')
    two = 'X' if first[1] else ('0' if second[1] else '2')
    three = 'X' if first[2] else ('0' if second[2] else '3')
    four = 'X' if first[3] else ('0' if second[3] else '4')
    five = 'X' if first[4] else ('0' if second[4] else '5')
    six = 'X' if first[5] else ('0' if second[5] else '6')
    seven = 'X' if first[6] else ('0' if second[6] else '7')
    eight = 'X' if first[7] else ('0' if second[7] else '8')
    nine = 'X' if first[8] else ('0' if second[8] else '9')

    print(f"{one}    {two}   {three}")
    print(f"{four}    {five}   {six}")
    print(f"{seven}    {eight}   {nine}")

def winner(first, second):

    winner_set = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for set in winner_set:
        if first[0] + first[1] + first[2] == 3:
            print("Winner is 'X'")
            return 1
        elif second[0] + second[1] + second[2] == 3:
            print("Winner is '0'")
            return 2
    return -1


if __name__ == "__main__":
    first = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    second = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print_board(first, second)
    palo = 1  # for x turn
    
    while(True):
                
        if palo:
            position = int(input("Enter a postion for 'X': "))
            first[position-1] = 1
            print_board(first, second)
        else:
            position = int(input("Enter a position for '0': "))
            # position = random.randint(0,9)
            second[position-1] = 1
            print_board(first, second)
        
        check = winner(first, second)
        if check != -1:
            print("match over")
            break
        palo = 1 - palo
