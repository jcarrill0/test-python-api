from flask import Flask, jsonify, request, Blueprint
from services.service import Service
from utils.utils import validate_min_date

INDICATOR_TYPE_UF = 'uf'

api = Blueprint('api', __name__)

@api.route('/indicator/<string:date>', methods=['GET'])
def get_uf_indicator_by_date(date):
    try:
        if validate_min_date(date):
            return jsonify({'error': 'La fecha debe ser superior o igual a 01-01-2013'}), 400
        
        service = Service(INDICATOR_TYPE_UF, date)
        data = service.get_info_by_date()
            
        return jsonify({'valor': data.get('valor')})
    except:
        return jsonify({'error': 'Fecha no valida!!'}), 400