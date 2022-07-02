import tkinter as root
from tkinter import messagebox

import requests as req

api_key = '0d0b783531888a92d1935c41b29e0529'

frame = root.Tk()
frame.title('weather webApp')
frame.geometry('900x500')
frame.resizable(False, False)



def weatherForcast():
    # print('Hello there')
    # print('city = ' + str(textSearchbar.get()))
    # print(location)
    # location = 'delhi'
    try:
        location = textSearchbar.get()
        location = location.lower()
        webLink = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + api_key
        api_link = req.get(webLink)
        apidata = api_link.json()
        print(api_link)
        condition = apidata['weather'][0]['main']
        description = apidata['weather'][0]['description']
        temp = int(apidata['main']['temp'] - 273.15)
        pressure = apidata['main']['pressure']
        humidity = apidata['main']['humidity']
        wind = apidata['wind']['speed']

        tempLabel.config(text=(str(temp)+ ' °C'))
        c.config(text=(condition, '|', 'Feels', 'Like', (str(temp) , " °")), font=('arial', 20, 'bold'))
        dotsw.config(text=(wind))
        dotsd.config(text=description)
        dotsp.config(text=pressure)
        # currentTime.config(text=(str(datetime.now().hour) + ' ' + str(datetime.now().minute)))
        # currentTime.config(text=datetime.now())
        dotsh.config(text=humidity)

    except Exception as e:
        root.messagebox.showerror('Weather App', 'Invalid arguements')


# search box
search_bar_image = root.PhotoImage(file='search1.png')
searchImage = root.Label(image=search_bar_image).place(x=20, y=20)

textSearchbar = root.Entry(frame,
                           justify='center',
                           width=17, font=('poppins ', 25, 'bold'),
                           bg='#404040', border=0, fg='white')
textSearchbar.place(x=50, y=40)
textSearchbar.focus()

searchSymbol = root.PhotoImage(file='search_icon.png')
searchIcon = root.Button(image=searchSymbol,
                         borderwidth=0,
                         cursor='hand2',
                         bg='#404040',
                         command=weatherForcast
                         )
searchIcon.place(x=800, y=33.5)

# logo image
logo_image = root.PhotoImage(file='logo3.png')
logo = root.Label(image=logo_image)
logo.place(x=150, y=110)

# botttom
bottom_image = root.PhotoImage(file='box.png')
box_image = root.Label(image=bottom_image)
box_image.pack(padx=5, pady=5, side='bottom')
# box_image.place()

labelw = root.Label(frame, text='WIND', font=('Helvetia', 15, 'bold'), fg='white', bg='#1ab5ef')
labelw.place(x=120, y=400)

labelh = root.Label(frame, text='HUMIDITY', font=('Helvetia', 15, 'bold'), fg='white', bg='#1ab5ef')
labelh.place(x=250, y=400)

labeld = root.Label(frame, text='DESCRIPTION', font=('Helvetia', 15, 'bold'), fg='white', bg='#1ab5ef')
labeld.place(x=430, y=400)

labelp = root.Label(frame, text='PRESSURE', font=('Helvetia', 15, 'bold'), fg='white', bg='#1ab5ef')
labelp.place(x=650, y=400)

currentWeatherLabel = root.Label(frame, text='CURRENT WEATHER', font=('Helvetia', 15, 'bold'))
currentWeatherLabel.place(x=40, y=90)
currentTime= root.Label(frame , font=('Helvetia', 20)).place(x=30 , y=130)
# currentTime.config(text=datetime.now())
tempLabel = root.Label(font=('arial', 60, 'bold'), fg='#ee666d')
tempLabel.place(x=400, y=150)

c = root.Label(font=('arial', 70, 'bold'))
c.place(x=400, y=250)

dotsw = root.Label(text='...', font=('arial', 15, 'bold'), bg='#1ab5ef')
dotsw.place(x=120, y=430)

dotsh = root.Label(text='...', font=('arial', 15, 'bold'), bg='#1ab5ef')
dotsh.place(x=280, y=430)

dotsd = root.Label(text='...', justify='center', font=('arial', 15, 'bold'), bg='#1ab5ef')
dotsd.place(x=470, y=430)

dotsp = root.Label(text='...', font=('arial', 15, 'bold'), bg='#1ab5ef')
dotsp.place(x=670, y=430)





frame.mainloop()
