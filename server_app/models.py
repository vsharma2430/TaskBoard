from pydantic import BaseModel
from datetime import datetime as dt
from typing import Union
from abc import ABC, abstractmethod
from server_app.misc import *

class DiaryEntry(ABC):
    @abstractmethod
    def get_context(self):
        pass

class Event(BaseModel,DiaryEntry):
    dt_stamp_start: dt
    dt_stamp_end: dt
    description: str    
    level: Union[int, None] = None
    attended: Union[bool, None] = False

    def get_context(self):
        data = list_map(self.description.split(','))

        title = data[0]
        desc = ''
        if(len(data)>=1):
            desc = data[1]

        return {
            'start_date':date_display(self.dt_stamp_start),
            'start_time':self.dt_stamp_start.time(),
            'end_date':date_display(self.dt_stamp_end),
            'end_time':self.dt_stamp_end.time(),
            'title':title,
            'description':desc,
            'level':self.level,
            'attended':self.attended,
            'lag_days': lag_display_days(start=self.dt_stamp_start,end=self.dt_stamp_end),
            'lag_hours': lag_display_hours(start=self.dt_stamp_start,end=self.dt_stamp_end),
            'opacity': 100 if dt.now() <= self.dt_stamp_end else 50
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
        data = list_map(self.description.split(','))
        
        title = data[0]
        desc = ''
        if(len(data)>=1):
            desc = data[1]

        return {
            'date':date_display(self.dt_stamp),
            'time':self.dt_stamp.time(),
            'title':title,
            'description':desc,
            'level':self.level,
            'complete':self.is_complete,
            'lag_days': lag_display_days(start=self.dt_stamp,end=dt.now()),
            'lag_hours':  lag_display_hours(start=self.dt_stamp,end=dt.now()),
            'opacity': 50 if self.is_complete else 100
        }
    
class Note(BaseModel,DiaryEntry):
    description: str    
    level: Union[int, None] = None

    def get_context(self):
        data = list_map(self.description.split(','))
        
        title = data[0]
        desc = ''
        if(len(data)>=1):
            desc = data[1]

        return {
            'title':title,
            'description':desc,
            'level':self.level,
            'opacity': 75
        }