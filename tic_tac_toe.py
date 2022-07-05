import keyboard  # using module keyboard
import random
import time
import create_dump_files
arr = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
turn = False
location = [[2,0],[2,1],[2,2],[1,0],[1,1],[1,2],[0,0],[0,1],[0,2]]
moves_map = [7,8,9,4,5,6,1,2,3]
move_history = []
option = ["X","O"]
starttime = time.time()
prev_keys_pressed = []
opponent_type = 0
# Check  if wins?
def check_if_wins(turn):
    #diagnols
    if (arr[0][0] == arr[1][1] == arr[2][2] == option[turn]) or (arr[0][2] == arr[1][1] == arr[2][0] == option[turn]):
        print("{} won!!!".format(option[turn]))
        return True
    #rows
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] == option[turn]:
            print("{} won!!!".format(option[turn]))
            return True
    #columns
    for i in range(3):
        if arr[0][i] == arr[1][i] == arr[2][i] == option[turn]:
            print("{} won!!!".format(option[turn]))
            return True
    return None

# Printing the matrix
def print_arr(arr):
    for i in arr:
        print(*i)
    print("")

# doing the move
def do(x,turn):
    move_history.append(x + 1)
    if turn != -1:
        position = location[x]
        if arr[position[0]][position[1]] == "-":
            arr[position[0]][position[1]] = option[turn]    
            return not turn
    return turn

#start
if __name__ == "__main__":
    # get dump file name
    dump_file_name = input("dump filename (main:1, default:Enter):\n->") 
    if dump_file_name == "":
        dump_file_name = "1"
    dump_file_name+=".txt"
    print_arr(arr)
    
    # Main loop       
    while True:
        try:
            x = None
            for i in range(1,10):
                if keyboard.is_pressed('{}'.format(i)):
                    if i not in prev_keys_pressed:
                        prev_keys_pressed.append(i)
                        print_arr_flag = 1
                        x = i
                    break
        except:
            break
        if x:
            if print_arr_flag:

                # player's move
                turn = do(x-1,turn)
                print_arr(arr)

                # check if any players win
                if check_if_wins(not turn):      
                    create_dump_files.write_dump_in(dump_file_name, option[not turn], move_history)          
                    move_history = []
                    break
                if "-" not in [i for ar in arr for i in ar]:
                    print("Tied up!!!")
                    create_dump_files.write_dump_in(dump_file_name, option[not turn], move_history)     
                    move_history = []
                    break
                
                # opponents's move
                choices = [j for j in range(9) if [i for ar in arr for i in ar][j] == '-']
                rand_move = moves_map[random.choice(choices)]
                turn = do(rand_move-1,turn)
                prev_keys_pressed.append(rand_move)
                print_arr(arr)


                # check if any players win
                if check_if_wins(not turn):
                    create_dump_files.write_dump_in(dump_file_name, option[not turn], move_history)     
                    move_history = []
                    break
                print_arr_flag = 0
                if "-" not in [i for ar in arr for i in ar]:
                    create_dump_files.write_dump_in(dump_file_name, option[not turn], move_history)     
                    print("Tied up!!!")
                    move_history = []
                    break

