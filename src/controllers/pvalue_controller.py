from flask import Blueprint, jsonify
from services.pvalue_service import calculate_pvalue

pvalue_bp = Blueprint('pvalue', __name__)

@pvalue_bp.route('', methods = ['GET'])
def get_pvalue():
    pvalue = calculate_pvalue()
    return jsonify({'pvalue': pvalue})