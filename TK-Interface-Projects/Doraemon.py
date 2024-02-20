# On Screen Pet
import tkinter as tk


class OnScreenPet:
    def __init__(self):
        # Create the window
        self.window = tk.Tk()
        self.window.title('OnScreen Pet')
        self.window.geometry('800x600')
        self.window.resizable(False, False)
        # Creating a Canvas
        self.canvas = tk.Canvas(master=self.window, bg='black')
        # Add the canvas into the window
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=2, pady=2)
        # Drawing the pet
        # Face
        # Create_Oval function takes the coordinates of top left and bottom right
        self.window.after(1000, self.blink)
        self.eye_open = True
        self.canvas.create_oval((200, 120, 600, 480), fill='#1E96D5')
        self.canvas.create_oval((235, 215, 565, 470), fill='#FFFFFF', outline='#000000', width=2)
        self.left_eye = self.canvas.create_oval((305, 150, 400, 270), fill='#FFFFFF', outline='#000000', width=2)
        self.right_eye = self.canvas.create_oval((400, 150, 495, 270), fill='#FFFFFF', outline='#000000', width=2)
        self.left_eye_pupil = self.canvas.create_oval((367, 217, 393, 243), fill='#000000')
        self.right_eye_pupil = self.canvas.create_oval((407, 217, 433, 243), fill='#000000')
        self.window.mainloop()

    def blink(self):
        if self.eye_open:
            # Show the Pupil
            self.canvas.itemconfig(self.left_eye, fill='#FFFFFF')
            self.canvas.itemconfig(self.right_eye, fill='#FFFFFF')

            self.canvas.itemconfig(self.left_eye_pupil, state='normal')
            self.canvas.itemconfig(self.right_eye_pupil, state='normal')
        else:
            # Hide the pupil
            self.canvas.itemconfig(self.left_eye, fill='#1E96D5')
            self.canvas.itemconfig(self.right_eye, fill='#1E96D5')

            self.canvas.itemconfig(self.left_eye_pupil, state='hidden')
            self.canvas.itemconfig(self.right_eye_pupil, state='hidden')

        self.eye_open = not self.eye_open
        self.window.after(1000, self.blink)


def main():
    pet = OnScreenPet()


main()
