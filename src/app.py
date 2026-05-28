"""
VulnScout test app — intentionally vulnerable for testing.
DO NOT use this code in production.
"""
import os
import sqlite3
import subprocess
import pickle


DB_PASSWORD = "s3cret_p@ss!2024"
API_SECRET_KEY = "sk-live-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

SALT = "hardcoded_salt_value_12345"


def login(username: str, password: str):
    """User login endpoint — contains SQL injection vulnerability."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    return cursor.fetchone()


def run_shell(cmd: str):
    """Run a shell command — contains command injection."""
    os.system("ping " + cmd)


def run_process(cmd: str):
    """Run subprocess — contains command injection via shell=True."""
    subprocess.call(cmd, shell=True)


def calculate(expr: str):
    """Evaluate a mathematical expression — contains code injection."""
    result = eval(expr)
    return result


def load_session(data: bytes):
    """Load session data — contains insecure deserialization."""
    return pickle.loads(data)


def render_template(name: str) -> str:
    """Render a greeting — safe function, no vulnerability."""
    return f"Hello, {name}! Welcome to our platform."


def generate_report(data: dict) -> str:
    """Generate a report string — safe function."""
    import json
    return json.dumps(data, indent=2)
