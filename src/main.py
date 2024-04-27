from tkinter import Tk
from services.algorithm_service import algorithm_service
from ui.ui import UI


def main():
    window = Tk()
    window.title("Todo application")

    ui_view = UI(window, algorithm_service)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
