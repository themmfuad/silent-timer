import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-topmost", True)  # Always on top

        self.running = False  # Initialize running attribute
        self.time_left = 0
        self.after_id = None  # Store the ID of the scheduled after event

        # Layout for input boxes in one line
        input_frame = tk.Frame(root)
        input_frame.pack(pady=2)

        self.hour_entry = tk.Entry(input_frame, width=3, bg='black', fg='white', borderwidth=2, relief='solid')
        self.hour_entry.pack(side=tk.LEFT)
        tk.Label(input_frame, text="H", bg='black', fg='white').pack(side=tk.LEFT)

        self.minute_entry = tk.Entry(input_frame, width=3, bg='black', fg='white', borderwidth=2, relief='solid')
        self.minute_entry.pack(side=tk.LEFT)
        tk.Label(input_frame, text="M", bg='black', fg='white').pack(side=tk.LEFT)

        self.second_entry = tk.Entry(input_frame, width=3, bg='black', fg='white', borderwidth=2, relief='solid')
        self.second_entry.pack(side=tk.LEFT)
        tk.Label(input_frame, text="S", bg='black', fg='white').pack(side=tk.LEFT)

        # Buttons in a separate line
        button_frame = tk.Frame(root)
        button_frame.pack(pady=2)

        self.start_button = tk.Button(button_frame, text="Start", command=self.start_timer, bg='black', fg='white')
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_timer, bg='black', fg='white')
        self.pause_button.pack(side=tk.LEFT)

        self.resume_button = tk.Button(button_frame, text="Resume", command=self.resume_timer, bg='black', fg='white')
        self.resume_button.pack(side=tk.LEFT)

        # Timer display on the third line
        self.time_display = tk.Label(root, text="Time left: 00 H - 00 M - 00 S", bg='black', fg='white')
        self.time_display.pack(pady=2)

        self.update_background_color()  # Set initial background color

    def update_background_color(self):
        """Update the background color based on timer state."""
        if self.running:
            self.root.config(bg="#000")
        else:
            self.root.config(bg="#444")  # Light red

    def start_timer(self):
        hours = int(self.hour_entry.get() or 0)
        minutes = int(self.minute_entry.get() or 0)
        seconds = int(self.second_entry.get() or 0)

        self.time_left = hours * 3600 + minutes * 60 + seconds

        if self.running:
            self.running = False
            if self.after_id is not None:
                self.root.after_cancel(self.after_id)

        self.running = True
        self.update_background_color()
        self.countdown()

    def countdown(self):
        if self.running and self.time_left > 0:
            hours, remainder = divmod(self.time_left, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.time_display.config(text=f"{hours:02} H - {minutes:02} M - {seconds:02} S")
            self.after_id = self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.running = False
            self.update_background_color()
            current_time = datetime.now().strftime("%I:%M %p")  # Current time in 12-hour format
            self.time_display.config(text=f"Time's up! - CT: {current_time}")
            messagebox.showinfo("Timer Finished", "Your timer has completed.")

    def update_timer(self):
        if self.running:
            self.time_left -= 1
            self.countdown()

    def pause_timer(self):
        self.running = False
        self.update_background_color()
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)

    def resume_timer(self):
        if not self.running and self.time_left > 0:
            self.running = True
            self.update_background_color()
            self.countdown()

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = CountdownTimer(root)
    root.mainloop()
