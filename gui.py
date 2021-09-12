import dearpygui.dearpygui as dpg
import database

vp = dpg.create_viewport(title='Internacoes')
dpg.set_viewport_small_icon('python.ico')

with dpg.font_registry():
    dpg.add_font('Roboto.ttf', 15, default_font=True)

db = database.Database()
db.start()

with dpg.window(menubar=False) as window:

    with dpg.tab_bar():
        with dpg.tab(label='1: Media de Idade'):
            with dpg.table(header_row=True, row_background=True,
                        borders_innerH=True, borders_outerH=True,
                        borders_innerV=True, borders_outerV=True, resizable=True,
                        scrollX=True, policy=dpg.mvTable_SizingFixedFit):
                for field in db.fields:
                    dpg.add_table_column(label=field.replace('_', ' ').title())
                data = db.get_municipio('VIAMAO')
                for row in range(len(data)):
                    for col in range(db.field_count):
                        dpg.add_text(f'{data[row][col]}')
                        if not (row == len(data) - 1 and col == db.field_count - 1):
                            dpg.add_table_next_column()

        with dpg.tab(label='2: Internacoes por Ano'):
            with dpg.table(header_row=True, row_background=True,
                        borders_innerH=True, borders_outerH=True,
                        borders_innerV=True, borders_outerV=True, resizable=True,
                        scrollX=True, policy=dpg.mvTable_SizingFixedFit):
                for field in db.fields:
                    dpg.add_table_column(label=field.replace('_', ' ').title())
                data = db.get_municipio('XANGRI-LA')
                for row in range(len(data)):
                    for col in range(db.field_count):
                        dpg.add_text(f'{data[row][col]}')
                        if not (row == len(data) - 1 and col == db.field_count - 1):
                            dpg.add_table_next_column()

        with dpg.tab(label='3: Hospitais'):
            with dpg.table(header_row=True, row_background=True,
                        borders_innerH=True, borders_outerH=True,
                        borders_innerV=True, borders_outerV=True, resizable=True,
                        scrollX=True, policy=dpg.mvTable_SizingFixedFit):
                for field in db.fields:
                    dpg.add_table_column(label=field.replace('_', ' ').title())
                data = db.get_municipio('CACHOEIRINHA')
                for row in range(len(data)):
                    for col in range(db.field_count):
                        dpg.add_text(f'{data[row][col]}')
                        if not (row == len(data) - 1 and col == db.field_count - 1):
                            dpg.add_table_next_column()

        with dpg.tab(label='4: Tempo de Internacao'):
            with dpg.table(header_row=True, row_background=True,
                        borders_innerH=True, borders_outerH=True,
                        borders_innerV=True, borders_outerV=True, resizable=True,
                        scrollX=True, policy=dpg.mvTable_SizingFixedFit):
                for field in db.fields:
                    dpg.add_table_column(label=field.replace('_', ' ').title())
                data = db.get_municipio('CAMARGO')
                for row in range(len(data)):
                    for col in range(db.field_count):
                        dpg.add_text(f'{data[row][col]}')
                        if not (row == len(data) - 1 and col == db.field_count - 1):
                            dpg.add_table_next_column()

        with dpg.tab(label='5: Tempo de Espera na Fila'):
            with dpg.table(header_row=True, row_background=True,
                        borders_innerH=True, borders_outerH=True,
                        borders_innerV=True, borders_outerV=True, resizable=True,
                        scrollX=True, policy=dpg.mvTable_SizingFixedFit):
                for field in db.fields:
                    dpg.add_table_column(label=field.replace('_', ' ').title())
                data = db.get_municipio('SAPIRANGA')
                for row in range(len(data)):
                    for col in range(db.field_count):
                        dpg.add_text(f'{data[row][col]}')
                        if not (row == len(data) - 1 and col == db.field_count - 1):
                            dpg.add_table_next_column()

dpg.set_primary_window(window, True)
dpg.setup_dearpygui(viewport=vp)
dpg.show_viewport(vp)

dpg.start_dearpygui()

db.close()
