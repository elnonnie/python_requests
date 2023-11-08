import customtkinter as c
from  PIL import Image
from CTkMessagebox import CTkMessagebox
import sqlite3
import requests

c.set_appearance_mode('light')

c.set_default_color_theme('green')
def load_images(image_path,size):
    img= c.CTkImage(Image.open(image_path),size=size)



def show_frame(frame):
    frame.lift()

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
        # print(main_text)
    entertainment_label.configure(text = my_news, width = 150, height = 400)

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
    business_label.configure(text = my_news, width = 150, height = 400)

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
    health_label.configure(text = my_news, width = 150, height = 400)

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
    sport_label.configure(text= my_news, width = 150, height = 400)

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
    science_label.configure(text= my_news, width = 150, height = 400)

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
    technology_label.configure(text= my_news, width = 150, height = 400)


    # for i in range(10):
    #     my_news = my_news + news_article[i] + "\n"
    #     print(i+1, news_article[i])
    
    # Create a database connection
    conn = sqlite3.connect('WASPDatabase.db')
    cursor = conn.cursor()

    # Create a table to store blog posts
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   content TEXT)''')
# def fetch_posts():
#     try:
#         response = requests.get('https://newsapi.org/v2/everything?q=keyword&apiKey=179f75ac4f624a87b516870b477bce37')
#         posts = response.json()

        # Clear existing posts in the database
        # cursor.execute('DELETE FROM posts')
        # conn.commit()

        # # Insert new posts into the database
        # for post in posts:
        #     cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
        #                    (post['title'], post['content']))
        # conn.commit()



if __name__=="__main__":
    window=c.CTk()
    # window.geometry('800x600')
    window.title('WASP BLOG')
    # window.maxsize(100, 700)
    window.minsize(800, 600)
    # window.iconbitmap('')

    
    
    #frame sections
    # top_frames = c.CTkLabel(window, text=" WASP BLOG", font= ('san sarif', 50, 'bold'))
    # top_frames.grid(row=0, column=0)

    navbar_frames = c.CTkFrame(window, fg_color='white',corner_radius=0, width= 800,height=1 )
    navbar_frames.grid(row=0, column=0, sticky= 'nsew', columnspan=2)

    menu_frames = c.CTkFrame(window, fg_color="white", corner_radius=0, width=200, height=500)
    menu_frames.grid(row=1, column=0, sticky='nsew')

    content_frames = c.CTkFrame(window, fg_color = "white", corner_radius=0, width=600)
    content_frames.grid(row=1, column=1, sticky='nsew')
    # home_frame_img =c.CTkImage(Image.open("Images/wasp.jepg"), size=(800,600))
    # im = c.CTkLabel(master= content_frames, text="",image=home_frame_img)
    # im.grid(row=0, column=0, sticky="nswe")
    content_button =c.CTkButton(menu_frames, text="Home", command=lambda: show_frame(content_frames))
    content_button.grid(row=0, column=0,pady=(10, 30))
    
    business_frame= c.CTkFrame(window, corner_radius=0, width=600)
    business_frame.grid(row=1, column=1, sticky='nsew')
    # music_frame_img =c.CTkImage(Image.open("snowflake.ico"), size=(800,600))
    # im = c.CTkLabel(master=music_frame, text="",image=music_frame_img)
    # im.grid(row=0, column=0, sticky="nswe")
    business_button =c.CTkButton(menu_frames, text="Business", command=lambda: [business_news(), show_frame(business_frame)])
    business_button.grid(row=2, column=0, pady=(0, 30))
   
    health_frame= c.CTkFrame(window, corner_radius=0, width=600)
    health_frame.grid(row=1, column=1, sticky='nsew')
    health_button =c.CTkButton(menu_frames, text= "Health", command=lambda: [health_news(), show_frame(health_frame)])
    health_button.grid(row=3, column=0, pady=(0, 30))
    
    sports_frame= c.CTkFrame(window, corner_radius=0, width=600)
    sports_frame.grid(row=1, column=1, sticky='nsew')
    sports_button =c.CTkButton(menu_frames, text="Sports News", command=lambda: [sports_news(),show_frame(sports_frame)])
    sports_button.grid(row=4, column=0, pady=(0, 30))
    
    science_frame= c.CTkFrame(window, corner_radius=0, width=600)
    science_frame.grid(row=1, column=1, sticky='nsew')
    science_buttton =c.CTkButton(menu_frames, text= "Science", command=lambda: [science_news(), show_frame(science_frame)])
    science_buttton.grid(row=5, column=0, pady=(0, 30))

    # schools_frame= c.CTkFrame(window, fg_color='green', corner_radius=0, width=600)
    # schools_frame.grid(row=1, column=1, sticky='nsew')
    # schools_button =c.CTkButton(menu_frames, text="Education", command=lambda: show_frame(schools_frame))
    # schools_button.grid(row=6, column=0, pady=(0, 30))
    
    entertainment_frame= c.CTkFrame(window, corner_radius=0, width=600)
    entertainment_frame.grid(row=1, column=1, sticky='nsew')
    entertainment_button =c.CTkButton(menu_frames, text="Entertainment\nNews", command=lambda:[entertainment(), show_frame(entertainment_frame)])
    entertainment_button.grid(row=7, column=0, pady=(0, 30))
   
    technology_frame= c.CTkFrame(window, corner_radius=0, width=600)
    technology_frame.grid(row=1, column=1, sticky='nsew')
    technology_button =c.CTkButton(menu_frames, text="Technology", command=lambda: [technology_news(), show_frame(technology_frame)])
    technology_button.grid(row=8, column=0, pady=(0, 30))
    

    #label section
    navbar_label = c.CTkLabel(navbar_frames, text= "Welcome to WASP Blog \nNews, Entertainment, Sports, Inspiration & Gossip",
                              font=('Hervertica',50))
    navbar_label.grid(row=0,column=0,padx=10, sticky="we")
    
    sport_label = c.CTkLabel(sports_frame,text= sports_news, font =('Herertica', 20))
    sport_label.grid(row=1, column=0, sticky = "we")

    entertainment_label = c.CTkLabel(entertainment_frame,  text= entertainment, font =('Herertica', 20))
    entertainment_label.grid(row=1, column=0, sticky = "we")

    business_label = c.CTkLabel(business_frame,  text= business_news, font =('Herertica', 20))
    business_label.grid(row=1, column=0, sticky = "we")

    health_label = c.CTkLabel(health_frame,  text= health_news, font =('Herertica', 20))
    health_label.grid(row=1, column=0, sticky = "we")

    science_label = c.CTkLabel(science_frame,  text= science_news, font =('Herertica', 20))
    science_label.grid(row=1, column=0, sticky = "we")

    technology_label = c.CTkLabel(technology_frame,  text= technology_news, font =('Herertica', 20))
    technology_label.grid(row=1, column=0, sticky = "we")


     #column and row configuration
    window.columnconfigure(1, weight=1)
    window.rowconfigure((0,1), weight=1)
    

    # sports_news()

    window.mainloop()