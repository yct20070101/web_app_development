from flask import render_template, request, redirect, url_for, flash
from app.routes import bp_main
from app.models.record import Record
from app.models.setting import Setting

@bp_main.route('/')
def index():
    """
    顯示首頁 (Dashboard)：
    1. 取得當月總收支與結餘
    2. 取得預算設定
    3. 計算預算達成率並決定是否顯示警告
    4. 渲染 templates/main/index.html
    """
    pass

@bp_main.route('/settings', methods=['GET'])
def settings():
    """
    顯示設定頁面：
    1. 取得目前設定的每月預算
    2. 渲染 templates/main/settings.html
    """
    pass

@bp_main.route('/settings/budget', methods=['POST'])
def update_budget():
    """
    更新預算設定：
    1. 從 POST 表單接收 budget
    2. 儲存至資料庫
    3. 重導向回設定頁面並顯示成功訊息
    """
    pass
