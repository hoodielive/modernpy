# The Game of Strings
#
# Three Letters: M, I, U
#
# Words:   Any sequence of MIU
# Examples:   UIIIIIM
#             MUI
#             MMMIIIU
#             IUM
#
# Game Rules:
#
# Rule 1:  Any string that ends with I, can have U added to it.
#              MUI --> MUIU
#
# Rule 2:  Any string Mx  (where x is any string) can be
#          replaced by Mxx. x is the remainder of the string (whatever letters)
#
#           MUM --> MUMUM
#           MII --> MIIII
#           MUIMU -> MUIMUUIMU
#
# Rule 3:  Any III substring can be replaced by U
#
#            MUIIIM -> MUUM
#            MIIIIM  -> MUIM   or MIUM
#
# Rule 4:  Any UU substring can be deleted
#             MUUM -> MM
#
#    Start : MUI -> MUIU (rule 1) -> MUIUUIU (rule 2) -> MUIIU (rule 4) -> ...
#
# Challenge:  Can you rewrite "MI" as "MU" (using only the rules)
#
# Ponder: Try it on paper maybe.   Write a program to try and figure it out.
#
#  MI   ->  MIU  (rule 1)
#       or  MII  (rule 2)

def next_moves(s):
    '''
    Given a string from MIU, make a list of all possible next moves.
    '''
    moves = []
    if s.endswith('I'):
        moves.append(s+'U')     # Rule 1
    if s.startswith("M"):
        moves.append("M" + s[1:]*2)  # Rule 2
    # Rule 3 and 4
    for n in range(len(s)):
        if s[n:n+3] == 'III':    # Rule 3: Any III replaceable by U
            moves.append(s[:n]+"U"+s[n+3:])
        if s[n:n+2] == 'UU':
            moves.append(s[:n]+s[n+2:])   # Rule 4: Any UU can be deleted
        
    return moves

def solve(s):
    strings = [ s ]    # All strings that need to be checked
    nsteps = 0
    while strings:
        all_next_moves = []
        nsteps += 1
        for s in strings:
            moves = next_moves(s)
            if "MU" in moves:
                print("Solved!!!")
                return
            all_next_moves.extend(moves)
        strings = all_next_moves
        print("After ", nsteps, "must check", len(strings))

solve("MI")

    
    

    
