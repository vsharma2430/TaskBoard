from server_app.models import *

nav_props = {'nav_title':'TaskBoard','nav_sub_title':'',
             'search_string':'',
             'nav_list':[{ 'caption': 'Home' , 'href' : f'/' ,},
                        { 'caption': 'Tasks' , 'href' : f'/{Task.url}/' ,},
                        { 'caption': 'Notes' , 'href' : f'/{Note.url}/',},
                        { 'caption': 'Meetings','href' : f'/{Event.url}/',},
                        { 'caption': 'Diary','href' : f'/diary/',},
                        { 'caption': 'Help','href' : f'/help/',}],}

nav_context = {'nav_context':nav_props}

def refresh_context():
    nav_context['nav_context']['search_string'] = ''