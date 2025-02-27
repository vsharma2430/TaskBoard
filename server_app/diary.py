from datetime import datetime as dt
from server_app.models import *
from server_app.misc import *
from server_app import *

def load_diary(file_location:str='diary.txt'):
    diary_objects = []
    data = read_file(file_location=file_location)
    data = clean_list_str_diary(data)
    for dataX in data:
        data_items = list_map(dataX.split('|'))
        len_data = len(data_items)
        
        if(len_data >= 2):
            dtX : str = data_items[0]
            if('to' in dtX):
                dts = list_map(list_obj=list_map(dtX.split('to')),fn=dt_from_iso)
                diary_objects.append(Event(dt_stamp_start=dts[0],dt_stamp_end=dts[1],description=data_items[1]))
            
            elif(dtX != '' or None):
                diary_objects.append(Task(dt_stamp=dt_from_iso(data_items[0]),description=data_items[1]))
                if(len_data >=3):
                    diary_objects[-1].is_complete = Task.is_complete_status_parse(data_items[2])
        else:
            diary_objects.append(Note(description=data_items[0]))
    return diary_objects

def get_diary_context_search_managed(diary_context=0,search=None,nav_context={}):
    search_list = []
    if(search !=  None and search != ''):
        search_list = search.split(',')
        nav_context['nav_context']['search_string'] = f'{search}'
    return get_diary_context(sub_part=diary_context,search=search_list)

def get_diary_context(sub_part:int=0,search:list | None = None):
    diary_objects = load_diary()
    
    searched_diary = []
    if(search!=None and len(search)!=0):
        search = list_map(search,str.lower)
        for d_obj in diary_objects:
            for sx in search:
                desc_lower = d_obj.description.lower()
                all_found = True
                if(sx in desc_lower):
                    searched_diary.append(d_obj)
                    break
    else:
        searched_diary = diary_objects

    diary_objects = searched_diary
    
    task_list_obj = clean_list([dx if type(dx) == Task else None for dx in diary_objects])
    event_list_obj = clean_list([dx if type(dx) == Event else None for dx in diary_objects])
    note_list_obj = clean_list([dx if type(dx) == Note else None for dx in diary_objects])

    task_list_obj.sort(key=lambda x: x.dt_stamp,reverse=False)
    task_list_obj.sort(key=lambda x: x.is_complete,reverse=False)
    
    event_list_obj.sort(key=lambda x: (dt.now() - x.dt_stamp_start).seconds,reverse=False)

    note_list_obj.reverse()

    task_context =  list_map(fn=Task.get_context,list_obj=task_list_obj)
    event_context = list_map(fn=Event.get_context,list_obj=event_list_obj)
    note_context = list_map(fn=Note.get_context,list_obj=note_list_obj)

    if(sub_part == 0):
        diary = {'tasks' : task_context,
                'events' : event_context,
                'notes': note_context}
    elif(sub_part == 1):
        diary = {'tasks' : task_context,}
    elif(sub_part == 2):
        diary = {'events' : event_context}    
    elif(sub_part == 3):
        diary = {'notes': note_context}     
    
    diary['diary_context'] = sub_part
    return diary