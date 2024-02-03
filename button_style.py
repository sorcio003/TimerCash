start_btn = '''
MDRoundFlatIconButton:
    text: "Start"
    icon: "check"
    text_color: "white"
    theme_bg_color: "Custom"
    line_color: "black"
    icon_color: "white"
    md_bg_color: "green"
    pos_hint: {'center_x':0.65, 'center_y':0.2}
    on_press: app.start()
'''

end_btn = '''
MDRoundFlatIconButton:
    text: "End"
    icon: "close"
    text_color: "white"
    theme_bg_color: "Custom"
    line_color: "black"
    icon_color: "white"
    md_bg_color: "red"
    pos_hint: {'center_x':0.35, 'center_y':0.2}
    on_press: app.stop()
'''

add_worker_btn = '''
MDRoundFlatIconButton:
    text: "Add Worker"
    icon: "plus"
    text_color: "black"
    pos_hint: {'center_x':0.8, 'center_y':0.8}
    on_press: app.add_worker()
'''