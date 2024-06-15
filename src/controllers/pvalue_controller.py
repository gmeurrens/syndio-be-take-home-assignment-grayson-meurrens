from flask import Blueprint, jsonify, request
from services.pvalue_service import calculate_pvalue, calculate_pvalue_department

pvalue_bp = Blueprint('pvalue', __name__)

@pvalue_bp.route('', methods = ['GET'])
def get_pvalue():
    dept = request.args.get('department')
    if dept is None:
        pvalue = calculate_pvalue()
        return jsonify({'pvalue': pvalue})
    else:
        pvalue = calculate_pvalue_department(dept)
        return jsonify({'pvalue': pvalue})
