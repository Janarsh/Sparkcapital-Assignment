import mysql.connector


class Crud:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="user1",
            password="password@123",
            database="mydb"
        )
        self.cursor = self.mydb.cursor()

    def create(self, user):
        query = "insert into user values(NULL, %s, %s)"
        values = (user.name, user.address)

        self.cursor.execute(query, values)
        self.mydb.commit()
        self.mydb.close()
        return self.cursor.lastrowid

    def read(self, user_id):
        query = "select * from user where user_id = %s"
        values = (user_id, )

        self.cursor.execute(query, values)
        user = self.cursor.fetchone()
        self.mydb.close()
        return user

    def update(self, user):
        query = "update user set name = %s, address = %s where user_id = %s"
        values = (user.name, user.address, user.user_id)

        self.cursor.execute(query, values)
        self.mydb.commit()
        self.mydb.close()
        return self.cursor.rowcount >= 1

    def delete(self, user_id):
        query = "delete from user where user_id = %s"
        values = (user_id,)

        self.cursor.execute(query, values)
        self.mydb.commit()
        self.mydb.close()
        return self.cursor.rowcount >= 1
