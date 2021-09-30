# from flask_peewee.rest import RestResource, RestrictOwnerResource


# class UserResource(RestrictOwnerResource):
#     """Define User api response"""

#     fields = ['username', ]


# class TagResource(RestrictOwnerResource):
#     """Define Not tag respose"""
#     fields = ['tag_name', ]


# class NoteResource(RestrictOwnerResource):
#     """Define Tag API response (All Public)"""

#     fields = ['user', 'message', 'public', ]

#     include_resources = {
#         'user': UserResource,
#     }

#     def get_query(self):
#         return self.model.select().where(self.model.public)
