import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta, time
import threading
import winsound

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x250")

        self.label = ttk.Label(root, text="Set Alarm:", font=("Helvetica", 12), foreground="blue")
        self.label.pack(pady=10)

        self.time_var = tk.StringVar()
        self.entry = ttk.Combobox(root, textvariable=self.time_var, font=("Helvetica", 12), state="readonly")
        self.entry['values'] = self.get_predefined_times()
        self.entry.set("Select or Enter HH:MM")
        self.entry.pack(pady=10)

        self.button = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.button.pack(pady=20)

    def get_predefined_times(self):
        predefined_times = []
        for hour in range(0, 24):
            for minute in range(0, 60, 1):  # Every 1 minute
                time_str = f"{hour:02d}:{minute:02d}"
                predefined_times.append(time_str)
        return predefined_times

    def set_alarm(self):
        alarm_time_str = self.time_var.get()
        try:
            if ":" in alarm_time_str:
                alarm_hour, alarm_minute = map(int, alarm_time_str.split(':'))
            else:
                raise ValueError("Invalid time format. Please use HH:MM.")

            current_time = datetime.now().time()
            current_datetime = datetime.combine(datetime.today(), current_time)

            alarm_datetime = datetime.combine(datetime.today(), time(hour=alarm_hour, minute=alarm_minute))

            if alarm_datetime <= current_datetime:
                # If the selected time is in the past, set it for the next day
                alarm_datetime += timedelta(days=1)

            seconds_to_alarm = (alarm_datetime - current_datetime).seconds

            threading.Timer(seconds_to_alarm, self.play_alarm).start()

            # Basic animation for the label
            self.animate_label(alarm_datetime)

        except ValueError as e:
            self.label.config(text=str(e), foreground="red")

    def play_alarm(self):
        self.label.config(text="Alarm!", foreground="green")
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

    def animate_label(self, alarm_datetime):
        def update_label():
            remaining_time = (alarm_datetime - datetime.now()).total_seconds()

            if remaining_time <= 0:
                self.label.config(text="Alarm is set!", foreground="orange")
            else:
                self.label.config(text=f"Alarm is set! Time remaining: {int(remaining_time)} seconds", foreground="orange")
                self.root.after(1000, update_label)

        original_color = self.label.cget("foreground")
        update_label()


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
