from flask import render_template, request, redirect, url_for, flash
from app.routes import bp_records
from app.models.record import Record
from app.models.category import Category
from app.models.setting import Setting

@bp_records.route('/', methods=['GET'])
def list_records():
    """
    顯示紀錄列表：
    1. 接收查詢參數 (例如月份、類別)
    2. 呼叫 Record.get_all(filters)
    3. 渲染 templates/records/index.html
    """
    pass

@bp_records.route('/new', methods=['GET'])
def new_record():
    """
    顯示新增紀錄表單：
    1. 取得所有類別供下拉選單使用
    2. 渲染 templates/records/form.html
    """
    pass

@bp_records.route('/', methods=['POST'])
def create_record():
    """
    建立新紀錄：
    1. 接收表單資料並驗證
    2. 存入資料庫
    3. 檢查是否超出當月預算，若超額產生提醒
    4. 重導向回紀錄列表
    """
    pass

@bp_records.route('/<int:id>/edit', methods=['GET'])
def edit_record(id):
    """
    顯示編輯紀錄表單：
    1. 透過 id 取得特定紀錄，找不到則回傳 404
    2. 取得所有類別
    3. 渲染 templates/records/form.html 並帶入現有資料
    """
    pass

@bp_records.route('/<int:id>/update', methods=['POST'])
def update_record(id):
    """
    更新紀錄：
    1. 接收表單資料並驗證
    2. 透過 id 更新特定紀錄
    3. 重導向回紀錄列表
    """
    pass

@bp_records.route('/<int:id>/delete', methods=['POST'])
def delete_record(id):
    """
    刪除紀錄：
    1. 透過 id 刪除紀錄
    2. 顯示成功訊息並重導向回紀錄列表
    """
    pass
