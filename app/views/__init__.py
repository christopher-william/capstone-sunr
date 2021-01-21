from flask import Flask
from flask_restful import Api

from .seller_view import SellerLogin, SellerRegister
from .message_view import Message
from .hsp_view import HspUf
from .lead_view import LeadView , LeadMessages


def configure(app: Flask):

    api = Api(app)
    api.add_resource(SellerRegister, '/register')
    api.add_resource(SellerLogin, '/login')
    api.add_resource(Message, '/message', '/message/<int:message_id>')
    api.add_resource(HspUf, '/hsp', '/hsp/<string:uf>')
    api.add_resource(LeadView, '/lead')
    api.add_resource(LeadMessages,'/lead/<int:lead_id>')
