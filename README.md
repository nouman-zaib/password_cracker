# Kivy Password Cracker Simulator

A simple graphical user interface (GUI) application built with Python and the Kivy framework. This app simulates a brute-force password cracking process by randomly guessing combinations of letters and digits until it successfully matches the user-provided password.

## Features
* **Simple GUI:** Clean and intuitive interface built using Kivy's `AnchorLayout` and `BoxLayout`.
* **Brute-Force Simulation:** Uses randomized string generation (`string.ascii_letters` + `string.digits`) to guess the password.
* **Attempt Tracking:** Calculates and displays the exact number of attempts it took to guess the target password.

## Prerequisites
Make sure you have Python 3.x installed on your system. You will also need to install the Kivy library.

```bash
pip install kivy
How to Run
Clone this repository or download the source code.

Save the code in a Python file, for example, main.py.

Open your terminal or command prompt and navigate to the folder containing the file.

Run the script using the following command:

Bash
python main.py
Usage
Launch the application.

Enter a short password in the text input field.

Note: Because the cracking loop runs synchronously on the main thread, entering a long or complex password will take significantly more time and may cause the application window to temporarily freeze ("Not Responding") until the password is found.

Click the Crack Password button.

Wait for the process to finish. The app will display the matched password along with the total number of attempts it took.

Disclaimer
This project is created for educational purposes only to demonstrate the basic mechanics of brute-force algorithms and to highlight the importance of using long, complex passwords in real-world applications.
