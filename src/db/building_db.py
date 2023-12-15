import sqlite3

from tables import table_food, table_meal, table_foods

# class Database:
    
def create_tables():
    conn = sqlite3.connect('diet_calculator.db')
    conn.execute("PRAGMA foreign_keys = ON")

    cursor = conn.cursor()

    cursor.execute(table_food.TABLE_FOOD)
    cursor.execute(table_meal.TABLE_MEAL)
    cursor.execute(table_foods.TABLE_FOODS)

    
    conn.close()

def building_db():
    try:
        create_tables()
        
    except Exception as e:
        print(e)


if __name__ == '__main__':
    building_db()

