# import sqlite3, random

   
# conn = sqlite3.connect('schoolreg.db')
# cursor = conn.cursor()



# for course in range(10):
#     random.seed(10)
#     classname = "CS{}".format(course * 40)
#     value = (classname, )
#     cursor.execute("INSERT INTO courses(name) VALUES (?)", value)

# print("Courses addedd!")

# cursor.execute("SELECT * FROM courses")
# for row in cursor:
#     print(row)

# conn.close()