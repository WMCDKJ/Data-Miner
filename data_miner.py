# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:07:19 2023

@author: USER
"""

import guilib as gb
import os


widgets = {
    "textbox": None
}

def read_data(folder):
    data = []
    faulty_files = []
    lines = []

    for file_name in os.listdir(folder):
        if file_name.endswith(".mydat"):
            file_location = os.path.join(folder, file_name)
            file = open(file_location, "r")
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                try:
                    name, val1, val2 = line.split(",")
                    data.append((name, float(val1), float(val2)))
                except ValueError:
                    faulty_files.append(file_name)
        else:
            continue

    return data, faulty_files

def open_folder():
    folder_path = gb.open_folder_dialog("Open")
    if folder_path:
        data, faulty_files = read_data(folder_path)
        for fault in faulty_files:
            fault_file_string = "Faulty file :"+fault
            gb.write_to_textbox(widgets["textbox"], fault_file_string)
        gb.write_to_textbox(widgets["textbox"], f"Number of data rows read: {len(data)}")
        
def main():
    window = gb.create_window("test window")
    top_frame = gb.create_frame(window, gb.LEFT)
    button_frame = gb.create_frame(top_frame, gb.LEFT)
    
    load_button = gb.create_button(button_frame, "Load", open_folder)
    quit_button = gb.create_button(button_frame, "Quit", quit)
      
    textbox_frame = gb.create_frame(top_frame, gb.RIGHT) 

    textbox = gb.create_textbox(textbox_frame, width=80, height=20)
    widgets["textbox"] = textbox
    
    gb.start()

if __name__ == "__main__":
    main()

     

     
