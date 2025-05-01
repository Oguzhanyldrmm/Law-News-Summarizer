import psycopg2

def save_to_db(article, summaries):
        
        #connect to db
        conn = psycopg2.connect(
            dbname="hukuk",         
            user="postgres",         
            password="193807", 
            host="localhost",
            port="1905"
        )
        cur = conn.cursor()

        #sql query
        cur.execute("""
            INSERT INTO news_summaries (title, link, category, published, summary_short, summary_medium, summary_long)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            article["title"],
            article["link"],
            article["category"],
            article["published"],
            summaries[0],  #short
            summaries[1],  #medium
            summaries[2]   #long
        ))

        #save and quit
        conn.commit()
        cur.close()
        conn.close()
        print("Added to database successfully!!:", article["title"])

