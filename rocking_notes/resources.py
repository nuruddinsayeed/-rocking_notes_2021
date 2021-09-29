from flask_peewee.rest import RestResource


class UserResource(RestResource):
    """Define User api response"""

    fields = ['username', ]


class NoteResource(RestResource):
    """Define Tag API response"""

    include_resources = {'user': UserResource}
