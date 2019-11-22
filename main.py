from logger import Logger
from send import Transceiver
from visualize import *

log = Logger()

def main():
    print (log.read("filename.txt"))


if __name__ == "__main__":
    main()