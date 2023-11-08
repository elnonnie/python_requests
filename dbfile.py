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


def G_news():
    api_key ="179f75ac4f624a87b516870b477bce37"
    url = "https://newsapi.org/v2/top-headlines?country=ng&apiKey="+api_key
    news = requests.get(url).json()
    
    articles = news["articles"]

    

    news_article = []
    my_news =""


    for arti in articles:
        news_article.append(arti["title"])

    for i in range(len(news_article)):
        my_news = my_news +str(i+1)+ "." +news_article[i] + "\n" 

        main_text = (i+1, news_article[i])
        for items2 in main_text:
            news_label.configure(text = my_news, width = 150, height = 400)

    conn = sqlite3.connect('WASPDatabase.db')
    cursor = conn.cursor()

    # Create a table to store blog posts
    cursor.execute('''CREATE TABLE IF NOT EXISTS news
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   content TEXT)''')
    cursor.execute("INSERT INTO news (title, content) VALUES (?, ?)", (my_news, items2))
    conn.commit()


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
            entertainment_label.configure(text = my_news, width = 150, height = 400)

    conn = sqlite3.connect('WASPDatabase.db')
    cursor = conn.cursor()

    # Create a table to store blog posts
    cursor.execute('''CREATE TABLE IF NOT EXISTS entertainment
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   content TEXT)''')
    cursor.execute("INSERT INTO entertainment (title, content) VALUES (?, ?)", (my_news, items1))
    conn.commit()
    # Function to fetch posts from the API and store them in the database

def sports_news():
    global conn
    api_key ="179f75ac4f624a87b516870b477bce37"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=sports&apiKey="+api_key
    news = requests.get(url).json()
    
    articles = news["articles"]
    news_article = []
    my_news =""


    for arti in articles:
        main = news_article.append(arti["title"])
        # print(main)
    for i in range(1,10):
        my_news = my_news + str(i+1) + "." + news_article[i] +"\n"
        main_text = (i +1, news_article[i])
        for items in main_text:
            sport_label.configure(text= my_news, font=('montserat', 17), width = 150, height = 400)

    # for i in range(10):
    #     my_news = my_news + news_article[i] + "\n"
    #     print(i+1, news_article[i])
    
    # Create a database connection
    conn = sqlite3.connect('WASPDatabase.db')
    cursor = conn.cursor()

    # Create a table to store blog posts
    cursor.execute('''CREATE TABLE IF NOT EXISTS sports
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   content TEXT)''')
    cursor.execute("INSERT INTO sports (title, content) VALUES (?, ?)", (my_news, items))
    conn.commit()
    # Function to fetch posts from the API and store them in the database

def fetch_posts():
    # Fetch posts from news API
    news_response = requests.get('news_api_url')
    news_posts = news_response.json()['posts']
     # Fetch posts from entertainment API
    entertainment_response = requests.get('https://newsapi.org/v2/top-headlines?country=ng&category=entertainment&apiKey="+api_key')
    entertainment_posts = entertainment_response.json()['posts']
    # Store the posts in the database
    for post in news_posts:
        c.execute("INSERT INTO posts (title, content, image, image_url) VALUES (?, ?, ?, ?)",
                  (post['title'], post['content'], post['image'], post['image_url']))
    for post in entertainment_posts:
        c.execute("INSERT INTO posts (title, content, image, image_url) VALUES (?, ?, ?, ?)",
                  (post['title'], post['content'], post['image'], post['image_url']))
    conn.commit()
    # Commit the changes to the database
    
    # Show a success message
    CTkMessagebox(title="Success", message="Posts fetched and stored in the database!")
    

    # Function to handle storing the blog post
# def store_blog_post():
#     title =title_entry.get()
#     content = content_entry.get("1.0", "end-1c")


# def fetch_posts():
#     try:
#         response = requests.get('https://newsapi.org/v2/everything?q=keyword&apiKey=179f75ac4f624a87b516870b477bce37')
#         posts = response.json()

#         # Clear existing posts in the database
#         # cursor.execute('DELETE FROM posts')
#         # conn.commit()

#         # # Insert new posts into the database
#         # for post in posts:
#         #     cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
#         #                    (post['title'], post['content']))
#         conn.commit()



if _name=="__main_":
    window=c.CTk()
    window.geometry('940x600+250+0')
    # window.resizable(0,0)
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

    content_frames = c.CTkFrame(window,fg_color='#722F37', corner_radius=0, width=600)
    content_frames.grid(row=1, column=1, sticky='nsew')
    home_frame_img =c.CTkImage(Image.open("Images/wasp.jpeg"), size=(800,600))
    im = c.CTkLabel(master= content_frames, text="",image=home_frame_img)
    im.grid(row=0, column=0, sticky="nswe")
    content_button =c.CTkButton(menu_frames, text="Home", command=lambda: show_frame(content_frames))
    content_button.grid(row=0, column=0,pady=(10, 30))
    
    news_frames= c.CTkFrame(window, corner_radius=0, width=600)
    news_frames.grid(row=1, column=1, sticky='nsew')
    news_button =c.CTkButton(menu_frames, text="News", command=lambda: [G_news(),show_frame(news_frames)])
    news_button.grid(row=1,column=0, pady=(0,30) )
    
    music_frame= c.CTkFrame(window, fg_color='red', corner_radius=0, width=600)
    music_frame.grid(row=1, column=1, sticky='nsew')
    music_frame_img =c.CTkImage(Image.open("images/wasp.jpeg"), size=(800,600))
    im = c.CTkLabel(master=music_frame, text="",image=music_frame_img)
    im.grid(row=0, column=0, sticky="nswe")
    music_button =c.CTkButton(menu_frames, text="Music", command=lambda: show_frame(music_frame))
    music_button.grid(row=2, column=0, pady=(0, 30))
   
    video_frame= c.CTkFrame(window, fg_color='white', corner_radius=0, width=600)
    video_frame.grid(row=1, column=1, sticky='nsew')
    video_button =c.CTkButton(menu_frames, text= "Video", command=lambda: show_frame(video_frame))
    video_button.grid(row=3, column=0, pady=(0, 30))
    
    sports_frame= c.CTkFrame(window, fg_color='pink', corner_radius=0, width=600)
    sports_frame.grid(row=1, column=1, sticky='nsew')
    sports_button =c.CTkButton(menu_frames, text="Sports News", command=lambda: [sports_news(),show_frame(sports_frame)])
    sports_button.grid(row=4, column=0, pady=(0, 30))
    
    politics_frame= c.CTkFrame(window, fg_color='gold', corner_radius=0, width=600)
    politics_frame.grid(row=1, column=1, sticky='nsew')
    politics_buttton =c.CTkButton(menu_frames, text= "Politics", command=lambda: show_frame(politics_frame))
    politics_buttton.grid(row=5, column=0, pady=(0, 30))

    # schools_frame= c.CTkFrame(window, fg_color='green', corner_radius=0, width=600)
    # schools_frame.grid(row=1, column=1, sticky='nsew')
    # schools_button =c.CTkButton(menu_frames, text="Education", command=lambda: show_frame(schools_frame))
    # schools_button.grid(row=6, column=0, pady=(0, 30))
    
    entertainment_frame= c.CTkFrame(window, fg_color='brown', corner_radius=0, width=600)
    entertainment_frame.grid(row=1, column=1, sticky='nsew')
    entertainment_button =c.CTkButton(menu_frames, text="Entertainment\nNews", command=lambda:[entertainment(), show_frame(entertainment_frame)])
    entertainment_button.grid(row=7, column=0, pady=(0, 30))
   
    lifestyle_frame= c.CTkFrame(window, fg_color='yellow', corner_radius=0, width=600)
    lifestyle_frame.grid(row=1, column=1, sticky='nsew')
    lifestyle_button =c.CTkButton(menu_frames, text="Lifestyle", command=lambda: show_frame(lifestyle_frame))
    lifestyle_button.grid(row=8, column=0, pady=(0, 30))
    

    #label section
    navbar_label = c.CTkLabel(navbar_frames, text= "Welcome to WASP's Blog \nNews,Entertainment,sports,Inspiration and yes...Gossip",
                              font=('Hervertica',30))
    navbar_label.grid(row=0,column=0,padx=20, sticky="we")
    
    sport_label = c.CTkLabel(sports_frame,text= sports_news)
    sport_label.grid(row=1, column=0)

    entertainment_label = c.CTkLabel(entertainment_frame,  text= entertainment)
    entertainment_label.grid(row=1, column=0)

    news_label = c.CTkLabel(news_frames,  text= G_news)
    news_label.grid(row=1, column=0)

     #column and row configuration
    window.columnconfigure(1, weight=1)
    window.rowconfigure((0,1), weight=1)
    

    # sports_news()

    window.mainloop()