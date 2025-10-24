# reaction-timer
A simple desktop GUI app built with Python and Pygame that tests your reaction time by measuring how fast you respond when the screen changes from red to green.\
\
**Features:**
- Clean, minimal interface
- Random delay (2-10s) to prevent prediction
- Detects early clicks and resets the test

**How it works:**
- Press spacebar to start the test
- Wait through a 3 second countdown
- Screen stays red for a random duration (2-10s)
- When the screen turns green, press spacebar as fast you can
- Your reaction time is displayed
- Press spacebar to restart the test

# Installation and Setup
Prerequisites:
- Python 3.7 or higher

**Setup**
1. Clone the repository
   ```python
   git clone https://github.com/monarchxr/reaction-timer.git
   cd reaction-timer
   ```
2. Create and activate a virtual environment
   On windows
   ```python
   python -m venv reactimer
   reactimer\Scripts\activate
   ```

   On macOS/Linux
   ```python
   python3 -m venv reactimer
   source reactimer\bin\activate
   ```

3. Install dependencies
   ```python
   pip install -r requirements.txt
   ```

4. Run the app
   ```python
   python main.py
   ```

# Contributing
Contributions are welcome. Check out contributing.md for more.
