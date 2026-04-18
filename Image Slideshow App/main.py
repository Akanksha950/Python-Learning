import tkinter as tk
import time
from PIL import Image, ImageTk
# main window
root=tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

# list of image path
image_paths=[
    r"C:\Users\Album\img1.jpg",
    r"C:\Users\Album\img2.jpg",
    r"C:\Users\Album\img3.jpg",
    r"C:\Users\Album\img4.jpg",
    r"C:\Users\Album\img5.jpg"
]
image_size=(700,700)
images=[]
for path in image_paths:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img)

# convert pil images to tkinter compatible images
final_image=[]
for img in images:
    photo=ImageTk.PhotoImage(img)
    final_image.append(photo)

# label widget as image frame
image_label=tk.Label(root)
image_label.pack(pady=30)

# slide show function
def slide_show():
    for photo in final_image:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)


# Button to play slideshow
play_button=tk.Button(
    root,
    text="Play Slideshow",
    font=("Arial",14),
    command=slide_show
)

play_button.pack(pady=40)
root.mainloop()

