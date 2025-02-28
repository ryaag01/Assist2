# shift_report.py
import datetime

def log_shift(shift_number: int):
    now = datetime.datetime.now()
    with open("shift_log.txt", "a") as log_file:
        log_file.write(f"Shift {shift_number} update at {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"Logged: Shift {shift_number} update at {now}")

if __name__ == "__main__":
    # For demonstration, simulate logging for a shift update.
    log_shift(shift_number=1)
