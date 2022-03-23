# save a variable to a database function

def saveToDatabase (type, thought) :
    import sqlite3
    conn = sqlite3.connect('masterbrain.db')
    c = conn.cursor()
    c.execute("INSERT INTO idea (type, thought) VALUES (?, ?)", (type, thought))
    conn.commit()
    conn.close()

saveToDatabase("test", "test")


