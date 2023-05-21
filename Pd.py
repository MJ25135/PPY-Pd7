import tkinter as tk
from tkinter import ttk
import mysql
from mysql import connector
import Student

root = tk.Tk()
treeview = ttk.Treeview(root)
treeview["columns"] = (
    "id", "name", "surname", "email", "project", "l_1", "l_2", "l_3", "h_1", "h_2", "h_3", "h_4", "h_5",
    "h_6",
    "h_7", "h_8", "h_9", "h_10", "grade", "status")
treeview.column("#0", width=0, )
treeview.heading("id", text="ID", )
treeview.heading("name", text="Imie")
treeview.heading("surname", text="Nazwisko")
treeview.heading("email", text="Email")
treeview.heading("project", text="Projekt")
treeview.heading("l_1", text="l_1", )
treeview.heading("l_2", text="l_2")
treeview.heading("l_3", text="l_3")
treeview.heading("h_1", text="h_1")
treeview.heading("h_2", text="h_2")
treeview.heading("h_3", text="h_3")
treeview.heading("h_4", text="h_4")
treeview.heading("h_5", text="h_5")
treeview.heading("h_6", text="h_6")
treeview.heading("h_7", text="h_7")
treeview.heading("h_8", text="h_8")
treeview.heading("h_9", text="h_9")
treeview.heading("h_10", text="h_10")
treeview.heading("grade", text="Ocena")
treeview.heading("status", text="Status")

treeview.column("id", width=50)
treeview.column("name", )
treeview.column("surname", width=150)
treeview.column("email")
treeview.column("project", width=50)
treeview.column("l_1", width=50)
treeview.column("l_2", width=50)
treeview.column("l_3", width=50)
treeview.column("h_1", width=50)
treeview.column("h_2", width=50)
treeview.column("h_3", width=50)
treeview.column("h_4", width=50)
treeview.column("h_5", width=50)
treeview.column("h_6", width=50)
treeview.column("h_7", width=50)
treeview.column("h_8", width=50)
treeview.column("h_9", width=50)
treeview.column("h_10", width=50)
treeview.column("grade", width=80)
treeview.column("grade", width=80)
treeview.column("status", width=100)


def connect():
    return mysql.connector.connect(
        host="db4free.net",
        user="s25135",
        password="Hiaber123",
        database="bazappy")


def fetch_data() -> list[tuple]:
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def load_data():
    data = fetch_data()

    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert("", "end", values=(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
            row[13], row[14], row[15], row[16], row[17], row[18], row[19]))


def add_new_Student():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj nowego Studenta")

    name_label = ttk.Label(new_window, text="Imie:")
    name_label.pack()
    name_entry = ttk.Entry(new_window)
    name_entry.pack()

    surname_label = ttk.Label(new_window, text="Nazwisko:")
    surname_label.pack()
    surname_entry = ttk.Entry(new_window)
    surname_entry.pack()

    email_label = ttk.Label(new_window, text="Email:")
    email_label.pack()
    email_entry = ttk.Entry(new_window)
    email_entry.pack()

    def add_new():
        name = name_entry.get()
        surname = surname_entry.get()
        email = email_entry.get()

        new_student = Student.Student(name, surname, email)

        try:
            conn = connect()

            cursor = conn.cursor()
            sql = "INSERT INTO `Student`(Name, Surname, email, project, l_1, l_2, l_3, h_1, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9, h_10, grade, STATUS)" \
                  " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

            params = [new_student.name, new_student.surname, new_student.email]
            for key in new_student.all_grade.keys():
                params.append(new_student.all_grade[key])
            params.append(new_student.status)

            cursor.execute(sql, params)
            conn.commit()

        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        load_data()

        new_window.destroy()

    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()


def delete_student():
    new_window = tk.Toplevel(root)
    new_window.title("Usuń Studenta")
    id_label = ttk.Label(new_window, text="ID:")
    id_label.pack()
    id_entry = ttk.Entry(new_window)
    id_entry.pack()

    def delete():
        _id = id_entry.get()
        conn = connect()
        cursor = conn.cursor()
        sql = "delete from Student where id = %s;"
        cursor.execute(sql, tuple(_id))
        conn.commit()
        cursor.close()
        conn.close()
        load_data()
        new_window.destroy()

    add_button = ttk.Button(new_window, text="Usuń", command=delete)
    add_button.pack()


def update_student_marks():
    new_window = tk.Toplevel(root)
    new_window.title("Zmień oceny")

    id_label = ttk.Label(new_window, text="ID:")
    id_label.pack()
    id_entry = ttk.Entry(new_window)
    id_entry.pack()

    project_label = ttk.Label(new_window, text="Projekt:")
    project_label.pack()
    project_entry = ttk.Entry(new_window)
    project_entry.pack()

    l_1_label = ttk.Label(new_window, text="l_1:")
    l_1_label.pack()
    l_1_entry = ttk.Entry(new_window)
    l_1_entry.pack()

    l_2_label = ttk.Label(new_window, text="l_2:")
    l_2_label.pack()
    l_2_entry = ttk.Entry(new_window)
    l_2_entry.pack()

    l_3_label = ttk.Label(new_window, text="l_2:")
    l_3_label.pack()
    l_3_entry = ttk.Entry(new_window)
    l_3_entry.pack()

    h_1_label = ttk.Label(new_window, text="h_1:")
    h_1_label.pack()
    h_1_entry = ttk.Entry(new_window)
    h_1_entry.pack()

    h_2_label = ttk.Label(new_window, text="h_2:")
    h_2_label.pack()
    h_2_entry = ttk.Entry(new_window)
    h_2_entry.pack()

    h_3_label = ttk.Label(new_window, text="h_3:")
    h_3_label.pack()
    h_3_entry = ttk.Entry(new_window)
    h_3_entry.pack()

    h_4_label = ttk.Label(new_window, text="h_4:")
    h_4_label.pack()
    h_4_entry = ttk.Entry(new_window)
    h_4_entry.pack()

    h_5_label = ttk.Label(new_window, text="h_5:")
    h_5_label.pack()
    h_5_entry = ttk.Entry(new_window)
    h_5_entry.pack()

    h_6_label = ttk.Label(new_window, text="h_6:")
    h_6_label.pack()
    h_6_entry = ttk.Entry(new_window)
    h_6_entry.pack()

    h_7_label = ttk.Label(new_window, text="h_7:")
    h_7_label.pack()
    h_7_entry = ttk.Entry(new_window)
    h_7_entry.pack()

    h_8_label = ttk.Label(new_window, text="h_8:")
    h_8_label.pack()
    h_8_entry = ttk.Entry(new_window)
    h_8_entry.pack()

    h_9_label = ttk.Label(new_window, text="h_9:")
    h_9_label.pack()
    h_9_entry = ttk.Entry(new_window)
    h_9_entry.pack()

    h_10_label = ttk.Label(new_window, text="h_10:")
    h_10_label.pack()
    h_10_entry = ttk.Entry(new_window)
    h_10_entry.pack()

    grade_label = ttk.Label(new_window, text="Ocena:")
    grade_label.pack()
    grade_entry = ttk.Entry(new_window)
    grade_entry.pack()

    def update():
        _id = id_entry.get()
        project = project_entry.get()
        l_1 = l_1_entry.get()
        l_2 = l_2_entry.get()
        l_3 = l_3_entry.get()
        h_1 = h_1_entry.get()
        h_2 = h_2_entry.get()
        h_3 = h_3_entry.get()
        h_4 = h_4_entry.get()
        h_5 = h_5_entry.get()
        h_6 = h_6_entry.get()
        h_7 = h_7_entry.get()
        h_8 = h_8_entry.get()
        h_9 = h_9_entry.get()
        h_10 = h_10_entry.get()

        if int(project) > 40:
            project = 40

        if int(l_1) > 20:
            l_1 = 20
        if int(l_2) > 20:
            l_2 = 20
        if int(l_3) > 20:
            l_3 = 20

        if int(h_1) > 100:
            h_1 = 100
        if int(h_2) > 100:
            h_2 = 100
        if int(h_3) > 100:
            h_3 = 100
        if int(h_4) > 100:
            h_4 = 100
        if int(h_5) > 100:
            h_5 = 100
        if int(h_6) > 100:
            h_6 = 100
        if int(h_7) > 100:
            h_7 = 100
        if int(h_8) > 100:
            h_8 = 100
        if int(h_9) > 100:
            h_9 = 100
        if int(h_10) > 100:
            h_10 = 100

        grade = 2
        status = ""
        if int(project) > 0 and int(l_1) > 0 and int(l_2) > 0 and int(l_3) > 0 \
                and int(h_1) > 0 and int(h_2) > 0 and int(h_3) > 0 and int(h_4) > 0 and int(h_5) > 0 and int(h_6) > 0 and int(h_7) > 0 and int(h_8) > 0 and int(h_9) > 0 and int(h_10) > 0:
            grade = grade_entry.get()
            status ='Graded'

        conn = connect()

        cursor = conn.cursor()
        sql = "update Student set project = %s, l_1 = %s, l_2 = %s, l_3 = %s," \
              " h_1 = %s, h_2 = %s, h_3 = %s, h_4 = %s, h_5 = %s, h_6 = %s, h_7 = %s, h_8 = %s, h_9 = %s, h_10 = %s, grade = %s, status = %s" \
              " where id = %s;"

        cursor.execute(sql, (project, l_1, l_2, l_3, h_1, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9, h_10, grade, status, _id))


        conn.commit()
        cursor.close()
        conn.close()

        load_data()

        new_window.destroy()

    add_button = ttk.Button(new_window, text="Zmień", command=update)
    add_button.pack()


add_button = tk.Button(root, text="Dodaj Studenta", command=add_new_Student)
delete_button = tk.Button(root, text="Usuń Studenta", command=delete_student)
delete_button.config(background='red')
update_button = tk.Button(root, text="Zmień oceny", command=update_student_marks)

treeview.pack(side='top')
add_button.pack(side='left')
delete_button.pack(side='left')
update_button.pack(side='left')

load_data()

root.mainloop()
