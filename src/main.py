from heapq import *
from dijkstra import Dijkstra
from jps import JPS
from services.algorithm_service import algorithm_service
from create_array import create_array
import argparse


from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Todo application")

    ui_view = UI(window, algorithm_service)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
