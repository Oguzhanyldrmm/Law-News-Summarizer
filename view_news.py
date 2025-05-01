import psycopg2

def get_categories():
    conn = psycopg2.connect(
        dbname="hukuk",
        user="postgres",
        password="193807",
        host="localhost",
        port="1905"
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT category FROM news_summaries")
    categories = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return categories

def get_summaries(selected_category):
    conn = psycopg2.connect(
        dbname="hukuk",
        user="postgres",
        password="193807",
        host="localhost",
        port="1905"
    )
    cur = conn.cursor()
    cur.execute("SELECT title, category,link,  summary_medium, summary_long FROM news_summaries ORDER BY published DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    print("\n🧾 Haberler:\n")

    for title, category,link, medium, long_ in rows:
        print(f"📌 Başlık: {title}")
        print(f"📂 Kategori: {category}")
        if category == selected_category:
            print(f"📝 Uzun Özet:\n{long_}\n")
        else:
            print(f"📄 Orta Özet:\n{medium}\n")
        print(f"Linke tıklayarak habere ulaşabilirsiniz: {link}")
        print("-" * 60)


print("📚 Veritabanındaki kategoriler:")
categories = get_categories()
for i, cat in enumerate(categories, start=1):
    print(f"{i}. {cat}")

selected = input("Lütfen ilgilendiğiniz kategori adını yazın (örneğin: Kararlar): ").strip().upper()
while selected not in categories:
    print(" Geçersiz kategori seçimi, yedinen deneyin!")
    selected = input("Lütfen ilgilendiğiniz kategori adını yazın (örneğin: Kararlar): ").strip().upper()

else:
    get_summaries(selected)
