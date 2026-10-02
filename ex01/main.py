from tkinter import *
import requests

def get_quote():
    try:
        response = requests.get("https://api.kanye.rest", timeout=10)
        response.raise_for_status()
        data = response.json()
        canvas.itemconfig(quote_text, text=data["quote"])
    except requests.exceptions.RequestException as e:
        canvas.itemconfig(quote_text, text=f"Couldn't fetch quote.\n{e}")



window = Tk()
window.title("Kanye Says...")
window.config(bg="white")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)
get_quote()



kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg="white")
kanye_button.grid(row=1, column=0)



window.mainloop()