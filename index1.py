import feedparser
import sqlite3
import uuid
import schedule
import time

def generate_unique_id():
    unique_id1 = str(uuid.uuid4()).replace('-', '')
    unique_id = unique_id1[:30]
    return unique_id

def fetch_rss_data():
    conn = sqlite3.connect('DBTic.db')
    c = conn.cursor()

    url1 = "https://www.ambito.com/rss/pages/home.xml"
    url2 = "http://www.ole.com.ar/rss/ultimas-noticias/"
    # url3 = "https://www.pagina12.com.ar/rss/portada"
    url4 = "https://www.perfil.com/feed"
    url5 = "https://www.telam.com.ar/rss2/ultimasnoticias.xml"

    feed1 = feedparser.parse(url1)
    feed2 = feedparser.parse(url2)
    # feed3 = feedparser.parse(url3)
    feed4 = feedparser.parse(url4)
    feed5 = feedparser.parse(url5)

    for post1 in feed1.entries:
        unique_id = generate_unique_id()
        titulos1 = post1.title
        fechas1 = post1.updated

        c.execute("SELECT * FROM Ambito_Financiero WHERE Titulo = ?", (titulos1,))
        existing_entry = c.fetchone()
        if existing_entry:
            continue  

        sentencia_sql1 = "INSERT INTO Ambito_Financiero (ID, Fecha, Titulo) VALUES (?, ?, ?)"
        valores1 = (unique_id, fechas1, titulos1)
        c.execute(sentencia_sql1, valores1)

    for post2 in feed2.entries:
        unique_id = generate_unique_id()
        titulos2 = post2.title
        fechas2 = post2.updated

        c.execute("SELECT * FROM Ole WHERE Titulo = ?", (titulos2,))
        existing_entry = c.fetchone()
        if existing_entry:
            continue  

        sentencia_sql2 = "INSERT INTO Ole (ID, Fecha, Titulo) VALUES (?, ?, ?)"
        valores2 = (unique_id, fechas2, titulos2)
        c.execute(sentencia_sql2, valores2)

    # for post3 in feed3.entries:
    #     unique_id = generate_unique_id()
    #     titulos3 = post3.title
    #     fechas3 = post3.updated

    #     c.execute("SELECT * FROM Pagina12 WHERE Titulo = ?", (titulos2,))
    #     existing_entry = c.fetchone()
    #     if existing_entry:
    #         continue  

    #     sentencia_sql3 = "INSERT INTO Pagina12 (ID, Fecha, Titulo) VALUES (?, ?, ?)"
    #     valores3 = (unique_id, fechas3, titulos3)
    #     c.execute(sentencia_sql3, valores3)

    for post4 in feed4.entries:
        unique_id = generate_unique_id()
        titulos4 = post4.title
        fechas4 = post4.updated

        c.execute("SELECT * FROM Perfil WHERE Titulo = ?", (titulos4,))
        existing_entry = c.fetchone()
        if existing_entry:
            continue  

        sentencia_sql4 = "INSERT INTO Perfil (ID, Fecha, Titulo) VALUES (?, ?, ?)"
        valores4 = (unique_id, fechas4, titulos4)
        c.execute(sentencia_sql4, valores4)

    for post5 in feed5.entries:
        unique_id = generate_unique_id()
        titulos5 = post5.title
        fechas5 = post5.updated

        c.execute("SELECT * FROM Telam WHERE Titulo = ?", (titulos5,))
        existing_entry = c.fetchone()
        if existing_entry:
            continue  

        sentencia_sql5 = "INSERT INTO Telam (ID, Fecha, Titulo) VALUES (?, ?, ?)"
        valores5 = (unique_id, fechas5, titulos5)
        c.execute(sentencia_sql5, valores5)

    conn.commit()
    conn.close()

def schedule_rss_fetch():
    schedule.every().day.at("06:00", "12:00", "18:00", "00:00").do(fetch_rss_data)

fetch_rss_data()

def run_scheduled_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)  

schedule_rss_fetch()
run_scheduled_tasks()


