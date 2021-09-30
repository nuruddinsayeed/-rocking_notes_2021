from flask_restful import Resource
from flask import request

from rocking_notes.models import Tag


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
