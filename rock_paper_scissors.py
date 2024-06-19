from tkinter import *
from PIL import ImageTk, Image
import random

class ImageLoader:
    def __init__(self, path, width, height):
        self.path = path
        self.width = width
        self.height = height
        self.img = self.load_and_resize_image(self.path, self.width, self.height)
        self.flipped_img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.tk_flipped_img = ImageTk.PhotoImage(self.flipped_img)

    def load_and_resize_image(self, path, width, height):
        try:
            img = Image.open(path)
            img = img.resize((width, height))
            return img
        except IOError as e:
            print(f"Error loading image '{path}': {e}")
            raise

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title('Rock Paper Scissors')
        self.root.geometry('800x680')

        self.background_color = '#f2f2f2'
        self.button_color = '#d9d9d9'
        self.result_color = '#4CAF50'
        self.result_font = ('Algerian', 25)

        self.player_score = 0
        self.computer_score = 0

        self.canvas = Canvas(self.root, width=800, height=680, bg=self.background_color)
        self.canvas.pack()

        self.create_widgets()
        self.load_images()

    def create_widgets(self):
        self.l1 = Label(self.root, text='Player', font=('Algerian', 25), bg=self.background_color)
        self.l2 = Label(self.root, text='Computer', font=('Algerian', 25), bg=self.background_color)
        self.l3 = Label(self.root, text='Vs', font=('Algerian', 40), bg=self.background_color)
        self.l1.place(x=80, y=20)
        self.l2.place(x=560, y=20)
        self.l3.place(x=370, y=230)

        self.score_label = Label(self.root, text=f'Player: {self.player_score}  Computer: {self.computer_score}', font=('Georgia', 18, 'bold'), bg=self.background_color)
        self.score_label.place(x=280, y=550)

        self.rock_b = Button(self.root, text='Rock', command=lambda: self.game(1), bg=self.button_color, fg='black', font=('Arial', 12, 'bold'), padx=10, pady=5, borderwidth=2, relief='raised')
        self.paper_b = Button(self.root, text='Paper', command=lambda: self.game(2), bg=self.button_color, fg='black', font=('Arial', 12, 'bold'), padx=10, pady=5, borderwidth=2, relief='raised')
        self.scissor_b = Button(self.root, text='Scissor', command=lambda: self.game(3), bg=self.button_color, fg='black', font=('Arial', 12, 'bold'), padx=10, pady=5, borderwidth=2, relief='raised')
        self.clear_b = Button(self.root, text='RESTART', font=('Arial', 10, 'bold'), bg='red', fg='white', width=10, command=self.clear)
        self.rock_b.place(x=20, y=500)
        self.paper_b.place(x=110, y=500)
        self.scissor_b.place(x=210, y=500)
        self.clear_b.place(x=370, y=28)

        self.result_var = StringVar()
        self.result_label = Label(self.root, textvariable=self.result_var, font=self.result_font, bg=self.background_color, fg=self.result_color)
        self.result_label.place(x=290, y=600)

    def load_images(self):
        # Load Images using ImageLoader class
        self.img_p = ImageLoader("C:\\Users\\green\\Downloads\\deefault.jpg", 300, 300)
        self.rock_p = ImageLoader("C:\\Users\\green\\Downloads\\rockk.jpg", 300, 300)
        self.paper_p = ImageLoader("C:\\Users\\green\\Downloads\\paper.jpeg", 300, 300)
        self.scissor_p = ImageLoader("C:\\Users\\green\\Downloads\\scissor.jpeg", 300, 300)
        self.img_s = ImageLoader("C:\\Users\\green\\Downloads\\selection1.jpg", 300, 130)

        # Display Initial Images on Canvas
        self.display_images()

    def display_images(self):
        # Clear Canvas
        self.canvas.delete('all')

        # Display Player and Computer Images
        self.canvas.create_image(0, 100, anchor=NW, image=self.img_p.tk_img)
        self.canvas.create_image(500, 100, anchor=NW, image=self.img_p.tk_flipped_img)
        self.canvas.create_image(0, 400, anchor=NW, image=self.img_s.tk_img)
        self.canvas.create_image(500, 400, anchor=NW, image=self.img_s.tk_img)

        # Update Score Label
        self.score_label.config(text=f'Player: {self.player_score}  Computer: {self.computer_score}')

    def game(self, player):
        select = [1, 2, 3]
        computer = random.choice(select)

        # Update Player Image
        if player == 1:
            self.canvas.create_image(0, 100, anchor=NW, image=self.rock_p.tk_img)
        elif player == 2:
            self.canvas.create_image(0, 100, anchor=NW, image=self.paper_p.tk_img)
        else:
            self.canvas.create_image(0, 100, anchor=NW, image=self.scissor_p.tk_img)

        # Update Computer Image
        if computer == 1:
            self.canvas.create_image(500, 100, anchor=NW, image=self.rock_p.tk_flipped_img)
        elif computer == 2:
            self.canvas.create_image(500, 100, anchor=NW, image=self.paper_p.tk_flipped_img)
        else:
            self.canvas.create_image(500, 100, anchor=NW, image=self.scissor_p.tk_flipped_img)

        # Determine Result
        if player == computer:
            result = 'Draw'
        elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
            result = 'You won'
            self.player_score += 1
        else:
            result = 'Computer won'
            self.computer_score += 1

        # Update Result Label
        self.result_var.set(f'Result: {result}')

        # Update Score Label
        self.score_label.config(text=f'Player: {self.player_score}  Computer: {self.computer_score}')

    def clear(self):
        # Clear Canvas, Result Label, and Scores
        self.canvas.delete('all')
        self.display_images()
        self.result_var.set('')
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text=f'Player: {self.player_score}  Computer: {self.computer_score}')

if __name__ == "__main__":
    root = Tk()
    app = RockPaperScissors(root)
    root.mainloop()
