from flask import Blueprint

# 初始化 Blueprints，避免循環匯入
bp_main = Blueprint('main', __name__)
bp_records = Blueprint('records', __name__, url_prefix='/records')
bp_analytics = Blueprint('analytics', __name__, url_prefix='/analytics')

# 匯入路由定義使其註冊到 Blueprint
from app.routes import main, records, analytics

def register_blueprints(app):
    """在建立 Flask app 時呼叫，用來註冊所有的 Blueprint"""
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_records)
    app.register_blueprint(bp_analytics)
