from os import system
from _thread import *

def caller(filename):
    print('launching')
    system('python '+filename)

def call(cmd):
    if cmd=="attt":
        start_new_thread(caller,('angry_tictactoe.py',))
    elif cmd=='dab':
        start_new_thread(caller,('dots_and_boxes.py',))
    elif cmd=='pm':
        start_new_thread(caller,('pacman.py',))
    elif cmd=='s':
        start_new_thread(caller,('SNAKES.py',))
    elif cmd=='sdk':
        start_new_thread(caller,('sudoku.py',))
    elif cmd=='tt':
        start_new_thread(caller,('tank_maze.py',))
    elif cmd=='t':
        start_new_thread(caller,('Tanks.py',))
    else:
        pass