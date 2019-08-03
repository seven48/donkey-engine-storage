"""FTP module."""

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

DEFAULT_PORT = 2121
DEFAULT_MAX_CONS = 256

STORAGE_BANNER: str = os.getenv('STORAGE_BANNER') or 'Hello'
STORAGE_HOST: str = os.getenv('STORAGE_HOST') or ''
STORAGE_PORT: int = int(os.getenv('STORAGE_PORT') or DEFAULT_PORT)
STORAGE_MAX_CONS: int = int(os.getenv('STORAGE_MAX_CONS') or DEFAULT_MAX_CONS)
STORAGE_MAX_CONS_PER_IP: int = int(os.getenv('STORAGE_MAX_CONS_PER_IP') or 5)


def main() -> None:
    """FTP runner."""
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous('storage/', perm='elradfmwMT')

    ftp_handler = FTPHandler
    ftp_handler.authorizer = authorizer
    ftp_handler.banner = STORAGE_BANNER

    address = (STORAGE_HOST, STORAGE_PORT)
    server = FTPServer(address, ftp_handler)
    server.max_cons = STORAGE_MAX_CONS
    server.max_cons_per_ip = STORAGE_MAX_CONS_PER_IP

    server.serve_forever()


if __name__ == '__main__':
    main()
