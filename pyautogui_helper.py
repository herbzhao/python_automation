import pyautogui
import time
import datetime

class pyautogui_helper_class_builder():
    def __init__(self):
        self.screen_size = pyautogui.size()
        # moving the mouse to the upper-left to stop programme
        pyautogui.FAILSAFE = True
        # a delay after each call
        # pyautogui.PAUSE = 0.1

        # a counter to store sample number
        self.counter = {}
        
    def script_parser(self, filename='example_script.txt'):
        file = open(filename, 'r')
        lines = file.readlines()
        line_count = 0
        loop_start_line = len(lines)
        loop_end_line = len(lines)
        loop_number = 0
        # remove the comments and blank space
        lines = [line for line in lines  if line[0] != '#' and line !='\n']

        for line in lines:
            if 'loop_start' in line:
                loop_start_line = line_count
                loop_number = int(line.replace('loop_start(', '').replace(')',''))
            if 'loop_end' in line:
                loop_end_line = line_count
            line_count += 1


        looped_lines = lines[loop_start_line:loop_end_line]
        # beginning of the command
        for line in lines[:loop_start_line]:
            self.line_parser(line)

        # loop in the middle 
        i = 0
        while i < loop_number:
            for line in looped_lines:
                self.line_parser(line)
            i += 1

        # after the loop
        for line in lines[loop_end_line:]:
            self.line_parser(line)


    def line_parser(self, line):
        #  for comment
        if line[0] == '#' or line == '\n':
            return None
        # example line is "action(x, y)"
        else:
            # remove the last ')'
            line = line.replace('\n','')[:-1]
            # part before '('
            action = line.split('(')[0]
            # part after ')'
            argument = line.split('(')[1]

            if action == 'move_mouse':
                self.move_mouse(argument)
            elif action == 'move_mouse_relative':
                self.move_mouse_relative(argument)
            elif action == 'find_image':
                self.find_image(argument)
            elif action == 'click':
                self.click(argument)
            elif action == 'delay':
                self.delay(argument)
            elif action == 'hot_key':
                self.hot_key(argument) 
            elif action == 'keyboard_input':
                self.keyboard_input(argument)

    def move_mouse(self, argument='100, 200'):
        x = int(argument.split(',')[0])
        y = int(argument.split(',')[1])
        pyautogui.moveTo(x, y, duration=0.1)

    def move_mouse_relative(self, argument='100, 200'):
        x = int(argument.split(',')[0])
        y = int(argument.split(',')[1])
        pyautogui.move(x, y, duration=0.1)

    def find_image(self, argument="'image.png'"):
        argument = argument[1:-1]
        #  keep searching the image in a loop
        while True:
            image_box = pyautogui.locateOnScreen(argument, grayscale=False)
            if image_box is None:
                print('couldnt find the {}, search again in few seconds'.format(argument))
                time.sleep(2)
            else:
                image_centre = pyautogui.center(image_box)
                pyautogui.moveTo(image_centre[0], image_centre[1], duration=0.1)
                break

    def delay(self, argument='0.5'):
        time.sleep(float(argument))

    def click(self, argument="'right'"):
        # remove the quotation mark before and after
        argument = argument[1:-1]
        pyautogui.click(button=argument)
    
    def hot_key(self, argument="'ctrl', 's'"):
        keys = argument.split(',')
        keys = [key.replace('\'','').replace('\"','').replace(' ','') for key in keys]
        pyautogui.hotkey(*keys)
    
    def keyboard_input(self, argument="'20x_', '001'"):
        keys = argument.split(',')
        keys = [key.replace('\'','').replace('\"','').replace(' ','') for key in keys]
        # the first argument is the normal text
        text = keys[0]
        #  the second argument is the incremental value
        if len(keys) > 1:
            if len(keys)>2:
                # if the counter name is specified
                try:
                    self.counter[keys[2]] += 1
                except KeyError:
                    self.counter[keys[2]] = int(keys[1])
                text = keys[0] + '{:03d}'.format(self.counter[keys[2]])
                
            else:
                # if the counter name is not specified, share the same counter
                try:
                    self.counter['default'] += 1
                except KeyError:
                    self.counter['default'] = int(keys[1])
                text = keys[0] + '{:03d}'.format(self.counter['default'])

        # print a time tag as this is useful for users
        pyautogui.typewrite(text, interval=0.01)
        print(datetime.datetime.now().strftime('%D %H:%M:%S'))
        print(text)



if __name__ == '__main__':
    pyautogui_helper_class = pyautogui_helper_class_builder()
    # change this file name to your script name
    pyautogui_helper_class.script_parser(filename='scripts/example_script.txt')