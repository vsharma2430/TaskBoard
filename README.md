# TaskBoard

## Introduction

This application exists to create beautiful view of a bullet journal/diary.All bullets of the journal are categorised under three heads namely Notes,Tasks and Events.

## Diary 
Diary is a simple text file which the application takes as an input. Each line of the diary is an categorised as a note,task or an event.User can also include comments in the diary which are not published using a '#' character in front of the bullet.

`# this is a comment or is it?`

### Notes
Notes are general text included in the diary with no deadlines or long-term plans.

`note heading (optional), hi there I'm a chilled out note.Look out for me on a weekend or a slow weekday.`

#### Bullets in bullets
> See there is always a guy If I had a wish I'd wish for three more wishes. 
> (Chandler)

You know what I'd like to grant you one. Here goes, join the two text using '&&' (why not just one ??).

`heading, note 1 && please connect me to same heading.`

#### Connected world

Add links to your bullet entry data using the format below.

`heading, note me please && [link name -> link address]`

##### Multiple connections ?

Sure why not!

`heading, note && [link name -> link address] && [name 2 -> link 2]`

### Tasks

Tasks are the bullet entires for the work assigned to you.This would only make sense if you had a date or the best estimate of a date when this task was assigned to you.To make matters worse this date should be entered in the specified format as below and the description of the task should be separarted by '|'.

`yyyy-mm-dd hh:mm:ss | heading yet again , I will almost do this now`

If you complete this task you are allowed to cross this off by using '| done' tag in the end like this else it would show in the incomplete list till eternity.

`yyyy-mm-dd hh:mm:ss | heading , Told ya I'd complete this | done`

### Events/Meetings

Events are the bullet entries which have a timeline both start and end which should be mentioned.This could be a meeting with a nemesis or a inter-departmental coordination.

`yyyy-mm-dd hh:mm:ss to yyyy-mm-dd hh:mm:ss | heading , we meet again`

## Features
But why should we use this Mr. Developer.Well, here is a list of features or bugs which you could find useful.

### Date-wise sorting 
Your bullet entries will be shown to you in a beautiful format and will be cooked with a secret sauce which is only known to python developers and Martians.Anyway the result is more than useful to a normal corporate peasant.

### Psychology
Your manager may finally acknowledge the work you do.

# Deployment (Coming soon)