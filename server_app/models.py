from re import search
from datetime import datetime as dt
from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Union
from server_app import *
from server_app.misc import *
from server_app.ui import *

class DiaryEntry(ABC):
    description: str    
    title : Union[str,None] = ''
    job : Union[str,None] = None
    data : Union[list[str],None] = []
    link : Union[list[tuple],None] = []

    def parse_data(self):
        data = list_map(self.description.split(','))
        split_data_0 = data[0].split()
        if(len(split_data_0)>=1 and search('[a-zA-Z0-9][0-9]{3}',split_data_0[0])):
            self.job = split_data_0[0]
            if(len(split_data_0)>1):
                self.title = ' '.join(split_data_0[1:])
        else:            
            self.title = data[0]    

        if(len(data)>1):
            data_list = list_map(data[1].split('&&'))
            extracted_data = []
            extracted_links = []

            dataX:str
            for dataX in data_list:
                if('[' in  dataX and ']' in dataX):
                    start_index = dataX.find('[')
                    link_data = list_map(dataX[start_index:dataX.find(']')].split('->'))
                    link_tuple = ('link',link_data[-1]) if len(link_data)==1 else (link_data[0].strip('['),link_data[1])
                    extracted_links.append(link_tuple)
                else:
                    extracted_data.append(dataX)

            self.link.extend(extracted_links)
            self.data.extend(extracted_data)

    @abstractmethod
    def get_context(self):
        pass

class Event(BaseModel,DiaryEntry):
    dt_stamp_start: dt
    dt_stamp_end: dt
    level: Union[int, None] = None
    attended: Union[bool, None] = False

    def get_context(self):
        self.parse_data()

        return {
            'start_date':date_display(self.dt_stamp_start),
            'start_time':self.dt_stamp_start.strftime('%H:%M'),
            'end_date':date_display(self.dt_stamp_end),
            'end_time':self.dt_stamp_end.strftime('%H:%M'),
            'title':self.title,
            'job':self.job,
            'description':self.data,
            'link':self.link,
            'level':self.level,
            'attended':self.attended,
            'lag_days': lag_display_days(start=self.dt_stamp_start,end=self.dt_stamp_end),
            'lag_hours': lag_display_hours(start=self.dt_stamp_start,end=self.dt_stamp_end),
            'opacity': full_opacity if dt.now() <= self.dt_stamp_end else muted_opacity,
            'card_class': 'border-info' if self.dt_stamp_start <= dt.now() <= self.dt_stamp_end else ''
        }
    
class Task(BaseModel,DiaryEntry):
    dt_stamp: dt
    description: str    
    level: Union[int, None] = None
    is_complete: Union[bool, None] = False

    @staticmethod
    def is_complete_status_parse(data:str):
        check = data.lower()
        if('y' in check or 'done' in check or 'yes' in check):
            return True
        return False

    def get_context(self):
        self.parse_data()
        lag_days = lag_display_days(start=self.dt_stamp,end=dt.now())
        lag_hours = lag_display_hours(start=self.dt_stamp,end=dt.now())
        card_class = ''

        if(self.is_complete == False):
            if (lag_days ==0):
                card_class = 'border-info'
            elif(1<=lag_days<=3):
                card_class = 'border-warning'
            elif(4<=lag_days<=7):
                card_class = 'border-danger'

        return {
            'date':date_display(self.dt_stamp),
            'time':self.dt_stamp.time(),
            'title':self.title,
            'job':self.job,
            'description':self.data,
            'link':self.link,
            'level':self.level,
            'complete':self.is_complete,
            'lag_days': lag_days,
            'lag_hours': lag_hours ,
            'opacity': muted_opacity if self.is_complete else full_opacity,
            'card_class': card_class
        }
    
class Note(BaseModel,DiaryEntry):
    level: Union[int, None] = None

    def get_context(self):
        self.parse_data()

        return {
            'title':self.title,
            'job':self.job,
            'description':self.data,
            'link':self.link,
            'level':self.level,
            'opacity': note_opacity
        }