import sqlite3
import os

# 資料庫檔案路徑：專案根目錄/instance/ledger.db
DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'instance', 'ledger.db')

def get_db():
    """取得資料庫連線"""
    db = sqlite3.connect(DATABASE_PATH)
    # 讓回傳的資料可以使用類似字典的方式存取 (例如 row['id'])
    db.row_factory = sqlite3.Row
    return db

def init_db():
    """初始化資料庫 (建立資料表與預設資料)"""
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    db = get_db()
    schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'schema.sql')
    
    with open(schema_path, 'r', encoding='utf-8') as f:
        db.executescript(f.read())
        
    db.commit()
    db.close()
