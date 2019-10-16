import sys
import traceback

from tkinter import Tk

from gui import App

def main():
    try:
        obj = App()

        root = Tk()
        obj.run(root)

    except KeyboardInterrupt:
        print("Keyboard Interrupt Occured")
        sys.exit()
    except:
        traceback.print_exc()
        sys.exit()

if __name__ == "__main__":
    main()

