import tkinter as tk
from detector import start_detection  # This will be created in the next step

def main():
    window = tk.Tk()
    window.title("Emotion Detector")
    window.geometry("350x200")
    window.configure(bg='#f2f2f2')

    label = tk.Label(window, text="Real-Time Emotion Detection By Ashvin", font=("Helvetica", 14), bg='#f2f2f2')
    label.pack(pady=20)

    start_button = tk.Button(window, text="Start Detection", font=("Helvetica", 12),
                             bg="#4CAF50", fg="white", command=start_detection)
    start_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
