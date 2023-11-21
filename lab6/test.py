import common
import random
import student_code

def generate_Board(n, no_of_rivals):
    arr = [[0 for i in range(n)] for j in range(n)]
    row = random.randrange(n)
    col = random.randrange(n)

    while arr[row][col] != 0:
       row = random.randrange(n)
       col = random.randrange(n)

    arr[row][col] = 1

    while arr[row][col] != 0:
       row = random.randrange(n)
       col = random.randrange(n)

    arr[row][col] = 2

    for i in range(no_of_rivals):
        while arr[row][col] != 0:
            row = random.randrange(n)
            col = random.randrange(n)
        arr[row][col] = 3       
    return arr 

def update_board(old_board, new_board):
    for i in range(len(old_board)):
        for j in range(len(old_board[i])):
            old_board[i][j] = round(new_board[i][j],2)

def run_test():
    delivery_fee = random.randrange(1,1000)
    battery_cost = random.randrange(1,100)
    repair_cost = random.randrange(1,1000)
    discount = round(random.random(),2)
    board = generate_Board(6,3)
    oldvalue = [[0 for i in range(6)] for j in range(6)]
    policies = [[0 for i in range(6)] for j in range(6)]
    student_code.print_2D_array(board)
    print("delivery_fee: ",delivery_fee,"battery_cost: ",battery_cost,"repair_cost: ",repair_cost,"discount: ",discount)
    student_code.drone_flight_planner(board,oldvalue,policies,delivery_fee,repair_cost,battery_cost,discount)
count = 0
while count < 20:
    run_test()
    count= count+1    