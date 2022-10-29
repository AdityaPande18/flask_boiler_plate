from flask_restx import Resource, Namespace
from app.controller.home_api_model import home_get_model
from app.utils.generic_utils import parse_response

home_ns = Namespace(name="home", description="This is home route")

hom_get_model_obj = home_ns.model(name="Home Get Request", model=home_get_model)

@home_ns.route("/")
class Home(Resource):
    @home_ns.expect(hom_get_model_obj, validate=False)
    def get(self):
        '''Get the records based on filter and pagination'''
        try:
            return parse_response(status=200)
        except Exception as error:
            return parse_response(status=500, message=str(error))
