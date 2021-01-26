# The Game of Strings 
#
# Three Letters: M, I, U
# 
# Words: Any sequence of MIU
# Examples:     UIIIIIM
#               MUI
#               MMMIIIU
#               IUM
#
# Game Rules:
#
# Rule 1:   Any string that ends with I, can have U added to it.
#               MUI -> MUIU
# 
# Rule 2:   Any string Mx (where x is any string) can be replaced by Mxx. 
#
#               MUM -> MUMUM
#               MII -> MIIII
#               MUIMU -> MUIMUUIMU
# Rule 3:   Any III can be replaced by U
# 
#               MUIIIM -> MUUM
#               MIIIIM -> MUIM or MIUM
#
# Rule 4:   Any UU can be deleted 
#               MUUM -> M
#

#  Start : MUI -> MUIU (rule1) -> MUIUUIU (rule2) -> MUIIU (rule 4) 
#

def APPEND_U(x): # Rule 1
    if 'MUI' in x:
        x = 'MUIU'
    return x

assert APPEND_U('MUI') == 'MUIU'

def APPEND_x(x): # Rule 2
    new_string = []
    if x.endswith('I'):
        new_string.append(x + 'I') 
        x = new_string[0]
        print(x)
    return x

assert APPEND_x('MII') == 'MIII'

def solve(x):
    s_db = [ x ] 
    steps_taken = 0 
    while s_db:
        the_next_move_is = []
        steps_taken += 1 
        x = [x for x in s_db]
        

