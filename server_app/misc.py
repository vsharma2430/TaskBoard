def read_file(file_location:str):
    data = []
    with open(file_location, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

clean_list = lambda list_obj:list([x for x in list_obj if x is not None])
list_map = lambda list_obj,fn=str.strip : list(map(fn,list_obj))
date_display = lambda dtx : dtx.date().strftime("%d %b'%y")
lag_display_days = lambda start,end: (end-start).days
lag_display_hours = lambda start,end:  roundQuarter((end-start).seconds / 3600)
roundQuarter = lambda x:round(x * 4) / 4.0