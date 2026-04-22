from app.models.database import get_db

class Record:
    @staticmethod
    def get_all(filters=None):
        db = get_db()
        query = """
            SELECT r.*, c.name as category_name, c.type as category_type
            FROM records r
            JOIN categories c ON r.category_id = c.id
            WHERE 1=1
        """
        params = []
        
        if filters:
            if 'year_month' in filters:
                query += " AND strftime('%Y-%m', r.date) = ?"
                params.append(filters['year_month'])
            if 'category_id' in filters:
                query += " AND r.category_id = ?"
                params.append(filters['category_id'])
                
        query += " ORDER BY r.date DESC, r.created_at DESC"
        
        cursor = db.execute(query, params)
        records = cursor.fetchall()
        db.close()
        return [dict(row) for row in records]

    @staticmethod
    def get_by_id(record_id):
        db = get_db()
        cursor = db.execute("""
            SELECT r.*, c.name as category_name, c.type as category_type
            FROM records r
            JOIN categories c ON r.category_id = c.id
            WHERE r.id = ?
        """, (record_id,))
        record = cursor.fetchone()
        db.close()
        return dict(record) if record else None

    @staticmethod
    def create(data):
        db = get_db()
        cursor = db.execute(
            "INSERT INTO records (amount, date, description, category_id) VALUES (?, ?, ?, ?)",
            (data['amount'], data['date'], data.get('description', ''), data['category_id'])
        )
        db.commit()
        record_id = cursor.lastrowid
        db.close()
        return record_id

    @staticmethod
    def update(record_id, data):
        db = get_db()
        db.execute(
            "UPDATE records SET amount = ?, date = ?, description = ?, category_id = ? WHERE id = ?",
            (data['amount'], data['date'], data.get('description', ''), data['category_id'], record_id)
        )
        db.commit()
        db.close()

    @staticmethod
    def delete(record_id):
        db = get_db()
        db.execute("DELETE FROM records WHERE id = ?", (record_id,))
        db.commit()
        db.close()

    @staticmethod
    def get_monthly_summary(year_month):
        """取得特定月份的總收入、總支出與結餘 (格式: 'YYYY-MM')"""
        db = get_db()
        cursor = db.execute("""
            SELECT 
                SUM(CASE WHEN c.type = 'income' THEN r.amount ELSE 0 END) as total_income,
                SUM(CASE WHEN c.type = 'expense' THEN r.amount ELSE 0 END) as total_expense
            FROM records r
            JOIN categories c ON r.category_id = c.id
            WHERE strftime('%Y-%m', r.date) = ?
        """, (year_month,))
        
        result = cursor.fetchone()
        db.close()
        
        income = result['total_income'] or 0
        expense = result['total_expense'] or 0
        
        return {
            'total_income': income,
            'total_expense': expense,
            'balance': income - expense
        }
