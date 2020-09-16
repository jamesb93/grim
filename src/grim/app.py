"""
Update manager for ReaCoMa
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from pathlib import Path


class Grim(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Row for Directory pointing
        self.find = toga.Button(
            'ReaCoMa location',
            on_press = self.find_reacoma,
            style=Pack(padding=5)
        )
        self.dir_label = toga.TextInput(
            readonly=True, 
            style=Pack(padding=5, width=500)
        )
        dir_box = toga.Box(style=Pack(direction=ROW))
        dir_box.add(self.find)
        dir_box.add(self.dir_label)

        # Add things to main box
        main_box.add(dir_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def get_me(self, btn):
        print(self.rand_label.value)
    
    def find_reacoma(self, btn):
        """pass the button that was pressed into the function"""
        p = self.main_window.select_folder_dialog('ReaCoMa location')

        if len(p) != 0:
            self.reacoma_dir = Path(p[0]).resolve()
            self.dir_label.value = str(self.reacoma_dir)


def main():
    return Grim()
