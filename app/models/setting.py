from app.models.database import get_db

class Setting:
    @staticmethod
    def get_value(key, default=None):
        db = get_db()
        cursor = db.execute("SELECT value FROM settings WHERE key = ?", (key,))
        result = cursor.fetchone()
        db.close()
        return result['value'] if result else default

    @staticmethod
    def set_value(key, value):
        db = get_db()
        db.execute(
            "INSERT INTO settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (key, str(value))
        )
        db.commit()
        db.close()
