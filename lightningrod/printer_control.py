from functools import partial
import asyncio
import justpy as jp
from groundplane import groundplane
from lightningrod.instructions import instructions


instr_interface = None
wp = None
gp = groundplane("gp.json")


async def condition_watcher(conditions):
    while True:
        met = True
        for comp, condition in conditions.items():
            print(f"Checking {comp} is set to {condition}")
            comp = getattr(gp, comp)
            if comp.state()['state'] != condition:
                met = False
                print("Conditions not met")
                break
        if met:
            print("CONDITIONS MET!")
            break
        asyncio.sleep(1)
    # Perform exit tasks
    print("Performing exit instructions")
    instruction = instructions[wp.stage]
    print(f"{wp.stage} instruction: {instruction}")
    if instruction.on_exit is not None:
        for comp, condition in instruction.on_exit.items():
            print(f"Setting {comp} to {condition}")
            getattr(gp, comp).request_state({"state": condition})
            print(f"{getattr(gp, comp)}")
            print(gp.right_door_latch.state())
    wp.stage += 1
    build_instr_interface()
    jp.run_task(wp.update())


instr_interface = None


def box_checked(self, msg):
    wp.stage += 1
    build_instr_interface()
    jp.run_task(wp.update())


def build_instr_interface():
    global condition_watch
    global instr_interface
    global wp
    print(f"WP at stage {wp.stage}")
    if instr_interface is not None:
        instr_interface.delete()
    
    if wp.stage < len(instructions):
        instruction = instructions[wp.stage]
        text = instruction.text
    else:
        jp.Div(a=instr_interface, classes="text-2xl text-center p-2", text="All Done!")
        jp.run_task(wp.update())
        return

    if instruction.during is not None:
        for comp, condition in instruction.during.items():
            getattr(gp, comp).request_state({"state": condition})

    instr_interface = jp.Div(a=wp, classes="container")
    text = instruction.text
    jp.Div(a=instr_interface, classes="text-2xl text-center p-2", text=instruction.text)
    if instruction.exit_condition == "user_input":
        print("Configuring for user input")
        div = jp.Div(a=instr_interface, classes="flex justify-center items-center align-center border-2")
        button_classes = 'w-32 mr-2 mb-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full'
        cb = jp.Button(a=div, type='button', classes=button_classes, click=box_checked, text="Confirm Step Complete")
    else:
        jp.run_task(condition_watcher(instruction.exit_condition))
    jp.run_task(wp.update())


async def initial_page():
    global wp
    global gp
    global instr_interface
    global instr_div
    wp = jp.WebPage()
    wp.stage = 0
    jp.Div(a=wp, classes="text-6xl text-center p-2", text="Hello!")
    error_field = jp.Div(a=wp, classes="text-xl text-center p-2 invisible", text="filler")
    build_instr_interface()


async def get_page():
    return wp


def launch_server():
    jp.justpy(get_page, startup=initial_page, host='0.0.0.0')

