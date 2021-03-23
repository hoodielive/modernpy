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

