import customtkinter as c
from PIL import Image
import requests
import sqlite3

# Initialize the customtkinter window
window = c.CTk()
window.title("WASP BLOG")
window.geometry("800x600")


# Create a function to switch to a specific frame
def show_frame(frame):
    frame.lift()

def general_news():
    api_key ="179f75ac4f624a87b516870b477bce37"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=general&apiKey="+api_key
    news = requests.get(url).json()
    
    articles = news["articles"]

    news_article = []
    my_news =""

    for arti in articles:
        news_article.append(arti["title"])

    for i in range(len(news_article)):
        my_news = my_news +str(i+1)+ "." +news_article[i] + "\n" 

        main_text = (i+1, news_article[i])
        # print(main_text)
    general_label.configure(text = my_news, width = 50, height = 200)

def entertainment():
    api_key ="179f75ac4f624a87b516870b477bce37"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=entertainment&apiKey="+api_key
    news = requests.get(url).json()

    articles = news["articles"]

    news_article = []
    my_news =""

    for arti in articles:
        news_article.append(arti["title"])

    for i in range(len(news_article)):
        my_news = my_news +str(i+1)+ "." +news_article[i] + "\n" 

        main_text = (i+1, news_article[i])
        for items1 in main_text:
            # sport_label.configure(text= my_news, width = 150, height = 400)
        # print(main_text)
            entertainment_label.configure(text = my_news, width = 50, height = 200)

    conn = sqlite3.connect('WASPDatabase.db')
    cursor = conn.cursor()

    # Create a table to store blog posts
    cursor.execute('''CREATE TABLE IF NOT EXISTS entertainment
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   content TEXT)''')
    cursor.execute("INSERT INTO entertainment (title, content) VALUES (?, ?)", (my_news, items1))
    conn.commit()



def business_news():
    api_key ="179f75ac4f624a87b516870b477bce37"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=business&apiKey="+api_key
    news = requests.get(url).json()
    
    articles = news["articles"]

    news_article = []
    my_news =""

    for arti in articles:
        news_article.append(arti["title"])

    for i in range(len(news_article)):
        my_news = my_news +str(i+1)+ "." +news_article[i] + "\n" 

        main_text = (i+1, news_article[i])
        # print(main_text)
    business_label.configure(text = my_news, width = 50, height = 200)

def health_news():
    api_key ="179f75ac4f624a87b516870b477bce37"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=health&apiKey="+api_key
    news = requests.get(url).json()
    
    articles = news["articles"]

    news_article = []
    my_news =""

    for arti in articles:
        news_article.append(arti["title"])

    for i in range(len(news_article)):
        my_news = my_news +str(i+1)+ "." +news_article[i] + "\n" 

        main_text = (i+1, news_article[i])
        # print(main_text)
    health_label.configure(text = my_news, width = 50, height = 200)

def sports_news():
    api_key ="179f75ac4f624a87b516870b477bce37"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=sports&apiKey="+api_key
    news = requests.get(url).json()
    
    articles = news["articles"]
    news_article = []
    my_news =""

    for arti in articles:
        main = news_article.append(arti["title"])
        # print(main)
    for i in range(len(news_article)):
        my_news = my_news + str(i+1) + "." + news_article[i] +"\n"
        main_text = (i +1, news_article[i])
    sport_label.configure(text= my_news, width = 50, height = 200)


def science_news():
    api_key ="179f75ac4f624a87b516870b477bce37"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=science&apiKey="+api_key
    news = requests.get(url).json()
    
    articles = news["articles"]
    news_article = []
    my_news =""

    for arti in articles:
        main = news_article.append(arti["title"])
        # print(main)
    for i in range(len(news_article)):
        my_news = my_news + str(i+1) + "." + news_article[i] +"\n"
        main_text = (i +1, news_article[i])
    science_label.configure(text= my_news, width = 50, height = 200)

def technology_news():
    api_key ="179f75ac4f624a87b516870b477bce37"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=technology&apiKey="+api_key
    news = requests.get(url).json()
    
    articles = news["articles"]
    news_article = []
    my_news =""

    for arti in articles:
        main = news_article.append(arti["title"])
        # print(main)
    for i in range(len(news_article)):
        my_news = my_news + str(i+1) + "." + news_article[i] +"\n"
        main_text = (i +1, news_article[i])
    technology_label.configure(text= my_news, width = 50, height = 200)

# Create the main window layout
navbar_frame = c.CTkFrame(window, fg_color="white", corner_radius=0, width=800, height=100)
# navbar_frame.pack(fill="x")
navbar_frame.grid(row=0, column=0, sticky= 'nsew', columnspan=2)

content_frame = c.CTkFrame(window, fg_color="#722F37", corner_radius=0)
# content_frame.pack(fill="both", expand=True)
content_frame.grid(row=1, column=0, sticky='nsew')

# Create buttons for different categories
general_frame=c.CTkFrame(window, corner_radius=0, width=600)
general_frame.grid(row=1, column=0, sticky='nsew')
general_button = c.CTkButton(navbar_frame, text="General", command=lambda: [general_news(), show_frame(general_frame)])
general_button.grid(row=0, column=0, padx=12, pady=12)

entertainment_frame= c.CTkFrame(window, corner_radius=0, width=600)
entertainment_frame.grid(row=1, column=0, sticky='nsew')
entertainment_button = c.CTkButton(navbar_frame, text="Entertainment", command=lambda: [entertainment(), show_frame(entertainment_frame)])
entertainment_button.grid(row=0, column=1, padx=12, pady=12)

technology_frame= c.CTkFrame(window, corner_radius=0, width=600)
technology_frame.grid(row=1, column=0, sticky='nsew')
technology_button =c.CTkButton(navbar_frame, text="Technology", command=lambda: [technology_news(), show_frame(technology_frame)])
technology_button.grid(row=0, column=2, padx=12, pady=12)

science_frame= c.CTkFrame(window, corner_radius=0, width=600)
science_frame.grid(row=1, column=0, sticky='nsew')
science_buttton =c.CTkButton(navbar_frame, text= "Science", command=lambda: [science_news(), show_frame(science_frame)])
science_buttton.grid(row=0, column=3, padx=12, pady=12)

sports_frame= c.CTkFrame(window, corner_radius=0, width=600)
sports_frame.grid(row=1, column=0, sticky='nsew')
sports_button = c.CTkButton(navbar_frame, text="Sports", command=lambda: [sports_news(), show_frame(sports_frame)])
sports_button.grid(row=0, column=4, padx=12, pady=12)

health_frame= c.CTkFrame(window, corner_radius=0, width=600)
health_frame.grid(row=1, column=0, sticky='nsew')
health_button =c.CTkButton(navbar_frame, text= "Health", command=lambda: [health_news(), show_frame(health_frame)])
health_button.grid(row=0, column=5, padx=12, pady=20)


business_frame= c.CTkFrame(window, corner_radius=0, width=600)
business_frame.grid(row=1, column=0, sticky='nsew')
business_button =c.CTkButton(navbar_frame, text="Business", command=lambda: [business_news(), show_frame(business_frame)])
business_button.grid(row=0, column=6, padx=10, pady=10)

# Create a label to display news
general_label = c.CTkLabel(general_frame,text= general_news, font =('Herertica', 20), justify="left")
general_label.grid(row=0, column=0, sticky = "nswe", padx=100, pady=100)

sport_label = c.CTkLabel(sports_frame,text= sports_news, font =('Herertica', 20), justify="left")
sport_label.grid(row=0, column=0, sticky = "nswe", padx=100, pady=100)

entertainment_label = c.CTkLabel(entertainment_frame,  text= entertainment, font =('Herertica', 20), justify="left")
entertainment_label.grid(row=0, column=0, sticky = "nswe", padx=100, pady=100)

business_label = c.CTkLabel(business_frame,  text= business_news, font =('Herertica', 20), justify="left")
business_label.grid(row=0, column=0, sticky = "nswe", padx=100, pady=100)

health_label = c.CTkLabel(health_frame,  text= health_news, font =('Herertica', 20), justify="left")
health_label.grid(row=0, column=0, sticky = "nswe", padx=100, pady=100)

science_label = c.CTkLabel(science_frame,  text= science_news, font =('Herertica', 20), justify="left")
science_label.grid(row=0, column=0, sticky = "nswe", padx=100, pady=100)

technology_label = c.CTkLabel(technology_frame,  text= technology_news, font =('Herertica', 20), justify="left")
technology_label.grid(row=0, column=0, sticky = "nswe", padx=100, pady=100)

# Configure column and row weights
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# Show the window
window.mainloop()
