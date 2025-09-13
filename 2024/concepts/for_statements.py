words = [ 'oyeku', 'ogbe', 'osa' ]

for w in words:
    print(w, len(w))

users = { 'Awo': 'active', 'Pastor': 'inactive', 'Tata': 'active' }

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}

for user, status in users.items():
    if status == 'active':
        active_users[user] = status


def make_chain(M):
    return M

def main() -> None:
    M = ""
    chain = make_chain(M)
    chain = M

