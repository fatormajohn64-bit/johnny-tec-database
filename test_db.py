import sqlite3
import os

DB_PATH = "database/johnny_tec.db"
SCHEMA_PATH = "sql/schema.sql"
SEED_PATH = "sql/seed.sql"

def run_test():
    # Ensure database directory exists
    os.makedirs("database", exist_ok=True)
    
    # Connect to SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Enable Foreign Key support
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    print("--- 1. Executing Schema ---")
    if os.path.exists(SCHEMA_PATH):
        with open(SCHEMA_PATH, "r") as f:
            cursor.executescript(f.read())
        print("✓ Tables created successfully.")
    else:
        print(f"✗ File missing: {SCHEMA_PATH}")
        return

    print("\n--- 2. Executing Seed Data ---")
    if os.path.exists(SEED_PATH):
        with open(SEED_PATH, "r") as f:
            cursor.executescript(f.read())
        print("✓ Seed data inserted successfully.")
    else:
        print(f"✗ File missing: {SEED_PATH}")

    print("\n--- 3. Database Verification Query ---")
    
    # Fetch Developers
    developers = cursor.execute("SELECT id, name, username, role FROM developers").fetchall()
    print(f"\n[Developers Table - {len(developers)} Records]")
    for dev in developers:
        print(f"  ID: {dev[0]} | Name: {dev[1]} | Username: {dev[2]} | Role: {dev[3]}")

    # Fetch Users
    users = cursor.execute("SELECT id, name, email, country FROM users").fetchall()
    print(f"\n[Users Table - {len(users)} Records]")
    for u in users:
        print(f"  ID: {u[0]} | Name: {u[1]} | Email: {u[2]} | Country: {u[3]}")

    # Fetch Conversations
    chats = cursor.execute("SELECT user_id, user_message, ai_response FROM conversations").fetchall()
    print(f"\n[Conversations Table - {len(chats)} Records]")
    for c in chats:
        print(f"  User {c[0]}: Prompt='{c[1]}' -> Response='{c[2]}'")

    conn.commit()
    conn.close()
    print("\n✓ Database test finished with 0 errors!")

if __name__ == "__main__":
    run_test()
      
