from flask import render_template, request
from app.routes import bp_analytics
from app.models.record import Record

@bp_analytics.route('/', methods=['GET'])
def index():
    """
    顯示統計分析圖表：
    1. 接收查詢參數 (如欲查詢的月份、收入或支出)
    2. 從資料庫撈取並按類別分群彙總金額
    3. 渲染 templates/analytics/index.html
    """
    pass
