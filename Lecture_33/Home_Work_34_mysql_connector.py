import mysql.connector

db_connector = mysql.connector.connect(
    host='localhost',
    user='shchala',
    password='1234',
    database='it_step34_1'
)

db_cursor = db_connector.cursor()

# User_ების ცხრილის შექმნა
create_user_table = """
CREATE TABLE IF NOT EXISTS User (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
)
"""
db_cursor.execute(create_user_table)

# Profile ცხრილის შექმნა
create_profile_table = """
CREATE TABLE IF NOT EXISTS Profile (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    bio TEXT,
    profile_picture VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES User(id)
)
"""
db_cursor.execute(create_profile_table)

# User_ების ცხრილში მონაცემების შეტანა
user_data = [
    ('IvaneKrtvelishvili', 'Ivane@gmail.com'),
    ('AnaAkhmeteli', 'Ana@gmail.com'),
    ('DavitAbuladze', 'Abu@gmail.com'),
    ('NataDidia', 'Didia_N@gmail.com'),
    ('PetreKanchaveli', 'Kancha@gmail.com')
]
insert_user_data = "INSERT INTO User (username, email) VALUES (%s, %s)"
db_cursor.executemany(insert_user_data, user_data)

# Profile ცხრილში მონაცემების შეტანა
profile_data = [
    (1, 'Software Engineer', 'Ivane_profile.jpg'),
    (2, 'Marketing Specialist', 'Ana_profile.jpg'),
    (3, 'Footballer', 'Davit_profile.jpg'),
    (4, 'CTO', 'Nata_profile.jpg'),
    (5, 'Programmer', 'Petre_profile.jpg')
]
insert_profile_data = "INSERT INTO Profile (user_id, bio, profile_picture) VALUES (%s, %s, %s)"
db_cursor.executemany(insert_profile_data, profile_data)

db_connector.commit()