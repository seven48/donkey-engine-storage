""" FTP module """

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


STORAGE_BANNER = os.getenv('STORAGE_BANNER') or 'Hello'
STORAGE_HOST = os.getenv('STORAGE_HOST') or ''
STORAGE_PORT = os.getenv('STORAGE_PORT') or 2121
STORAGE_MAX_CONS = os.getenv('STORAGE_MAX_CONS') or 256
STORAGE_MAX_CONS_PER_IP = os.getenv('STORAGE_MAX_CONS_PER_IP') or 5


def main():
    """ FTP runner """
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous('storage/')

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = STORAGE_BANNER

    address = (STORAGE_HOST, STORAGE_PORT)
    server = FTPServer(address, handler)
    server.max_cons = STORAGE_MAX_CONS
    server.max_cons_per_ip = STORAGE_MAX_CONS_PER_IP

    server.serve_forever()

if __name__ == "__main__":
    main()
