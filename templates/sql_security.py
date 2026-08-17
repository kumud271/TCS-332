import sqlite3


DATABASE = "netsecure.db"


def setup_database():
    """Create a local demo database with sample users."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM users")

    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", "admin123")
        )

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("student", "student123")
        )

    connection.commit()
    connection.close()


def vulnerable_login(username, password):
    """
    Demonstration of an intentionally vulnerable SQL query.

    This function is ONLY for the local educational demonstration.
    """

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    query = (
        "SELECT * FROM users "
        "WHERE username = '" + username +
        "' AND password = '" + password + "'"
    )

    try:
        cursor.execute(query)
        user = cursor.fetchone()
    except sqlite3.Error as error:
        user = None
        print("SQL Error:", error)

    connection.close()

    return user


def secure_login(username, password):
    """
    Secure login using a parameterized SQL query.
    """

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    query = """
        SELECT * FROM users
        WHERE username = ? AND password = ?
    """

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    connection.close()

    return user


if __name__ == "__main__":
    setup_database()

    print("=== NetSecure SQL Injection Demonstration ===")
    print()

    username = input("Enter username: ")
    password = input("Enter password: ")

    print("\n--- Vulnerable Login ---")

    vulnerable_result = vulnerable_login(username, password)

    if vulnerable_result:
        print("Login successful.")
        print("WARNING: Vulnerable query accepted the input.")
    else:
        print("Login failed.")

    print("\n--- Secure Login ---")

    secure_result = secure_login(username, password)

    if secure_result:
        print("Login successful.")
    else:
        print("Login failed.")