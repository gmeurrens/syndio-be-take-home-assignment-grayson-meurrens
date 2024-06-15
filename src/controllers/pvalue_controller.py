from flask import Blueprint, jsonify, request
from services.pvalue_service import calculate_pvalue

pvalue_bp = Blueprint('pvalue', __name__)

@pvalue_bp.route('', methods = ['GET'])
def get_pvalue():
    dept = request.args.get('department')
    pvalue = calculate_pvalue(dept)
    
    return jsonify({'pvalue': pvalue})
