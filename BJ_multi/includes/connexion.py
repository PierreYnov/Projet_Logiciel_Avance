from tkinter import *
import sqlite3
import subprocess

window = Tk()
window.geometry("330x150")
window.title('Rejoins nous')
window.config(background='green')


def login():
    def login_database():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM test WHERE email=? AND password=?", (e1.get(), e2.get()))
        row = cur.fetchall()
        conn.close()
        print(row)
        if row != []:
            user_name = row[0][1]
            l3.config(text="Connexion réussie au compte : " + user_name, background='green', fg='yellow')
            text_file = open("test.txt", "wt")
            n = text_file.write(user_name)
            text_file.close()
            subprocess.call(['python', 'start.py'])
            window.destroy()

        else:
            l3.config(text="Mauvais mot de passe", fg='yellow')

    window.destroy()
    login_window = Tk()
    login_window.title('Page de connexion')
    login_window.config(background='green')
    login_window.geometry("700x250")
    l1 = Label(login_window, text="Adresse mail", font="times 20", background='green', fg='yellow')
    l1.grid(row=1, column=1)
    l2 = Label(login_window, text="Mot de passe", font="times 20", background='green', fg='yellow')
    l2.grid(row=2, column=1)
    l3 = Label(login_window, font="times 20", background='green')
    l3.grid(row=5, column=2)

    email_text = StringVar()
    e1 = Entry(login_window, textvariable=email_text)
    e1.grid(row=1, column=2)
    password_text = StringVar()
    e2 = Entry(login_window, textvariable=password_text, show='*')
    e2.grid(row=2, column=2)

    b1 = Button(login_window, text="Se connecter", width=20, command=login_database, background='green', fg='yellow')
    b1.grid(row=4, column=2)
    login_window.mainloop()


def signup():
    def signup_database():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
        cur.execute("INSERT INTO test Values(Null,?,?,?)", (e1.get(), e2.get(), e3.get()))
        l4 = Label(signup_window, text="Compte créé avec succès !", font="times 15", background='green', fg='yellow')
        l4.grid(row=7, column=2)
        conn.commit()
        conn.close()

    def retour_menu():
        def login_database():
            conn = sqlite3.connect("1.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM test WHERE email=? AND password=?", (e1.get(), e2.get()))
            row = cur.fetchall()
            conn.close()
            print(row)
            if row != []:
                user_name = row[0][1]
                l3.config(text="Connexion réussie au compte : " + user_name, background='green', fg='yellow')
                text_file = open("test.txt", "wt")
                n = text_file.write(user_name)
                text_file.close()
                subprocess.call(['python', 'start.py'])


            else:
                l3.config(text="Mauvais mot de passe", fg='yellow')


        login_window = Tk()
        login_window.title('Page de connexion')
        login_window.config(background='green')
        login_window.geometry("700x250")
        l1 = Label(login_window, text="Adresse mail", font="times 20", background='green', fg='yellow')
        l1.grid(row=1, column=1)
        l2 = Label(login_window, text="Mot de passe", font="times 20", background='green', fg='yellow')
        l2.grid(row=2, column=1)
        l3 = Label(login_window, font="times 20", background='green')
        l3.grid(row=5, column=2)

        email_text = StringVar()
        e1 = Entry(login_window, textvariable=email_text)
        e1.grid(row=1, column=2)
        password_text = StringVar()
        e2 = Entry(login_window, textvariable=password_text, show='*')
        e2.grid(row=2, column=2)

        b1 = Button(login_window, text="Se connecter", width=20, command=login_database, background='green',
                    fg='yellow')
        b1.grid(row=4, column=2)
        login_window.mainloop()

    window.destroy()
    signup_window = Tk()
    signup_window.title('Enregistre-toi')
    signup_window.config(background='green')

    signup_window.geometry("400x250")
    l1 = Label(signup_window, text="Pseudo", font="times 20", background='green', fg='yellow')
    l1.grid(row=1, column=1)
    l2 = Label(signup_window, text="Adresse mail", font="times 20", background='green', fg='yellow')
    l2.grid(row=2, column=1)
    l3 = Label(signup_window, text="Mot de passe", font="times 20", background='green', fg='yellow')
    l3.grid(row=3, column=1)

    name_text = StringVar()
    e1 = Entry(signup_window, textvariable=name_text)
    e1.grid(row=1, column=2)
    email_text = StringVar()
    e2 = Entry(signup_window, textvariable=email_text)
    e2.grid(row=2, column=2)
    password_text = StringVar()
    e3 = Entry(signup_window, textvariable=password_text)
    e3.grid(row=3, column=2)

    b1 = Button(signup_window, text="Créer le compte", width=20, command=signup_database, background='green',
                fg='yellow')
    b1.grid(row=4, column=2)

    b2 = Button(signup_window, text="Connectez-vous", width=20, command=retour_menu, background='green',
                fg='yellow')
    b2.grid(row=6, column=2)


l1 = Label(window, text="Connectez vous au Blackjack", font="times 20", background='green', fg='yellow')
l1.grid(row=1, column=2, columnspan=2)

b1 = Button(window, text="Se connecter", width=20, command=login, background='green', fg='yellow')
b1.grid(row=2, column=2)

b2 = Button(window, text="S'enregistrer", width=20, command=signup, background='green', fg='yellow')
b2.grid(row=2, column=3)

window.mainloop()
