import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Connessione al database MySQL
db = mysql.connector.connect(
    host="hostname",
    user="username",
    password="password",
    database="nomedatabase"
)

# Variabile globale per la finestra principale
main_window = None

# Variabili globali per gli entry field
nome_entry = None
quantita_entry = None
prezzo_entry = None
codice_entry = None
item_list = None

# Funzione per il login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Eseguire la verifica delle credenziali nel database
    cursor = db.cursor()
    query = "SELECT * FROM utenti WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        # Se le credenziali sono corrette, apri la finestra principale
        show_main_window()
        login_window.destroy()
    else:
        # Altrimenti, mostra un messaggio di errore
        messagebox.showerror("Errore di accesso", "Credenziali non valide")

    cursor.close()

# Funzione per aggiungere un nuovo oggetto al magazzino
def add_item():
    nome = nome_entry.get()
    quantita = quantita_entry.get()
    prezzo = prezzo_entry.get()
    codice = codice_entry.get()

    # Eseguire l'inserimento dei dati nel database
    cursor = db.cursor()
    query = "INSERT INTO magazzino (nome, quantita, prezzo, codice) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome, quantita, prezzo, codice))
    db.commit()

    messagebox.showinfo("Oggetto aggiunto", "Oggetto aggiunto con successo")

    cursor.close()

    # Aggiorna la lista degli oggetti nel pannello principale
    show_items()

# Funzione per eliminare l'oggetto selezionato nella tabella degli oggetti
def delete_item():
    selection = item_list.selection()
    if selection:
        # Ottenere l'ID dell'oggetto selezionato
        item_id = item_list.item(selection)['values'][0]

        # Eseguire l'eliminazione dell'oggetto dal database
        cursor = db.cursor()
        query = "DELETE FROM magazzino WHERE id = %s"
        cursor.execute(query, (item_id,))
        db.commit()

        messagebox.showinfo("Oggetto eliminato", "Oggetto eliminato con successo")

        cursor.close()

        # Rimuovere l'oggetto dalla tabella nella GUI
        item_list.delete(selection)
    else:
        messagebox.showerror("Errore di eliminazione", "Seleziona un oggetto da eliminare")

# Funzione per mostrare la finestra principale
def show_main_window():
    global main_window
    main_window = Tk()
    main_window.title("StoragePlus - Gestione Magazzino")
    main_window.geometry("960x360")

    # Creazione della tabella degli oggetti con Treeview
    global item_list
    item_list = ttk.Treeview(main_window, columns=("ID", "Nome", "Quantità", "Prezzo", "Codice"), show="headings")

    # Definizione delle colonne della tabella
    item_list.heading("ID", text="ID")
    item_list.heading("Nome", text="Nome")
    item_list.heading("Quantità", text="Quantità")
    item_list.heading("Prezzo", text="Prezzo")
    item_list.heading("Codice", text="Codice")

    item_list.pack()

    # Bottone per eliminare un oggetto
    delete_button = Button(main_window, text="Elimina oggetto", command=delete_item)
    delete_button.pack()

    # Bottone per aggiungere un oggetto
    add_button = Button(main_window, text="Aggiungi oggetto", command=show_add_item_form)
    add_button.pack()

    # Bottone per modificare un oggetto
    edit_button = Button(main_window, text="Modifica oggetto", command=show_edit_item_form)
    edit_button.pack()

    # Mostrare la lista degli oggetti nella tabella
    show_items()


# Funzione per mostrare il form per aggiungere un oggetto
def show_add_item_form():
    global add_item_window
    add_item_window = Toplevel(main_window)
    add_item_window.title("Aggiungi Oggetto")
    add_item_window.geometry("400x300")

    # Etichetta e campo di input per il nome
    nome_label = Label(add_item_window, text="Nome:")
    nome_label.pack()
    global nome_entry
    nome_entry = Entry(add_item_window)
    nome_entry.pack()

    # Etichetta e campo di input per la quantità
    quantita_label = Label(add_item_window, text="Quantità:")
    quantita_label.pack()
    global quantita_entry
    quantita_entry = Entry(add_item_window)
    quantita_entry.pack()

    # Etichetta e campo di input per il prezzo
    prezzo_label = Label(add_item_window, text="Prezzo:")
    prezzo_label.pack()
    global prezzo_entry
    prezzo_entry = Entry(add_item_window)
    prezzo_entry.pack()

    # Etichetta e campo di input per il codice
    codice_label = Label(add_item_window, text="Codice:")
    codice_label.pack()
    global codice_entry
    codice_entry = Entry(add_item_window)
    codice_entry.pack()

    # Bottone per confermare l'aggiunta
    confirm_button = Button(add_item_window, text="Conferma", command=add_item)
    confirm_button.pack()

# Funzione per mostrare il form per modificare un oggetto
def show_edit_item_form():
    selection = item_list.selection()
    if selection:
        # Ottenere l'ID dell'oggetto selezionato
        item_id = item_list.item(selection)['values'][0]

        # Eseguire la query per ottenere i dati dell'oggetto dal database
        cursor = db.cursor()
        query = "SELECT * FROM magazzino WHERE id = %s"
        cursor.execute(query, (item_id,))
        item = cursor.fetchone()

        # Mostrare il form di modifica dell'oggetto
        global edit_item_window
        edit_item_window = Toplevel(main_window)
        edit_item_window.title("Modifica Oggetto")
        edit_item_window.geometry("400x300")

        # Etichetta e campo di input per il nome
        nome_label = Label(edit_item_window, text="Nome:")
        nome_label.pack()
        global nome_entry
        nome_entry = Entry(edit_item_window)
        nome_entry.insert(0, item[1])  # Inserisci il valore attuale
        nome_entry.pack()

        # Etichetta e campo di input per la quantità
        quantita_label = Label(edit_item_window, text="Quantità:")
        quantita_label.pack()
        global quantita_entry
        quantita_entry = Entry(edit_item_window)
        quantita_entry.insert(0, item[2])  # Inserisci il valore attuale
        quantita_entry.pack()

        # Etichetta e campo di input per il prezzo
        prezzo_label = Label(edit_item_window, text="Prezzo:")
        prezzo_label.pack()
        global prezzo_entry
        prezzo_entry = Entry(edit_item_window)
        prezzo_entry.insert(0, item[3])  # Inserisci il valore attuale
        prezzo_entry.pack()

        # Etichetta e campo di input per il codice
        codice_label = Label(edit_item_window, text="Codice:")
        codice_label.pack()
        global codice_entry
        codice_entry = Entry(edit_item_window)
        codice_entry.insert(0, item[4])  # Inserisci il valore attuale
        codice_entry.pack()

        # Bottone per confermare la modifica
        confirm_button = Button(edit_item_window, text="Conferma", command=update_item)
        confirm_button.pack()
    else:
        messagebox.showerror("Errore di modifica", "Seleziona un oggetto da modificare")

# Funzione per aggiornare un oggetto nel magazzino
def update_item():
    selection = item_list.selection()
    if selection:
        # Ottenere l'ID dell'oggetto selezionato
        item_id = item_list.item(selection)['values'][0]

        nome = nome_entry.get()
        quantita = quantita_entry.get()
        prezzo = prezzo_entry.get()
        codice = codice_entry.get()

        # Eseguire l'aggiornamento dei dati nel database
        cursor = db.cursor()
        query = "UPDATE magazzino SET nome = %s, quantita = %s, prezzo = %s, codice = %s WHERE id = %s"
        cursor.execute(query, (nome, quantita, prezzo, codice, item_id))
        db.commit()

        messagebox.showinfo("Oggetto modificato", "Oggetto modificato con successo")

        cursor.close()

        # Chiudi la finestra di modifica
        edit_item_window.destroy()

        # Aggiorna la lista degli oggetti nel pannello principale
        show_items()
    else:
        messagebox.showerror("Errore di modifica", "Seleziona un oggetto da modificare")

# Funzione per mostrare la lista degli oggetti nella tabella
def show_items():
    # Eseguire la query per ottenere la lista degli oggetti dal database
    cursor = db.cursor()
    query = "SELECT * FROM magazzino"
    cursor.execute(query)
    items = cursor.fetchall()

    # Pulire la lista degli oggetti
    item_list.delete(*item_list.get_children())

    # Mostrare la lista degli oggetti nella tabella
    for item in items:
        item_list.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4]))

    cursor.close()

# Finestra di login
login_window = Tk()
login_window.title("Login")

username_label = Label(login_window, text="Username:")
username_label.grid(row=0, column=0, sticky=W, padx=10, pady=5)
username_entry = Entry(login_window)
username_entry.grid(row=0, column=1)

password_label = Label(login_window, text="Password:")
password_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)
password_entry = Entry(login_window, show="*")
password_entry.grid(row=1, column=1)

login_button = Button(login_window, text="Accedi", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Mostra la finestra di login solo se è necessario
if __name__ == "__main__":
    login_window.mainloop()
