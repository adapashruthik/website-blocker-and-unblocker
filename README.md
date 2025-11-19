A simple and handy desktop tool built using Python and Tkinter that lets you block and unblock distracting websites on your system. Perfect for productivity, parental control, or just keeping your focus locked in.
✨ Features

Block any website by entering its domain

Unblock websites that were previously blocked

Clean and simple Tkinter-based GUI

Works by modifying your system's hosts file

Runs on Windows, macOS, and Linux (admin privileges required)
🚀 How It Works

This tool adds entries into your system's hosts file so that chosen websites get redirected to your local machine (127.0.0.1), effectively blocking them.
📦 Requirements

Make sure you have:

Python 3.8+

Tkinter (comes pre-installed with most Python versions)

Administrator/root access

Windows: Run the app as Run as Administrator

macOS/Linux: Use sudo python app.py
🔧 Installation

Clone the repo

git clone https://github.com/your-username/website-blocker.git
cd website-blocker


Run the application

python main.py
🖥️ Usage

Open the application

Type the website you want to block (like facebook.com)

Hit Block

To unblock, select the website from the list and click Unblock

Restart your browser to see the changes  
🔐 Important Notes

The app modifies the hosts file — so admin/root access is required.

Some browsers cache DNS aggressively, so you may need to:

Restart the browser

Or flush DNS (optional)

PROJECT STRUCTURE
website-blocker/
│
├── main.py          # GUI and core logic
├── blocker.py       # Helper functions for editing hosts file
├── README.md        # Project documentation
└── assets/          # (optional) icons, images, etc.
