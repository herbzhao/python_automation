# python_automation
based on pyautogui

You can now write down scripts for automation, for example, moving mouse to certain place and click button.

You can also track location of a screen shot. 



## remember to change current working folder to this module!

Run the automation:

`python run_me.py`

#### change the active script file name accordingly

Find the coordinates of mouse by 

`python coordinate_recorder.py`

and the coordinates will be available in `coordinates.txt`


## How to edit script file:

edit/create the script file in scripts folder

```python
# hot_key combination
hot_key('ctrl', 'f')
# move mouse to absolute coordinate 
move_mouse(800, 300)
# or relative
move_mouse_relative(-100,0)
# add delay in seconds
delay(1)

# control keyboard to type, the arguments are keyboard_input(text, starting_count, counter_name)
keyboard_input('abcde')
keyboard_input('CNC_20x_', '0')
keyboard_input('CNC_20x_', '1', 'counter1')
```

### Read scripts/example_script.txt for more information 
