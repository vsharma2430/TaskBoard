from datetime import datetime as dt
from server_app.models import *
from server_app.misc import *
from server_app import *

def load_diary(file_location:str='diary.txt'):
    diary_objects = []
    data = read_file(file_location=file_location)
    for dataX in data :
        data_items = list_map(dataX.split('|'))
        len_data = len(data_items)
        
        if(len_data >= 2):
            dtX : str = data_items[0]
            if('to' in dtX):
                dts = list_map(list_obj=list_map(dtX.split('to')),fn=dt.fromisoformat)
                diary_objects.append(Event(dt_stamp_start=dts[0],dt_stamp_end=dts[1],description=data_items[1]))
            
            elif(dtX != '' or None):
                diary_objects.append(Task(dt_stamp=dt.fromisoformat(data_items[0]),description=data_items[1]))
                if(len_data >=3):
                    diary_objects[-1].is_complete = Task.is_complete_status_parse(data_items[2])
        else:
            diary_objects.append(Note(description=data_items[0]))

    return diary_objects

def get_diary_context():
    diary_objects = load_diary()

    task_list_obj = clean_list([dx if type(dx) == Task else None for dx in diary_objects])
    event_list_obj = clean_list([dx if type(dx) == Event else None for dx in diary_objects])
    note_list_obj = clean_list([dx if type(dx) == Note else None for dx in diary_objects])

    task_list_obj.sort(key=lambda x: x.dt_stamp,reverse=False)
    task_list_obj.sort(key=lambda x: x.is_complete,reverse=False)
    
    event_list_obj.sort(key=lambda x: (dt.now() - x.dt_stamp_start).seconds,reverse=True)

    task_context =  list_map(fn=Task.get_context,list_obj=task_list_obj)
    event_context = list_map(fn=Event.get_context,list_obj=event_list_obj)
    note_context = list_map(fn=Note.get_context,list_obj=note_list_obj)

    diary = {'tasks' : task_context,
             'events' : event_context,
             'notes': note_context}
    return diary
