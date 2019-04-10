import pyautogui
import time


class lab_auto_class_builder():
    def __init__(self):
        self.screen_size = pyautogui.size()
        # moving the mouse to the upper-left to stop programme
        pyautogui.FAILSAFE = True
        # a delay after each call
        # pyautogui.PAUSE = 0.1
        self.list_of_actions = ['move_mouse', 'click', 'user_input', '']
        
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
            # print(line)
            if 'loop_start' in line:
                print('loop started!')
                loop_start_line = line_count
                loop_number = int(line.replace('loop_start(', '').replace(')',''))
            if 'loop_end' in line:
                print('loop ended')
                loop_end_line = line_count
            line_count += 1

        print('loop number {}'.format(loop_number))
        print('loop start {}'.format(loop_start_line))
        print('loop end {}'.format(loop_end_line))

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

        print('head')
        print(lines[:loop_start_line])
        print('loop')
        print(lines[loop_start_line:loop_end_line])
        print('end')
        print(lines[loop_end_line:])


    def line_parser(self, line):
        print(line)
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
            elif action == 'click':
                self.click(argument)
            elif action == 'delay':
                self.delay(argument)
            elif action == 'key_combination':
                self.key_combination(argument) 
            elif action == 'keyboard_input':
                self.keyboard_input(argument)

    def move_mouse(self, argument='100, 200'):
        x = int(argument.split(',')[0])
        y = int(argument.split(',')[1])
        pyautogui.moveTo(x, y, duration=0.1)
        
    def delay(self, argument='0.5'):
        time.sleep(float(argument))

    def click(self, argument="'right'"):
        # remove the quotation mark before and after
        argument = argument[1:-1]
        pyautogui.click(button=argument)
    
    def key_combination(self, argument="'ctrl', 's'"):
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
            try:
                self.sample_number += 1
            except AttributeError:
                self.sample_number = int(keys[1])
            text = keys[0] + '{:03d}'.format(self.sample_number)
        
        pyautogui.typewrite(text, interval=0.01)

            



if __name__ == '__main__':
    lab_auto_class = lab_auto_class_builder()
    lab_auto_class.script_parser(filename='example_script.txt')