import requests  # For get requests
from bs4 import BeautifulSoup  # Parse raw html
import tkinter as tk  # python gui
from tkinter import ttk, messagebox  # tkinter theme

# Simple scraper and python GUI study


def scrape():
    url = "https://thescoop.co/"
    try:
        # send get
        response = requests.get(url)
        response.raise_for_status()

        # Parse raw html
        soup = BeautifulSoup(response.text, "html.parser")

        # Clear text area before user scrapes again
        text_area.delete(1.0, tk.END)

        headlines = soup.find_all("a", itemprop="url")

        if not headlines:
            text_area.insert(tk.END, "No headlines found.\n")
            return

        for i, headline in enumerate(headlines, start=1):
            title = headline.get_text(strip=True)
            link = headline["href"]
            text_area.insert(tk.END, f"{i}. {title}\n{link}\n\n")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


# Main window
root = tk.Tk()
root.title("Scoop News Scraper")
root.geometry("600x400")

# ** Frame (concept similar to html Divs)
frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

# Scrape button
scrape_button = ttk.Button(frame, text="Scrape Headlines", command=scrape)
scrape_button.pack(pady=10)

# Text area to show headlines
text_area = tk.Text(frame, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True)

# ** End Frame

# Run the app
root.mainloop()
