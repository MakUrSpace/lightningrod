import justpy as jp
from lightningrod.instructions import instructions
from groundplane import groundplane
from inspect import getmembers, ismethod, signature

input_classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
p_classes = 'm-2 p-2 h-32 text-xl border-2'


gp = None

async def box_checked(self, msg):
    if self.instr_id > len(self.instr_div.checked):
        self.error_field.text = "Oh No!"
        self.error_field.classes = self.error_field.classes.replace("invisible", "visible")
    else:
        if self.instr_id == 1:
            gp.lights.set_strip_to_color()
        self.instr_div.checked.append(self.instr_id)


def thing_administration_invocation(self, msg):
    method = getattr(gp, self.method_name)
    print(f"Received {self.method_name} for {method}")
    if getattr(self, "arg_field", None):
        print(f"With args: {arg_field}")
    # TODO: interpret  msg for method parameters
    args = []
    kwargs = {}
    #    method(*args, **kwargs)


def build_thing_panel(host_div, thing):
    global gp
    thing_div = jp.Div(a=host_div, classes="border-2")
    jp.Div(a=thing_div, classes="text-2xl text-center p-2", text=f"{thing.thing_name.replace('_', ' ').title()} panel")
    for method_name, method in getmembers(thing, ismethod):
        if '__' in method_name[2:]:
            continue
        ui_div = jp.Div(a=thing_div, classes="flex justify-center items-center")
        method_sig = signature(method)
        label_classes = "m-2 p-2 w-128 text-right"
        main_label_text = f"{method_name.replace('_', ' ').title()}"
        arg_field = None
        if method_sig.parameters:
            label_text = f" ({dict(method_sig.parameters)}) "
            jp.Div(a=ui_div, classes=label_classes, text=main_label_text + label_text)
            arg_field = jp.Input(a=ui_div, type="text", classes="w-256 m-4 text-right")
        else:
            jp.Label(a=ui_div,
                     text=main_label_text,
                     classes=label_classes)
        button_classes = "w-16 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded-full"
        invoke = jp.Button(a=ui_div, text="Invoke", click=thing_administration_invocation, classes=button_classes)
        invoke.method_name = method_name
        invoke.arg_field = arg_field


def input_demo(request):
    wp = jp.WebPage()
    jp.Div(a=wp, classes="text-6xl text-center p-2", text="PDPM Administration Console")
    error_field = jp.Div(a=wp, classes="text-xl text-center p-2 invisible", text="filler")
    panel_div = jp.Div(a=wp, classes="border-4")
    
    things = [getattr(gp, m['SORT']) for m in gp.mthings]
    for thing in things:
        build_thing_panel(panel_div, thing)
    return wp


def launch_server(gp_cfg_path="gp.json"):
    global gp
    gp = groundplane(gp_cfg_path)
    jp.justpy(input_demo, host='0.0.0.0')

