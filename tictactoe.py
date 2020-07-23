cells = [' ' for _ in range(9)]
s = 0

def field(cells):
    print("-" * 9)
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("-" * 9)


x_o = 'X'

field(cells)

end1, end3 = False, True
while True:
    if s % 2 == 0:
        x_o = 'X'
    else:
        x_o = 'O'
    
    while end1 != True:
        end2 = False
        a = input("Enter the coordinates: > ").split()
        while end2 != True:
            if len(a) != 2:
                print("You should enter numbers!")
                break
            elif a[0].isdigit() is False or a[1].isdigit() is False:
                print("You should enter numbers!")
                break
            else:
                end3 = False
                break
        
        while end3 != True:
            x, y = [int(i) for i in a]
            if (x < 1 or x > 3) or (y < 1 or y > 3):
                print("Coordinates should be from 1 to 3!")
                break
            else:
                n = 8 - 3 * y + x
                if cells[n] == 'X' or cells[n] == 'O':
                    print("This cell is occupied! Choose another one!")
                    break
                else:
                    end1 = True
                    break
    n = 8 - 3 * y + x
    cells[n] = x_o
    field(cells)
    s += 1
    end1, end3 = False, True

    x_win = cells[0] == cells[1] == cells[2] == 'X' or cells[3] == cells[4] == cells[5] == 'X' or cells[6] == cells[
        7] == cells[8] == 'X'  # X win in lines

    x_win = x_win or cells[0] == cells[3] == cells[6] == 'X' or cells[1] == cells[4] == cells[7] == 'X' or cells[2] == \
            cells[5] == cells[8] == 'X'  # X win in columns

    x_win = x_win or cells[0] == cells[4] == cells[8] == 'X' or cells[2] == cells[4] == cells[
        6] == 'X'  # X win in diagonale

    o_win = cells[0] == cells[1] == cells[2] == 'O' or cells[3] == cells[4] == cells[5] == 'O' or cells[6] == cells[
        7] == cells[8] == 'O'  # O win in lines

    o_win = o_win or cells[0] == cells[3] == cells[6] == 'O' or cells[1] == cells[4] == cells[7] == 'O' or cells[2] == \
            cells[5] == cells[8] == 'O'  # O win in columns

    o_win = o_win or cells[0] == cells[4] == cells[8] == 'O' or cells[2] == cells[4] == cells[
        6] == 'O'  # O win in diagonale
    
    if x_win is True:
        print('X wins')
    elif o_win is True:
        print('O wins')
    elif o_win == x_win == False and (' ' not in cells and '_' not in cells):
        print('Draw')
    elif o_win == x_win == False and (' ' in cells or '_' in cells):
        continue
    break