from datetime import datetime as dt

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
    

clean_list = lambda list_obj:list([x for x in list_obj if x is not None])
clean_list_str = lambda list_obj:list([x for x in list_obj if (x is not None and x != '')])
clean_list_str_diary = lambda list_obj:list([x for x in list_obj if (x is not None and x != '' and x.startswith('#') == False)])
list_map = lambda list_obj,fn=str.strip : list(map(fn,list_obj))
date_display = lambda dtx : dtx.date().strftime("%d %b'%y")
lag_display_days = lambda start,end: (end-start).days
lag_display_hours = lambda start,end:  roundQuarter((end-start).seconds / 3600)
roundQuarter = lambda x:round(x * 4) / 4.0