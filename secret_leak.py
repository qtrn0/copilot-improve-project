API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
DB_PASSWORD = "admin123"

def connect_to_database():
    print(f"Veritabanına bağlanılıyor... Şifre: {DB_PASSWORD}")

def call_external_api():
    print(f"API çağrısı yapılıyor. Anahtar: {API_KEY[:10]}...")

def main():
    connect_to_database()
    call_external_api()

if __name__ == "__main__":
    main()