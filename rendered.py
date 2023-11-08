import customtkinter as c
from PIL import Image
import requests

# Initialize the customtkinter window
window = c.CTk()
window.title("WASP BLOG")
window.geometry("800x600")

# Create a function to fetch news based on a given category
def fetch_news(category):
    api_key = "179f75ac4f624a87b516870b477bce37"  # Replace with your actual News API key
    country = "ng"  # Set the country code as needed

    # Define the News API URL based on category
    if category == "entertainment":
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category=entertainment&apiKey={api_key}"
    elif category == "sports":
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category=sports&apiKey={api_key}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        news_data = response.json()
        articles = news_data.get("articles", [])

        if articles:
            news_text = "\n".join([f"{i+1}. {article['title']}" for i, article in enumerate(articles)])
            news_label.config(text=news_text)
        else:
            news_label.config(text="No news articles found.")
    except requests.exceptions.RequestException as e:
        c.CTkMessagebox.showerror("Error", f"Failed to fetch news: {str(e)}")

# Create a function to switch to a specific frame
def show_frame(frame):
    frame.lift()

# Create the main window layout
navbar_frame = c.CTkFrame(window, fg_color="white", corner_radius=0, width=800, height=100)
navbar_frame.pack(fill="x")

content_frame = c.CTkFrame(window, fg_color="#722F37", corner_radius=0)
content_frame.pack(fill="both", expand=True)

# Create buttons for different categories
news_button = c.CTkButton(navbar_frame, text="News", command=lambda: fetch_news("general"))
news_button.grid(row=0, column=0, padx=10, pady=10)

entertainment_button = c.CTkButton(navbar_frame, text="Entertainment", command=lambda: fetch_news("entertainment"))
entertainment_button.grid(row=0, column=1, padx=10, pady=10)

sports_button = c.CTkButton(navbar_frame, text="Sports", command=lambda: fetch_news("sports"))
sports_button.grid(row=0, column=2, padx=10, pady=10)

# Create a label to display news
news_label = c.CTkLabel(content_frame, text="", wraplength=600)
news_label.pack(padx=20, pady=20, fill="both", expand=True)

# Configure column and row weights
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# Show the window
window.mainloop()
