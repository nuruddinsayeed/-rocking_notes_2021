from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import request
from rocking_notes import auth

from rocking_notes.models import Tag, Note


#########################################################################
############################ Tag Section ################################
#########################################################################

class TagResoruce(Resource):

    def get(self):
        """Get all tags list"""
        tags = Tag.select()
        if tags:
            tags_list = [{tag.id: tag.tag_name} for tag in tags]
            return {"tags": tags_list}
        return "No Tags Found", 400

    def post(self):
        """Create a new tag"""

        try:
            tag_name = request.json.get('tag_name', None)

            if not tag_name:
                return 'Missing tag_name', 400

            # Create a new tag
            new_tag = Tag.create(tag_name=tag_name)
            new_tag.save()
            return {"tag": new_tag.tag_name}

        except AttributeError:
            return 'Provide an Email and Password in JSON format in the request body', 400


#########################################################################
############################ Note Section ################################
#########################################################################

# Destructure Note object
def destruc_note(note):
    return {
        'id': note.id,
        'user': note.user.username,
        'tags': [{tag.id: tag.tag_name} for tag in note.tags],
        'message': note.message,
        'public': note.public
    }


class NoteResource(Resource):
    """CRUD Notes"""

    @jwt_required()
    def get(self, id):
        "Read note detail"
        try:
            note = Note.get_by_id(id)
            if note.user.username != get_jwt_identity().get('username'):
                return "Unauthorized", 401
            return destruc_note(note)
        except Exception as e:
            return "Notes not Found", 400

    @jwt_required()
    def post(self, id):
        """Create note detail"""

        try:
            message = request.json.get('message', None)
            public = request.json.get('public', None)
            tag_id = request.json.get('tag_id', None)

            if not message:
                return 'Missing message', 400
            if public is None:
                return 'Missing public', 400
            if not tag_id:
                return 'Missing tag_id', 400

            # Getting current logged in suer by jwt token
            user = get_jwt_identity()  # returns user data dictionary
            user = auth.get_user_model().get(username=user.get('username'))
            # get tag by id
            tag = Tag.get_by_id(tag_id)

            new_note = Note.create(user=user, message=message, public=public)
            new_note.tags.add(tag)
            new_note.save()

            return destruc_note(new_note)
        except AttributeError:
            return 'Provide an message(str), public(bool), and tag_id(int) in JSON format in the request body', 400

    @jwt_required()
    def put(self, id):

        try:
            curr_username = get_jwt_identity().get('username')
            note = Note.get_by_id(id)
            if note:
                note_username = note.user.username
                if note_username != curr_username:
                    return "Unauthorized", 401

                message = request.json.get('message', None)
                public = request.json.get('public', None)
                tag_id = request.json.get('tag_id', None)

                if not message:
                    return 'Missing message', 400
                if public is None:
                    return 'Missing public', 400
                if not tag_id:
                    return 'Missing tag_id', 400

                # get tag by id
                tag = Tag.get_by_id(tag_id)
                note.message = message
                note.public = public
                note.save()
                note.tags.add(tag)

                return destruc_note(note)

            return "Notes not Found", 400
        except Exception as e:
            return 'Provide an message(str), public(bool), and tag_id(int) in JSON format in the request body', 400

    @jwt_required()
    def delete(self, id):
        try:
            curr_username = get_jwt_identity().get('username')
            note = Note.get_by_id(id)
            if note:
                note_username = note.user.username
                if note_username != curr_username:
                    return "Unauthorized", 401

            note.delete_instance()
            return {"Delete": "Note Dleteted Successfully"}
        except Exception as e:
            return "Notes not Found", 400
