import mysql.connector

HOST_DB = "localhost"
USER_DB = "root"
PASSWORD = ""
DATABASE = "dev_team"

cnx = mysql.connector.connect(user=USER_DB, password=PASSWORD,
                              host=HOST_DB,
                              database=DATABASE)

print(cnx)

insert_developer = """
INSERT INTO developers
(developer_id, developer_name)
VALUES ( %s, %s )
"""

reviewers_records = [
    ("123", "Tomas"),
]
"""
with cnx.cursor() as cursor:
    cursor.executemany(insert_developer,
                       reviewers_records)
    cnx.commit()
"""

show_developers = "DESCRIBE developers"
with cnx.cursor() as cursor:
    cursor.execute(show_developers)
    # Fetch rows from last executed query
    result = cursor.fetchall()
    for row in result:
        print(row)

print("")

select_developers = "SELECT * FROM developers LIMIT 5"
with cnx.cursor() as cursor:
    cursor.execute(select_developers)
    result = cursor.fetchall()
    for row in result:
        print(row)