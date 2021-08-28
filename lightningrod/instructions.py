unicode_forbidden_symbol = u"\U0001F6C7"
unicode_uparrow_symbol = u"\u2B61"
unicode_downarrow_symbol = u"\u2B63"


class PDPMInstruction:
    def __init__(self, text, exit_condition, during=None, on_exit=None, tip=None):
        self.text = text
        self.exit_condition = exit_condition
        self.during = during
        self.on_exit = on_exit
        self.tip = tip


instructions = [
    PDPMInstruction(**instr) for instr in 
    [
        {"text": "Open Right Door",
         "during": {
             "right_door_latch": "retracted",
             "lights": "white"
         },
         "exit_condition": {
             "right_door_sensor": "no_field_present"
         },
         "on_exit":{
             "right_door_latch": "extended",
         }
        },
        {"text": "Open Printer Door",
         "exit_condition": "user_input"},
        {"text": "Raise Printer Head",
         "exit_condition": "user_input"},
        {"text": "Press Start Print",
         "during": {
             # "storageplane": "send_file"
         },
         "exit_condition": "user_input"},
        {"text": "Close Right Door",
         "exit_condition": {
             "right_door_sensor": "field_present"
         },
         "on_exit":{
             "lights": "off"
         }
        }
    ]
]
