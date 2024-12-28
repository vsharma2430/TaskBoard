from server_app.models import *
from datetime import datetime as dt

nav_props = {'nav_title':'TaskBoard','nav_sub_title':'',
             'search_string':'',
             'nav_list':[{ 'caption': 'Home' , 'href' : f'/' ,},
                        { 'caption': 'Tasks' , 'href' : f'/{Task.url}/' ,},
                        { 'caption': 'Notes' , 'href' : f'/{Note.url}/',},
                        { 'caption': 'Meetings','href' : f'/{Event.url}/',},
                        { 'caption': 'Diary','href' : f'/diary/',},
                        { 'caption': 'Help','href' : f'/help/',}],}

nav_context = {'nav_context':nav_props}

quotes = [
    Quote(quote_data="The single biggest problem in communication is the illusion that it has taken place.",citation="George Bernard Shaw"),
    Quote(quote_data="Blessed is the man, who having nothing to say, abstains from giving wordy evidence of the fact.",citation="George Eliot"),
    Quote(quote_data="The exaggeradtedly high value and attachment placed on products that you build yourself,regardless of the end result quality.",citation="IKEA Effect")
]
def refresh_context():
    nav_context['nav_context']['search_string'] = ''

def get_quote():
    return quotes[dt.now().second%len(quotes)].get_context()

quote_context={'quote_context':get_quote()}
