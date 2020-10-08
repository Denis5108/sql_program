import sqlite3
import random, sys

conn = sqlite3.connect('schoolreg.db')
cursor = conn.cursor()

# create student
cursor.execute('''
        CREATE TABLE IF NOT EXISTS students
        (id                    integer primary key,
        name             char(255) NOT NULL,
        Age                    int,
        Address          char(255),
        email            char(255));

''')

# create course
cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses
        (courseID                  integer primary key,
         name                       char(255) NOT NULL);
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS data
        (student_id             integer,
         course_id              integer,
         data_name              char(255))
''')

# for course in range(10):
#     random.seed(10)
#     classname = "CS{}".format(course)
#     value = (classname, )
#     cursor.execute("INSERT INTO courses(name) VALUES (?)", value)


cursor = conn.execute("SELECT * from Students")
# add some classes into the mix

def profileCreation():

    name = str(input("What is your name? "))
    for row in cursor:
        if (name == row[1]):
            print("You are logged in to the system")
            return [name]

    age = int(input("What is your age? "))
    address = str(input("What is your current address? "))
    email   = str(input("What is your current email? "))

    values = (name, age, address, email)
    cursor.execute("INSERT INTO Students(name, age, address, email) VALUES(?,?,?,?)", values)


    print("User Created, welcome to your page!!")
 
    return [name, age, address, email]

user = profileCreation()
def editProfile():
    cursor.execute("SELECT * FROM Students")
    for record in cursor.fetchall():
        if (record[1] == user[0]):
            print("\n1.student ID: {} \
                   \n2.student Name: {} \
                   \n3.student Age: {} \
                   \n4.student Address: {} \
                   \n5.student email: {}".format(record[0], 
                   record[1], record[2], record[3], record[4]))

    print("\nType '0' if you don't want to edit a value")
    edit = int(input("Which value do you want to edit > "))

    selection = ("id","name","age","address","email")
    if (edit != 0):
        if (selection[edit - 1] == "age" or selection[edit - 1] == "id"):
            if (selection[edit - 1] == "id"):
                _id = int(input("'{}' > ".format(selection[edit - 1])))
                value = (_id,)
                cursor.execute("UPDATE Students SET id = ?", value)
            else:
                _age = int(input("'{}' > ".format(selection[edit - 1])))
                value = (_age,)
                cursor.execute("UPDATE Students SET age = ?", value)
        else:
            if (selection[edit - 1] == "name"):
                _name = str(input("'{}' > ".format(selection[edit - 1])))
                value = (_name,)
                cursor.execute("UPDATE Students SET name = ?", value)
            if (selection[edit - 1] == "address"):
                _addr = str(input("'{}' > ".format(selection[edit - 1])))
                value = (_addr,)
                cursor.execute("UPDATE Students SET address = ?", value)
            else:
                _email = str(input("'{}' > ".format(selection[edit - 1])))
                value = (_email,)
                cursor.execute("UPDATE Students SET email = ?", value)

    print("'{}' has been changed".format(selection[edit - 1]))

def viewCourses():
    student_id = int(input("What is your student id > "))
    values = (student_id, )


    cursor.execute("SELECT courses.name,\
    data.data_name FROM data INNER JOIN courses\
    ON data.course_id == courses.courseID WHERE \
    data.student_id == ?", values)

    print("Here are your courses {}".format(user[0]))
    for record in cursor.fetchall():
        print("{} - {}".format(record[0], record[1]))

def addCourses():
    cursor.execute("SELECT * FROM courses")

    # Show all courses
    for record in cursor.fetchall():
        print("course id: {},  course name: {}".format(record[0], record[1]))

    student_id = int(input("Please enter your id > "))
    course_id  = int(input("Select a course id > "))
    course     = str(input("Choose a course > "))
    values     = (student_id, course_id, course)

    cursor.execute("INSERT INTO data VALUES (?,?,?)", values)
    print("Added Courses for the semester go in here.")

def dropCourses():
    viewCourses()
    course_name = str(input("Please select a course to delete > "))
    values = (course_name, )
    cursor.execute("DELETE FROM data WHERE data_name = ?", values)
    print("Course Dropped.")

def deleteUser():
    cursor.execute("SELECT name FROM students")
    for record in cursor.fetchall():
        print(" users {}". format(record[0]))

    name = str(input("> "))    
    values = (name, )
    cursor.execute("DELETE FROM data WHERE data_name = ?", values)
    cursor.execute("DELETE FROM students WHERE  name = ?", values)
    print("All Course Dropped.")
    print("Username deleted out of the system")
    conn.close()
    sys.exit()

def locateAddDropCourse():
    print("\n1.Add Course\
           \n2.Drop Course")

    rspnse = int(input("> "))
    if (rspnse == 1):
        addCourses()

    if (rspnse == 2):
        dropCourses()

def homepage():
    print("Welcome, {}".format(user[0]))
    print("\
        \n1.Add/Drop Courses\
        \n2.View Courses\
        \n3.Edit Profile\
        \n4.Delete User\
        \n5.Exit")


def main():
    response = " "
    while (response != 5):
    
        homepage()
        response = int(input("> "))

        if (response == 1):
            locateAddDropCourse()
        if (response == 2):
            viewCourses()
        if (response == 3):
            editProfile()
        if (response == 4):
            deleteUser()

        print("Total changes '{}' ".format(conn.total_changes))
        conn.commit()

if __name__ == "__main__":
    main()

print("--- logged out ---")
conn.commit
conn.close()