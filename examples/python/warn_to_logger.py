import warnings
import logging

def do_something():
    warnings.warn("Some warning")

def main():
    logger = logging.getLogger('py.warnings')
    logging.captureWarnings(True)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)-10s - %(message)s'))
    logger.addHandler(sh)

    logger.setLevel(logging.DEBUG)
    logger.info("before")
    do_something()
    logger.info("after")

main()
