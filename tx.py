import hconfig
import blockchain as hchain
import json
import rcrypt
import secrets
import pdb
import logging

"""
log debugging messages to file debug.log
"""
logging.basicConfig(filename="debug.log", filemode="w", \
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    level=logging.DEBUG)

def create_transaction(transaction: 'dictionary', zero_inputs: 'boolean'=False) -> 'bool':
    if validate_transaction(transaction, zero_inputs) == False: return False
    return True

create_transaction()
