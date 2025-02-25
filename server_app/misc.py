from datetime import datetime as dt
from server_app import *

def read_file(file_location:str):
    data = []
    with open(file_location, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def dt_from_iso(data:str):
    try:
        return dt.fromisoformat(data)
    except:
        return dt.now()
    
def add_s_tag(data:str):
    if(data.startswith('<s>') == True and data.endswith('</s>') == False):
        return data + ' </s>'
    elif(data.startswith('<s>') == False and data.endswith('</s>') == True):
        return '<s> ' + data
    else :
        return data
    
def join_strings_starting_with_and(strings:list[str]) -> list[str]:
    modified_strings = []
    for string in strings:
        if string.startswith('&&'):
            if modified_strings:
                modified_strings[-1] += string[2:]
        else:
            modified_strings.append(string)
    return modified_strings

clean_list = lambda list_obj:list([x for x in list_obj if x is not None])
clean_list_str = lambda list_obj:list([x for x in list_obj if (x is not None and x != '')])
clean_list_str_diary = lambda list_obj:join_strings_starting_with_and(list([x for x in list_obj if (x is not None and x != '' and x.startswith('#') == False)]))
list_map = lambda list_obj,fn=str.strip : list(map(fn,list_obj))
date_display = lambda dtx : dtx.date().strftime("%d %b'%y")
lag_display_days = lambda start,end: (end-start).days if (end > start) else -1*(start-end).days
lag_display_hours = lambda start,end:  roundQuarter((end-start).seconds / 3600) if (end > start) else -1*roundQuarter((start - end).seconds / 3600)
roundQuarter = lambda x:round(x * 4) / 4.0
check_start_end_str = lambda x,y:True if x.startswith(y) and x.endswith(y) else False
check_start_end_tag = lambda x,tag:True if x.startswith(f'<{tag}>') and x.endswith(f'</{tag}>') else False
add_start_end_tag = lambda x,tag: f'<{tag}>' + x.strip(f'<{tag}>').strip(f'</{tag}>') + f'</{tag}>'