CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('income', 'expense'))
);

CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- 預設類別資料 (使用 INSERT OR IGNORE 避免重複執行報錯)
INSERT OR IGNORE INTO categories (id, name, type) VALUES (1, '餐飲', 'expense');
INSERT OR IGNORE INTO categories (id, name, type) VALUES (2, '交通', 'expense');
INSERT OR IGNORE INTO categories (id, name, type) VALUES (3, '娛樂', 'expense');
INSERT OR IGNORE INTO categories (id, name, type) VALUES (4, '購物', 'expense');
INSERT OR IGNORE INTO categories (id, name, type) VALUES (5, '薪水', 'income');
INSERT OR IGNORE INTO categories (id, name, type) VALUES (6, '投資', 'income');
