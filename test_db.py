from app.models.database import init_db
from app.models.category import Category
from app.models.record import Record
from app.models.setting import Setting

def test():
    print("Initializing database...")
    init_db()
    print("Database initialized.")

    print("\n--- Testing Category ---")
    categories = Category.get_all()
    print(f"Categories found: {len(categories)}")
    for c in categories:
        print(c)

    print("\n--- Testing Setting ---")
    Setting.set_value("monthly_budget", "10000")
    budget = Setting.get_value("monthly_budget")
    print(f"Monthly budget: {budget}")

    print("\n--- Testing Record ---")
    record_id = Record.create({
        "amount": 150.5,
        "date": "2026-04-23",
        "description": "Lunch",
        "category_id": 1 # 餐飲
    })
    print(f"Created record ID: {record_id}")
    
    records = Record.get_all()
    print(f"Records found: {len(records)}")
    for r in records:
        print(r)
        
    summary = Record.get_monthly_summary("2026-04")
    print(f"Monthly summary: {summary}")

if __name__ == "__main__":
    test()
