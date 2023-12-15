

TABLE_FOOD = """
    CREATE TABLE IF NOT EXISTS food (
        foodId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount REAL NOT NULL,
        unity VARCHAR(2) NOT NULL,
        kcal REAL NOT NULL,
        protein REAL,
        carbohydrate REAL,
        fat REAL,
        weight REAL,
        weightUnity TEXT,
        createdAt DATETIME NOT NULL,
        updateAt DATETIME
    );
    """