# 🤖 Clash of Clans Donation Bot

> ⚠️ **Disclaimer**: This project is intended for **educational purposes only**.
> Do **not** use this bot in real Clash of Clans accounts — doing so may violate **Supercell’s Terms of Service** and could result in your account getting **banned**. The author is not responsible for any misuse of this tool.

A Python automation script that donates troops in **Clash of Clans** using screen recognition with `OpenCV`, GUI automation with `PyAutoGUI`, and human-like interactions to reduce detection risk. This bot works by detecting request templates on screen and clicking the donation buttons intelligently.

---

## 🚀 Features

* 🧠 **Image recognition** using OpenCV for troop and donation button detection
* 👆 **Human-like clicks and movement** using sigmoid curve pathing
* 🤭 Real-time screen scanning and troop response loop
* 🖼️ Visual overlay with troop request detection windows
* 🥵 Multi-threaded design for efficient operation
* 😶️ Works on screen-shared or emulator-based Clash of Clans sessions

---

## 📂 File Structure

```
📁 coc-bot/
├── coc.py              # Main bot script (entry point)
├── draw.py             # Tkinter-based debug visualization
├── human_like.py       # Human-like movement and click simulation
├── donate_file/        # Folder with troop template images (e.g., loon.png, light.png)
├── donate.png          # Image template of the donation button
```

---

## 📦 Requirements

Install the required Python packages using pip:

```bash
pip install opencv-python pyautogui numpy
```

> ⚠️ `tkinter` comes preinstalled with most Python distributions. If not, install it manually (especially on Linux).

---

## 🛠️ Usage

1. **Prepare your environment**:

   * Run Clash of Clans on an emulator or screen-shared device in a fixed screen resolution (e.g., 1920x1080).
   * Position the game so that troop requests appear in the upper-left region of the screen.

2. **Add troop templates**:

   * Place cropped grayscale images of troop requests (e.g., `loon.png`, `light.png`) in the `donate_file/` directory.
   * Make sure each image matches the screen size and resolution precisely.

3. **Run the bot**:

```bash
python coc.py
```

The bot will:

* Continuously scan for troop requests
* Detect and click donation buttons
* Log activity to the console
* Draw visual boxes to show detection zones

---

## 🧠 How It Works

* `find_template()` scans specific screen regions for matching troop request templates.
* If a match is found, it looks for the donate button nearby.
* Clicks are performed via `human_like.py`, which simulates realistic motion paths.
* `draw.py` draws a temporary red box to show what part of the screen is being scanned.

---

## 👍 Notes & Warnings

* 🔐 **Use at your own risk** – while this mimics human behavior, automation tools may still be against game ToS.
* 🖥️ This bot is not universal – you **must use proper screen resolution**, or the templates won't match.
* 🧪 Test in sandboxed or secondary accounts before using on your main.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤛 Contributing

Contributions are welcome! Feel free to open issues or pull requests.
