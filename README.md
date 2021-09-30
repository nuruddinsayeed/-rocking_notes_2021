# _Rocking Notes Project_

## About

Let's build a Python app that lets users to take notes, edit
them, share them with other users and delete them as well. Users can add tags so that they can find relevant
notes later. Users can also make their notes public so that any user can find them using tags. Sound
interesting? Okay let's get started.

## Tools used in this project

- python3,
- Flask,
- flask-peewee ORM
- Flask-RESTful API
- Flask-JWT-Extended Token Authentication
- SQLite,

## Installation

```json
$ git clone https://github.com/nuruddinsayeed/-rocking_notes_2021.git
$ cd (enter the downloaded directory)
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install - requirements.txt
```

Installing Part is done now lets Run our app

```json
$ python app.py
```

## Project Detail:

_If Poject setup is successfull, then you can follow the steps bellw_

### Video Link:

<p align="center">
  <a href="https://youtu.be/TbacbAHp7H8"><img src="https://github.com/nuruddinsayeed/ami-code-parina-project/blob/main/zzzz.png" width="290"></a>
</p>

## about token authentication

most of the links of this projec require token authentication.
So you will nee a Auth token, which can be gained by loggin in
or registration. So to authenticate, this token have to be used in
header section as Authorization and the tokne should be like this:
(Bearer your_auth_token). sample token: Bearer

Bearer eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMjk3MDI1MywianRpIjoiOGUwMWI5NTEtYmYzMC00ZDFlLTk4YmItOWI5NjgzNTI1NDM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VybmFtZSI6InNheWVkIn0sIm5iZiI6MTYzMjk3MDI1MywiZXhwIjoxNjMyOTcxMTUzfQ.mr0nc-fvJqm7HRyBmQSFjuceWTCQb2lfNPBFvVdG9P8

## This Project has three types of api endpoint

## Section One (Authentication/Registration api Endpoints):

_Save this login token to use it latter_

````json
Login Token URL: http://127.0.0.1:5000/api/login
Registration URL: http://127.0.0.1:5000/api/register

```

### Sample Registration payload


{
"username": "sayeed",
"email": "secret@email.com",
"password": "123"
}


### Sample Login payload


{
"username": "sayeed",
"password": "123"
}


## Section Two (User Notes CRUD and Note Tag api Endpoints):

_For creating a new Tag_(GET, POST)

```json

http://127.0.0.1:5000/api/tags

```

_For creating updatng deleting and getting notes_(GET, POST, PUT, DELETE)
_here 2 is id of the notes_

```json

http://127.0.0.1:5000/api/notes/2

```

### Sample Login payload for POST and PUT request


{
"message": "note created from postman Three",
"public": false,
"tag_id": 1
}


## Section Three (gettign list of notes public and users private):

_To get users all notes_

```json

http://127.0.0.1:5000/api/notes

```

_To get all users public notes all notes_

```json

http://127.0.0.1:5000/api/all-notes

```

_To get users all notes filtered by notes tag_

```json

http://127.0.0.1:5000/api/notes

```

_To get all users public notes filtered by notes tag_

```json

http://127.0.0.1:5000/api/all-notes

```

### Sample Login payload for POST and PUT request


{
"message": "note created from postman Three",
"public": false,
"tag_id": 1
}


## License

This project is released under [MITlicense](https://www.mit.edu/~amini/LICENSE.md)

````
