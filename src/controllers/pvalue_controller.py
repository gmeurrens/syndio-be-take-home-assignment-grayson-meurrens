from flask import Blueprint, jsonify

pvalue_bp = Blueprint('pvalue', __name__)

@pvalue_bp.route('', methods = ['GET'])
def get_pvalue():
    return jsonify({'pvalue': 'test value'})