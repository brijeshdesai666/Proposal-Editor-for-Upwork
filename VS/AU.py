import pyautogui
import time
import random
import keyboard

import threading

stop_flag = False

def on_esc_press():
    global stop_flag
    stop_flag = True
    print("\n E...")

# Attach global hotkey listener
keyboard.add_hotkey('esc', on_esc_press)

def move_and_click(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 0.6))
    pyautogui.click()

def scroll_down_fixed(min_scroll=2, max_scroll=7):
    steps = random.randint(min_scroll, max_scroll)
    for _ in range(steps):
        pyautogui.scroll(-200)
        time.sleep(random.uniform(0.5, 1))
        if stop_flag:
            return

def scroll_down_safe(min_scroll=1, max_scroll=4):
    steps = random.randint(min_scroll, max_scroll)
    for _ in range(steps):
        pyautogui.scroll(-200)
        time.sleep(random.uniform(0.4, 0.9))
        if stop_flag:
            return

def move_cursor_around():
    for _ in range(random.randint(3, 6)):
        if stop_flag:
            return
        x = random.randint(300, 800)
        y = random.randint(200, 700)
        pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.5))
        time.sleep(random.uniform(0.5, 1.2))

def browse_job():
    if stop_flag:
        return

    screen_width, screen_height = pyautogui.size()
    min_x = int(screen_width * 0.30)
    max_x = int(screen_width * 0.80)

    scroll_down_safe()
    time.sleep(random.uniform(1, 2))
    if stop_flag:
        return

    job_x = random.randint(min_x, max_x)
    job_y = random.randint(250, 700)
    move_and_click(job_x, job_y)

    time.sleep(random.uniform(3, 8))
    scroll_down_fixed(1, 4)

    read_time = random.uniform(8, 12)
    start_time = time.time()
    while time.time() - start_time < read_time:
        if stop_flag:
            return
        move_cursor_around()

    pyautogui.hotkey('alt', 'left')
    time.sleep(random.uniform(3, 5))
    scroll_down_safe()

def simulate_upwork_browsing():
    global stop_flag
    print("➡  ENTER")
    input()
    print("⌛  10 seconds ...")
    time.sleep(10)

    print("🟢 AS\n")

    while not stop_flag:
        cycles = random.randint(5, 11)
        print(f"🔁 Starting {cycles} browsing cycles...")

        for i in range(cycles):
            if stop_flag:
                break
            print(f"📄 Cycle {i + 1}/{cycles}")
            browse_job()

        if stop_flag:
            break

        print("🔄 R p")
        # pyautogui.hotkey('ctrl', 'r')
        
        time.sleep(5)
        pyautogui.press('home')

        load_wait_time = random.uniform(7, 10)
        print(f"⏳ Waiting {round(load_wait_time, 2)} seconds for page to load...")
        time.sleep(load_wait_time)

        print("⬇ Scrolling down to reach job listings...")
        scroll_down_fixed(2, 5)

    print(" A st")
    print("✅ F a c")

simulate_upwork_browsing()





