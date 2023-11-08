import customtkinter as c
import requests
from  PIL import Image
from CTkMessagebox import CTkMessagebox
# import sqlite3

c.set_appearance_mode('light')

c.set_default_color_theme('green')
def load_images(image_path,size):
    img= c.CTkImage(Image.open(image_path),size=size)

def combined_function():
    show_frame(news_frames)
    sports_news()


def show_frame(frame):
    frame.lift()

def sports_news():
    api_key = "e44acfad9a8d4734b43fa5b79f882c21"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=sports&apiKey="+api_key
    news = requests.get(url).json()
    
    article = news["articles"]

    news_article = []
    for arti in article:
        news_article.append(arti["title"])
    
    for index, value in enumerate(news_article) :
        print(index+1, value)






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

    content_frames = c.CTkFrame(window,fg_color='#722F37', corner_radius=0, width=600)
    content_frames.grid(row=1, column=1, sticky='nsew')
    # home_frame_img =c.CTkImage(Image.open("blog/wasp.jpg"), size=(800,600))
    # im = c.CTkLabel(master= content_frames, text="",image=home_frame_img)
    # im.grid(row=0, column=0, sticky="nswe")
    content_button =c.CTkButton(menu_frames, text="Home", command=lambda: show_frame(content_frames))
    content_button.grid(row=0, column=0,pady=(10, 30))
    
    news_frames= c.CTkFrame(window, fg_color='blue', corner_radius=0, width=600)
    news_frames.grid(row=1, column=1, sticky='nsew')
    news_button =c.CTkButton(menu_frames, text="News", command=combined_function)
    news_button.grid(row=1,column=0, pady=(0,30) )
    
    music_frame= c.CTkFrame(window, fg_color='red', corner_radius=0, width=600)
    music_frame.grid(row=1, column=1, sticky='nsew')
    music_frame_img =c.CTkImage(Image.open("snowflake.ico"), size=(800,600))
    im = c.CTkLabel(master=music_frame, text="",image=music_frame_img)
    im.grid(row=0, column=0, sticky="nswe")
    music_button =c.CTkButton(menu_frames, text="Music", command=lambda: show_frame(music_frame))
    music_button.grid(row=2, column=0, pady=(0, 30))
   
    video_frame= c.CTkFrame(window, fg_color='white', corner_radius=0, width=600)
    video_frame.grid(row=1, column=1, sticky='nsew')
    video_button =c.CTkButton(menu_frames, text= "Video", command=lambda: show_frame(video_frame))
    video_button.grid(row=3, column=0, pady=(0, 30))
    
    lifestyle_frame= c.CTkFrame(window, fg_color='pink', corner_radius=0, width=600)
    lifestyle_frame.grid(row=1, column=1, sticky='nsew')
    lifestyle_button =c.CTkButton(menu_frames, text="Lifesytle", command=lambda: show_frame(lifestyle_frame))
    lifestyle_button.grid(row=4, column=0, pady=(0, 30))
    
    politics_frame= c.CTkFrame(window, fg_color='gold', corner_radius=0, width=600)
    politics_frame.grid(row=1, column=1, sticky='nsew')
    politics_buttton =c.CTkButton(menu_frames, text= "Politics", command=lambda: show_frame(politics_frame))
    politics_buttton.grid(row=5, column=0, pady=(0, 30))

    schools_frame= c.CTkFrame(window, fg_color='green', corner_radius=0, width=600)
    schools_frame.grid(row=1, column=1, sticky='nsew')
    schools_button =c.CTkButton(menu_frames, text="Education", command=lambda: show_frame(schools_frame))
    schools_button.grid(row=6, column=0, pady=(0, 30))
    
    farm_frame= c.CTkFrame(window, fg_color='brown', corner_radius=0, width=600)
    farm_frame.grid(row=1, column=1, sticky='nsew')
    farm_button =c.CTkButton(menu_frames, text="Agriculture", command=lambda: show_frame(farm_frame))
    farm_button.grid(row=6, column=0, pady=(0, 30))
   
    religion_frame= c.CTkFrame(window, fg_color='yellow', corner_radius=0, width=600)
    religion_frame.grid(row=1, column=1, sticky='nsew')
    religion_button =c.CTkButton(menu_frames, text="Religion", command=lambda: show_frame(religion_frame))
    religion_button.grid(row=6, column=0, pady=(0, 30))
    
     #column and row configuration
    window.columnconfigure(1, weight=1)
    window.rowconfigure((0,1), weight=1)
    


    window.mainloop()