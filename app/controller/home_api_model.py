from flask_restx import fields

home_get_model = {
    "filter": fields.String(description='Fetch result based on this filter'),
    "page_number": fields.Integer(description='Page number for pagination'),
    "limit": fields.Integer(description='Limit for pagination'),
}