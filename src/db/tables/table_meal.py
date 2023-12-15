
TABLE_MEAL = """
    CREATE TABLE IF NOT EXISTS meal (
        mealId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        weight REAL,
        weightUnity VARCHAR(2),
        totalProtein REAL,
        totalCarbohydrate REAL,
        totalFat REAL,
        totalKcal REAL,
        createdAt DATETIME NOT NULL,
        updateAt DATETIME
    );
""" 