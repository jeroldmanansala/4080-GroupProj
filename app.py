import tkinter as tk
from PIL import Image
from processor import process_and_predict

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw an Emotion")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.button_clear = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.button_clear.pack()

        self.button_recognize = tk.Button(root, text="Recognize Emotion", command=self.recognize_emotion)
        self.button_recognize.pack()

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="black", outline="black")

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas_as_image(self):
        self.canvas.postscript(file="drawing.eps")
        img = Image.open("drawing.eps")
        img.save("drawing.png")

    def recognize_emotion(self):
        self.save_canvas_as_image()
        emotion = process_and_predict("drawing.png")
        print(f"Recognized Emotion: {emotion}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
