import tkinter as tk
from PIL import Image, ImageTk
import requests

def clear():
    e1.delete(0, tk.END)

def weather():
    city = e1.get()
    api_key = "e93752e69a3bcfd7698e59441f032855"  # Your API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            weather_result.config(text="City not found!", fg="red")
        else:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result = f"Temperature: {temp}°C\nWeather: {desc}\nHumidity: {humidity}%\nWind: {wind} m/s"
            weather_result.config(text=result, fg="black")

    except Exception as e:
        weather_result.config(text="Error fetching data", fg="red")

root = tk.Tk()
root.title("WEATHER PREDICTION")
root.geometry("500x500")
root.resizable(False, False)

# Background image
img = Image.open(r"C:\\Users\\Lenovo\\OneDrive\\Pictures\\Saved Pictures\\w.JPG").resize((500, 500))
final_img = ImageTk.PhotoImage(img)
labelx = tk.Label(root, image=final_img)
labelx.image = final_img
labelx.place(x=0, y=0)

# City label
l1 = tk.Label(root, text="ENTER CITY", bg="white", fg="blue", font="arial 12 bold")
l1.place(x=200, y=80)

# Entry field
e1 = tk.Entry(root, width=15, font="arial 18 bold")
e1.place(x=150, y=140)

# Search button
b1 = tk.Button(root, text="SEARCH", bg="sky blue", fg="blue", font="arial 15 bold", command=weather)
b1.place(x=150, y=210)

b2=tk.Button(root,text="clear",bg="white",fg="black",font="arial 15 bold",command=clear)
b2.place(x=280,y=210)


# Weather result label
weather_result = tk.Label(root, text="", bg="white", font="arial 12 bold", justify="left")
weather_result.place(x=150, y=280)

root.mainloop()
