import pyautogui  # http://pyautogui.readthedocs.io/en/latest/cheatsheet.html

class  coordinate_recorder_class_builder():
    def __init__(self):
        self.filename = 'coordinates.txt' 
        self.screenshot_folder = 'screenshots\\'
    
    def record_mouse_position(self):
        while True:
            coordinate_name = pyautogui.prompt(text = 'Name the coordinate', title = 'Name the coordinate', default='default')
            with open(self.filename, 'a+') as coordinate_file:
                coordinate_file.write(coordinate_name + ': ({}, {})'.format(pyautogui.position()[0], pyautogui.position()[1]))
                coordinate_file.write('\n')

            if coordinate_name is None:
                break



if __name__ == '__main__':
    coordinate_recorder = coordinate_recorder_class_builder()
    coordinate_recorder.record_mouse_position()