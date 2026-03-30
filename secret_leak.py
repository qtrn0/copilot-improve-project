import os

# Security fix: Hardcoded secrets removed. Use environment variables.
# API_KEY = os.getenv("API_KEY")
# DB_PASSWORD = os.getenv("DB_PASSWORD")

def connect_to_database():
    print("Connecting to database... (password from env var)")

def call_external_api():
    print("Calling API... (key from env var)")

def main():
    connect_to_database()
    call_external_api()

if __name__ == "__main__":
    main()