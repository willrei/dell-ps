import dearpygui.dearpygui as dpg
import database as db

vp = dpg.create_viewport(title='Internacoes')
dpg.set_viewport_small_icon('python.ico')

with dpg.window(label='aaa', menubar=False) as window:
    dpg.add_button(label='1')
    dpg.add_button(label='2')
    dpg.add_button(label='3')
    dpg.add_button(label='4')
    dpg.add_button(label='5')

dpg.set_primary_window(window, True)
dpg.setup_dearpygui(viewport=vp)
dpg.show_viewport(vp)

dpg.show_item_registry()

dpg.start_dearpygui()

db.start()
print(len(db.get()))
db.close()
