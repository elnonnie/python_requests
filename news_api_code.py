import customtkinter as c
from CTkMessagebox import CTkMessagebox
import sqlite3
import PIL as imagetk
import requests

# c.set_appearance_mode('dark')
# c.set_default_color_theme('blue')

def sports_page():
#     music_frame.grid_remove()
#     lifestyle_frame.grid_remove()
#     politics_frame.grid_remove()
#     religion_frame.grid_remove()
#     school_frame.grid_remove()
#     home_frame.grid_remove()
#     film_frame.grid_remove()
#     sports_frame.grid(row=1, column=1, sticky='nsew')

    api_key = "e44acfad9a8d4734b43fa5b79f882c21"
    main_url = "https://newsapi.org/v2/top-headlines?country=ng&category=sports&apiKey="+api_key
    news = requests.get(main_url).json()
    articles = news["articles"]

    news_article = []
    my_news = ""

    for article in articles:
        news_article.append(article["title"])

    for i in range(10):
        my_news = i+1, news_article[i]
        print(my_news)

# if __name__== "__main__":
#     window=c.CTk()
#     # window.geometry('800x600')
#     window.title('WASP BLOG')
#     window.maxsize(900, 700)
#     window.minsize(800, 600)
#     # window.iconbitmap('')


#     #frame sections
   
#     # navbar_frames = c.CTkFrame(window, fg_color="grey", width= 800,height=100,corner_radius=0 )
#     # navbar_frames.grid(row=0, column=0, sticky= 'nsew', columnspan=2)

#     # navbar_label = c.CTkLabel(navbar_frames, text="Welcome to WASP's Blog \nNews, Entertainment, Lifestyle, Inspiration and yes... Gossip!", font = ("Montserat", 28, "bold"))
#     # navbar_label.grid(row=0,column=0)

#     menu_frames = c.CTkFrame(window, fg_color="grey", corner_radius=0, width=100, height=500)
#     menu_frames.grid(row=1, column=0, sticky='nsew')

#     home_frame = c.CTkFrame(window, corner_radius=0, width=700)
#     home_frame.grid(row=1, column=1, sticky='nsew')

#     music_frame = c.CTkFrame(window, corner_radius=0, width=700)
#     music_frame.grid(row=1, column=1, sticky='nsew')

#     sports_frame = c.CTkFrame(window, corner_radius=0, width=700)
#     sports_frame.grid(row=1, column=1, sticky='nsew')

#     lifestyle_frame = c.CTkFrame(window, corner_radius=0, width=700)
#     lifestyle_frame.grid(row=1, column=1, sticky='nsew')

#     politics_frame = c.CTkFrame(window, corner_radius=0, width=700)
#     politics_frame.grid(row=1, column=1, sticky='nsew')
    
#     religion_frame = c.CTkFrame(window, corner_radius=0, width=700)
#     religion_frame.grid(row=1, column=1, sticky='nsew')

#     school_frame = c.CTkFrame(window, corner_radius=0, width=700)
#     school_frame.grid(row=1, column=1, sticky='nsew')

#     film_frame = c.CTkFrame(window, corner_radius=0, width=700)
#     film_frame.grid(row=1, column=1, sticky='nsew')

#     # menu buttons
#     home_button =c.CTkButton(menu_frames, text="Home")
#     home_button.grid(row=0, column=0,pady=(10, 30))

#     news_button =c.CTkButton(menu_frames, text="News")
#     news_button.grid(row=1,column=0, pady=(0,30) )

#     music_button =c.CTkButton(menu_frames, text="Music")
#     music_button.grid(row=2, column=0, pady=(0, 30))

#     sports_button =c.CTkButton(menu_frames, text= "Sports", command = sports_page)
#     sports_button.grid(row=3, column=0, pady=(0, 30))

#     lifestyle_button =c.CTkButton(menu_frames, text="Lifesytle")
#     lifestyle_button.grid(row=4, column=0, pady=(0, 30))

#     politics_buttton =c.CTkButton(menu_frames, text= "Politics")
#     politics_buttton.grid(row=5, column=0, pady=(0, 30))
    
#     schools_button =c.CTkButton(menu_frames, text="Education")
#     schools_button.grid(row=6, column=0, pady=(0, 30))
   
#     film_button =c.CTkButton(menu_frames, text="Film")
#     film_button.grid(row=6, column=0, pady=(0, 30))
   
#     religion_button =c.CTkButton(menu_frames, text="Religion")
#     religion_button.grid(row=6, column=0, pady=(0, 30))

#     sports_page()

#      #column and row configuration
#     window.columnconfigure(1, weight=1)
#     window.rowconfigure(0, weight=1)
    


#     window.mainloop()



