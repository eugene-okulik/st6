import logging
logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

print(__name__)


def greet():
    logging.debug('Asking user\'s name')
    name = input('your name: ')
    logging.info(f'User name is {name}')
    print(f'Hello, {name}')
    logging.debug('Finishing program')
