# import module
import sqlite3

# Connect database
conn = sqlite3.connect('example.db')
c = conn.cursor()


# Create table
def create_table():
    c.execute("CREATE TABLE stocks(id, data)")


# Insert a row of data
def insert_data():
    c.execute("INSERT INTO stocks VALUES (1, 'hello')")
    aaa = 2
    bbb = 'apple'
    c.execute("INSERT INTO stocks(id, data) VALUES (?, ?)" , [aaa, bbb])


# Select a row of data
def select_data():
    c.execute("SELECT * FROM stocks")
    for row in c:
        print(str(row[0]) + ' : ' + row[1])


# Select a row of data
def select_data2():
    c.execute("SELECT * FROM stocks")
    for id, data in c.fetchall():
        print('%s = %s' % (id, data))


# Delete data
def delete_data():
    c.execute("DELETE FROM stocks WHERE id = 1")
    c.execute("DELETE FROM stocks WHERE id = 2")


# Save and close
def save_close():
    # Save (commit) the changes
    conn.commit()
    # Close database
    conn.close()


# main
if __name__ == '__main__':
    # create_table()
    insert_data()
    select_data()
    delete_data()
    select_data2()
    save_close()
