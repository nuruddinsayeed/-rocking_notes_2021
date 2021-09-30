from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from rocking_notes import auth

from rocking_notes.models import Note, Tag, NotesTags


#########################################################################
####################### Notes List api Resource classes #################
#########################################################################

User = auth.get_user_model()


def note_dictionary(notes):
    """Convert Note object to Dictionary"""
    notes_list = []
    for note in notes:
        tags = []
        if note.tags:
            tags = [tag.tag_name for tag in note.tags]
        notes_list.append({
            'user': note.user.username,
            'tags': tags,
            'message': note.message,
            'public': note.public
        })
    return notes_list


class AllPublicNotes(Resource):
    """Response all public notes"""

    def get(self):
        """Hndle GET request"""
        notes_public = Note.select().where(Note.public)

        if notes_public:
            notes = note_dictionary(notes_public)

            return {'All Notes': notes}
        # If notes database is impty
        return {'notes': None}, 404


class NotesByTagPublic(Resource):
    """provite all users node on specifiq tag"""

    def get(self, tag_name):
        try:
            tag = Tag.get(tag_name=tag_name)
        except Exception as e:
            return 'Tag Not Found!', 400

        if tag:

            notes = (Note
                     .select()
                     .where(Note.public)  # Selecting all public notes
                     .join(NotesTags)
                     .join(Tag)
                     .where(Tag.tag_name == tag_name))
            # notes = Note.select().join(Tag).where(Tag.tag_name == tag_name)
            return {tag_name: note_dictionary(notes)}
        return 'No notes related to this tag found', 400


#########################################################################
######### All Classes that requires JWT token authentication ############
#########################################################################
class AllUserNotes(Resource):
    """Response All User Notes"""

    # user = auth.get_user_model().get(1)

    @jwt_required()
    def get(self):
        """Response all users Notes"""

        user = get_jwt_identity()  # returns user data dictionary
        user = auth.get_user_model().get(username=user.get('username'))

        # user_nts = Note.select().join(User).where(
        #     User.username == user.get('username'))

        # usr_nts = Note.select().join(User).where(User.username == 'sayed')

        user_notes = Note.select().where(Note.user == user)

        if user_notes:
            return {"Your Notes": note_dictionary(user_notes)}
        return {'Your Notes': None}, 404


class NotesByTag(Resource):
    """provite all users node on specifiq tag"""

    @jwt_required()
    def get(self, tag_name):
        try:
            tag = Tag.get(tag_name=tag_name)
        except Exception as e:
            return 'Tag Not Found!', 400

        if tag:

            # fetch user to filter notes written by user
            user = get_jwt_identity()  # returns user data dictionary
            user = auth.get_user_model().get(username=user.get('username'))

            notes = (Note
                     .select()
                     .where(Note.user == user)
                     .join(NotesTags)
                     .join(Tag)
                     .where(Tag.tag_name == tag_name))
            # notes = Note.select().join(Tag).where(Tag.tag_name == tag_name)
            return {tag_name: note_dictionary(notes)}
        return 'No notes related to this tag found', 400
