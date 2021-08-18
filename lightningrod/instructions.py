unicode_forbidden_symbol = u"\U0001F6C7"
unicode_uparrow_symbol = u"\u2B61"
unicode_downarrow_symbol = u"\u2B63"

instructions = [
    {"instr": "Open Right Door"},
    {"instr": "Open Printer Door"},
    {"instr": "Raise Printer Head",
     "subinstr": [
         {"instr": "Press 'Tools'"},
         {"instr": "Press 'Move Z'"},
         {"instr": "Press '10mm'"},
         {"instr": f"Press '{unicode_uparrow_symbol}' until printer head has raised up and out of the resin vat",
          "tip": f"Press '{unicode_forbidden_symbol}' to stop the printer head from moving"}
     ]
    },
    {"instr": "Remove resin vat",
     "subinstr": [
         {"instr": "Loosen thumb-screws on either side of the resin vat by hand"},
         {"instr": "Slide resin vat towards the front of the printer until it clears the brackets"}
     ]
    },
    {"instr": "Level Printer Bed",
     "subinstr": [
        {"instr": "Loosen printer bed bolt"},
        {"instr": "Press the house-shaped button"},
        {"instr": "Press '0.1mm'"},
        {"instr": f"Adjust printer bed level with the '{unicode_uparrow_symbol}' and '{unicode_downarrow_symbol}' buttons"},
        {"instr": "Tighten printer bed bolt"},
        {"instr": "Press back arrow"},
        {"instr": "Press 'Z=0'"},
        {"instr": "Press 'Enter'"},
        {"instr": "Press back arrow"}
     ]
    }
]
