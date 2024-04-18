import sqlite3

# Create a connection to the database
conn = sqlite3.connect('vivino.db')

# Enable foreign key constraints
conn.execute("PRAGMA foreign_keys = ON")

# Create a cursor object
cursor = conn.cursor()

# Define DDL statements
ddl_statements = [
    """
    CREATE TABLE reviewer (
        reviewer_id INTEGER PRIMARY KEY,
        reviews_count INTEGER,
        purchase_order_count INTEGER
    )
    """,
    """
    CREATE TABLE reviews (
        review_id INTEGER PRIMARY KEY,
        wine_id INTEGER,
        rating NUMERIC,
        note TEXT,
        language TEXT,
        reviewer_id INTEGER,
        FOREIGN KEY (wine_id) REFERENCES wines(id),
        FOREIGN KEY (reviewer_id) REFERENCES reviewer(reviewer_id)
    )
    """
]

# Execute DDL statements
for statement in ddl_statements:
    cursor.execute(statement)

# Commit changes and close the connection
conn.commit()
conn.close()