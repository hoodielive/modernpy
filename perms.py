# perms.py:  File permissions
#
# On Unix, file permissions are organized into three parts.
#
#      - User permission
#      - Group permission
#      - All permission
#
# You see these permissions when looking at a directory listing
#
#     bash % ls -l
#     -rw-r--r--  1 beazley  staff  3622 Jul  9 03:32 data.py
#      ^^^^^^^^^
#      U  G  A
#
# The permissions for each part are represented as a 3-bit 
# integer (rwx).  For example:
#       
#       4 = 0b100 -> Read
#       5 = 0b101 -> Read/Execute
#       6 = 0b110 -> Read/Write
#       7 = 0b111 -> Read/Write/Execute
#      
# A complete set of permissions is often written out in Octal (base-8)
# like this:
#
#       -rw-r--r-- -> 0o644  -> 0b110100100 -> 0b110_100_100  
#

import os
def get_user(perms):
    # Return the user-portion of permissions
    return (perms >> 6)


assert get_user(0o644) == 6

def get_group(perms):
    return (perms >> 3) & 0b111
    return (perms & 0b000111000) >> 3 # Alternative 
# assert get_group(0o644) == 4

def get_all(perms):
    return perms & 0b111

# assert get_all(0o642) == 2

def set_user(perms, pbits):
    # Set the user permission bits
    perms = (perms & 0b000111111) | (pbits << 6)

# assert set_user(0o644, 7) == 0o744

def set_group(perms, pbits):
    # Set the group bits
    return (perms & 0b000111111) | (pbits << 3) 

# assert set_group(0o644, 6) == 0o664

def set_all(perms, pbits):
    # Set the all bits
    return (perms & 0b111111000) | pbits

# assert set_all(0o644, 0) == 0o640

# These functions test a group of 3 permission bits to
# see if an operation is allowed or not.

def can_read(pbits):
    return pbits & 0b010

# assert can_read(get_user(0o644)) == True

def can_write(pbits):
    return pbits & 0b010

# assert can_write(get_user(0o644)) == False

def can_execute(pbits):
    pass

# assert can_execute(get_user(0o644)) == False

# Sometimes the above operations are carried out with bitmasks
P_ALL_X   = 0b000000001
P_ALL_W   = 0b000000010
P_ALL_R   = 0b000000100
P_GROUP_X = 0b000001000
P_GROUP_W = 0b000010000
P_GROUP_R = 0b000100000
P_USER_X  = 0b001000000
P_USER_W  = 0b010000000
P_USER_R  = 0b100000000

# Show how you could set USER_X permission
perm = 0o644     # Change to 0o744

# Show how you could take away USER_W permission
perm = 0o644     # Change to 0o444

