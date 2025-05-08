# File: /color-extractor/color-extractor/src/main.py

from tkinter import Tk, filedialog, ttk, Label, Button, Entry
from PIL import Image
from utils.color_utils import rgb_to_hex
from services.image_processor import ImageProcessor
import threading
import os

def calculate_brightness(color):
    # Calculate brightness using the luminance formula
    r, g, b = color
    return 0.2126 * r + 0.7152 * g + 0.0722 * b  # Standard luminance formula

def process_image(image_path, num_colors, progress_label, progress_bar):
    processor = ImageProcessor()
    image = processor.load_image(image_path)

    if image is None:
        progress_label.config(text=f"Error: Failed to load image from {image_path}")
        return

    # Update progress label
    progress_label.config(text="Processing image...")

    # Extract colors
    colors = processor.extract_colors(image, num_colors=num_colors)

    # Sort colors by brightness (lightest to darkest)
    sorted_colors = sorted(colors, key=calculate_brightness)

    # Convert colors to hex and save to a text file
    with open('colors.txt', 'w') as f:
        for i, color in enumerate(sorted_colors):
            hex_color = rgb_to_hex(color)
            f.write(f"{hex_color}\n")
            # Update progress bar
            progress_bar['value'] = (i + 1) / len(sorted_colors) * 100
            progress_bar.update()

    progress_label.config(text="Processing complete! Colors saved to colors.txt")

def select_file(num_colors_entry, progress_label, progress_bar):
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    if file_path:
        try:
            num_colors = int(num_colors_entry.get())
            if num_colors <= 0:
                raise ValueError("Number of colors must be greater than 0.")
        except ValueError:
            progress_label.config(text="Error: Enter a valid number of colors.")
            return

        progress_label.config(text=f"Selected file: {file_path}")
        # Run the processing in a separate thread to avoid freezing the UI
        threading.Thread(target=process_image, args=(file_path, num_colors, progress_label, progress_bar)).start()

def open_colors_file():
    # Open the colors.txt file in the default text editor
    colors_file_path = os.path.abspath("colors.txt")
    if os.path.exists(colors_file_path):
        os.startfile(colors_file_path)
    else:
        print("colors.txt not found!")

def main():
    # Create the main window
    root = Tk()
    root.title("Color Extractor")
    root.geometry("400x300")  # Set a fixed window size

    # Create UI elements
    Label(root, text="Select an image file to extract colors:").pack(pady=10)

    # Entry for number of colors
    Label(root, text="Number of colors to extract:").pack(pady=5)
    num_colors_entry = Entry(root)
    num_colors_entry.insert(0, "80")  # Default value
    num_colors_entry.pack(pady=5)

    # File selection button
    progress_label = Label(root, text="")
    progress_label.pack(pady=5)

    progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=10)

    Button(root, text="Select File", command=lambda: select_file(num_colors_entry, progress_label, progress_bar)).pack(pady=5)

    # Button to open colors.txt
    Button(root, text="Open colors.txt", command=open_colors_file).pack(pady=5)

    # Add a label at the bottom left
    Label(root, text="Made by: @NAWIDX", anchor="w").place(x=10, y=270)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()