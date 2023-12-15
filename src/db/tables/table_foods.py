

TABLE_FOODS = """
    CREATE TABLE IF NOT EXISTS foods (
            amount REAL NOT NULL,
            unity VARCHAR(2) NOT NULL,
            weight REAL,
            weightUnity VARCHAR(2),
            createdAt DATETIME NOT NULL,
            updateAt DATETIME,
            foodId INTEGER NOT NULL,
            mealId Integer NOT NULL,
            FOREIGN KEY(foodId) REFERENCES food(foodId),
            FOREIGN KEY(mealId) REFERENCES meal(mealId)
    );
"""