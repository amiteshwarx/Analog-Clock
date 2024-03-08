import tkinter as tk
from math import cos, sin, pi
from datetime import datetime

class AnalogClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analog Clock")
        self.geometry("400x400")
        self.configure(bg="black")
        self.resizable(False, False)

        self.clock_display = tk.Canvas(self, width=400, height=400, bg="black", highlightthickness=0)
        self.clock_display.pack()

        self.update_clock()

    def update_clock(self):
        now = datetime.now()
        hour = now.hour % 12
        minute = now.minute
        second = now.second

        self.clock_display.delete("all")

        # Draw clock face
        self.clock_display.create_oval(50, 50, 350, 350, outline="white")

        # Draw hour markers
        for i in range(12):
            angle = i * (360 / 12) - 90
            x1 = 200 + 130 * cos(angle * pi / 180)
            y1 = 200 + 130 * sin(angle * pi / 180)
            x2 = 200 + 150 * cos(angle * pi / 180)
            y2 = 200 + 150 * sin(angle * pi / 180)
            self.clock_display.create_line(x1, y1, x2, y2, fill="white", width=2)

        # Draw hour hand
        hour_angle = (hour * 30 + minute / 2 + second / 120) - 90
        hour_x = 200 + 80 * cos(hour_angle * pi / 180)
        hour_y = 200 + 80 * sin(hour_angle * pi / 180)
        self.clock_display.create_line(200, 200, hour_x, hour_y, fill="white", width=6)

        # Draw minute hand
        minute_angle = (minute * 6 + second / 10) - 90
        minute_x = 200 + 100 * cos(minute_angle * pi / 180)
        minute_y = 200 + 100 * sin(minute_angle * pi / 180)
        self.clock_display.create_line(200, 200, minute_x, minute_y, fill="white", width=3)

        # Draw second hand
        second_angle = (second * 6) - 90
        second_x = 200 + 100 * cos(second_angle * pi / 180)
        second_y = 200 + 100 * sin(second_angle * pi / 180)
        self.clock_display.create_line(200, 200, second_x, second_y, fill="red", width=1)

        # Display digital time
        time_str = now.strftime("%I:%M:%S %p")
        self.clock_display.create_text(200, 280, text=time_str, font=("Arial", 16), fill="white")

        self.after(100, self.update_clock)  # Update more frequently for smoother animation

if __name__ == "__main__":
    app = AnalogClock()
    app.mainloop()
