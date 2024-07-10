import tkinter as tk
import random
import time

def draw_square(top_right_x, top_right_y, side_length,side_height):

    # Function to remove the square after the specified duration
    def remove_square():
        canvas.delete(square)
        canvas.delete(text_item)
        canvas.delete(text_bg)
    duration=1000
    # Create a Tkinter window
    root = tk.Tk()
    root.overrideredirect(True)  # Remove the window frame
    root.wm_attributes("-topmost", True)  # Keep the window on top
    root.wm_attributes("-transparentcolor", root['bg'])  # Make the background transparent

    # Create a canvas with a transparent background
    canvas = tk.Canvas(root,width = root.winfo_screenwidth(),height=root.winfo_screenheight(), highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Calculate the bottom-left position of the square
    # top_right_x = top_right_x-220
    # top_right_y = top_right_y-20
    bottom_left_x = top_right_x + side_length
    bottom_left_y = top_right_y + side_height

    # a=random.randint(0, 255)
    # b=random.randint(0, 255)
    # c=random.randint(0, 255)
    # clour=f'#{a:02x}{b:02x}{c:02x}'
    current_time = time.strftime('%H:%M:%S')
    square = canvas.create_rectangle(top_right_x, top_right_y,bottom_left_x, bottom_left_y, outline='red', width=5)
    text_bg= canvas.create_rectangle(top_right_x-2.5,top_right_y-24,top_right_x + 95,top_right_y,fill='red',outline='red')
    text_item = canvas.create_text(top_right_x, top_right_y - 20, anchor=tk.NW, text=f'ID_{current_time}', fill='white',font=('Helvetica', 10, 'bold'))

    # Schedule the square to be removed after the specified duration (in milliseconds)
    root.after(duration, remove_square)

    # Close the window after the square is removed
    root.after(duration + 5 , root.destroy)

    # Run the Tkinter event loop
    root.mainloop()


# draw_square(1100,100, 100,500)
