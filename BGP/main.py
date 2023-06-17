import tkinter
import customtkinter
from pytube import YouTube
import sqlite3

def sentToBase(result):
    conn = sqlite3.connect("database.db", timeout=5)
    cursor = conn.cursor()

    table_persons = cursor.execute("SELECT * FROM persons ORDER BY idP DESC LIMIT 1")
    table_persons = table_persons.fetchall()
    resultToMoves = (table_persons[0][0],)+result

    cursor.execute("INSERT INTO moves(idP,name,link) VALUES(?,?,?)", resultToMoves)

    resultToAll = table_persons[0]+resultToMoves
    print(resultToAll)
    cursor.execute("INSERT INTO combined_table(idP, fName, sName, age, 'idP:1', name, link) VALUES(?,?,?,?,?,?,?)", resultToAll)

    conn.commit()
    conn.close()

def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()   # VS Code don't have a volume. You must open video normal (without VS Code)

        title.configure(text=ytObject.title, text_color='black')
        finishLabel.configure(text='')
        video.download()
        finishLabel.configure(text='Download!')

    except:
        finishLabel.configure(text='Download Error!', text_color='red')

    result = (ytObject.title, ytlink)
    sentToBase(result)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100

    per = str(int(percentage_of_completion))
    pProcentage.configure(text=per+'%')
    pProcentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)

# System Settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Our app frame
app = customtkinter.CTk()
app.geometry('545x280')
app.title('IM YouTube Downloader')

# Adding UI elements
title = customtkinter.CTkLabel(app, text='Insert a youtube link')
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

# Progress procentage
pProcentage = customtkinter.CTkLabel(app, text='0%')
pProcentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack(padx=10, pady=10)