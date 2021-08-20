import justpy as jp
from instructions import instructions

input_classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
p_classes = 'm-2 p-2 h-32 text-xl border-2'


async def box_checked(self, msg):
    if self.instr_id > len(self.instr_div.checked):
        self.error_field.text = "Oh No!"
        self.error_field.classes = self.error_field.classes.replace("invisible", "visible")
    else:
        self.instr_div.checked.append(self.instr_id)


async def input_demo(request):
    wp = jp.WebPage()
    jp.Div(a=wp, classes="text-6xl text-center p-2", text="Hello!")
    error_field = jp.Div(a=wp, classes="text-xl text-center p-2 invisible", text="filler")
    instr_div = jp.Div(a=wp, classes="border-4")
    instr_div.checked = []
    for i, instr in enumerate(instructions):
        div = jp.Div(a=instr_div, classes="flex justify-center items-center align-center border-2")
        cb = jp.Input(a=div, type='checkbox', classes="w-4 align-left", change=box_checked)
        cb.instr_id = i
        cb.instr_div = instr_div
        cb.error_field = error_field
        jp.Label(a=div, classes='m-2 p-2 w-64 inline-block text-left', text=instr['instr'])
    return wp


jp.justpy(input_demo, host='0.0.0.0')
