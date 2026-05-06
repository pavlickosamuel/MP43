import tkinter as tk, random
win = tk.Tk()
win.title("Pyrotechnik")
colors = ["green", "red", "gray", "blue", "orange"]
random.shuffle(colors) # pridali sme zamiesanie farieb
sirka = 15 # pridali sme upravovanie sirky
dlzka = 400 # pridali sme upravovanie dlzky
wires = []
time = 60
stop = False
canvas = tk.Canvas(width=600, height=600, bg='white')
canvas.pack()
canvas.create_text(300, 150, text="Pyrotechnik", font=("Arial", 20, "bold"), fill="magenta4")
canvas.create_text(300, 170, text="Vyber správny káblik", font=("Arial", 12, "bold"), fill="black")
hodiny = canvas.create_text(300, 400, text=time, font=("Arial", 20, "bold"), fill="magenta4")

def checker(event):
    global stop
    objects = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)
    if winner in objects:
        canvas.create_text(300, 300, text="Vyhral si!", font=("Arial", 20, "bold"), fill="magenta4")
        stop = True
    else:
        canvas.create_text(300, 300, text="Prehral si!", font=("Arial", 20, "bold"), fill="magenta4")
        stop = True
        
def timer():
    global time
    time = time - 1
    canvas.itemconfig(hodiny, text=time)
    if time > 0 and not stop:
        canvas.after(1000, timer)
    else:
        canvas.create_text(300, 300, text="Prehral si!", font=("Arial", 20, "bold"), fill="magenta4")

for i in range(0, len(colors)):
    wires.append(canvas.create_rectangle(100,200 + i* sirka, 100 + dlzka,200 + sirka + i* sirka, fill=colors[i], outline = "black", width = 2))
winner = random.choice(wires)

canvas.bind("<Button-1>", checker)

timer()
win.mainloop()