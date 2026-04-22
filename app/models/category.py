from app.models.database import get_db

class Category:
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.execute("SELECT * FROM categories ORDER BY id")
        categories = cursor.fetchall()
        db.close()
        return [dict(row) for row in categories]

    @staticmethod
    def get_by_id(category_id):
        db = get_db()
        cursor = db.execute("SELECT * FROM categories WHERE id = ?", (category_id,))
        category = cursor.fetchone()
        db.close()
        return dict(category) if category else None

    @staticmethod
    def create(name, type_):
        db = get_db()
        cursor = db.execute(
            "INSERT INTO categories (name, type) VALUES (?, ?)",
            (name, type_)
        )
        db.commit()
        category_id = cursor.lastrowid
        db.close()
        return category_id

    @staticmethod
    def update(category_id, name, type_):
        db = get_db()
        db.execute(
            "UPDATE categories SET name = ?, type = ? WHERE id = ?",
            (name, type_, category_id)
        )
        db.commit()
        db.close()

    @staticmethod
    def delete(category_id):
        db = get_db()
        try:
            db.execute("DELETE FROM categories WHERE id = ?", (category_id,))
            db.commit()
            return True
        except db.IntegrityError:
            # 會拋出錯誤代表有記錄使用此類別，受限於 FOREIGN KEY 條件無法刪除
            return False
        finally:
            db.close()
