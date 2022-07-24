'''
Python version = 3.9.6

'''

# Imports
from interface.interface import Interface


def main():
    print("MAIN")

    interface = Interface.get_instance()

    interface.run()

    print("MAIN - FINISHED.")

    

if __name__ == "__main__":
    main()