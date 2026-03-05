# 📁 Email Simulator

A terminal-based email system that simulates sending, receiving, and managing emails between users built with object-oriented Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)

## 📌 About

This project simulates a basic email system entirely in the terminal. Users can send emails to each other, check their inbox, read individual messages, and delete them. The goal was to practise designing a multi-class OOP system where objects interact with each other in a realistic way each user gets their own `Inbox`, and each message is its own `Email` object.

## 🧠 What I Learned
- **Multi-class OOP design** — Splitting responsibilities across three classes (`Email`, `User`, `Inbox`) so each class has a single clear purpose, rather than putting everything in one place
- **Object relationships** — Having `User` hold an `Inbox` instance, and `Email` hold references to both a sender and receiver `User` — modeling real-world relationships between objects
- **The `datetime` module** — Automatically timestamping each email on creation with `datetime.datetime.now()` and formatting it cleanly with `strftime()`
- **1-based indexing** — Converting user-friendly 1-based input to 0-based list indices with `actualIndex = index - 1`, and validating the range before accessing the list
- **`enumerate()` with `start=1`** — Displaying numbered lists in a clean, user-friendly way without manually tracking a counter
- **`__str__` vs display methods** — Using `__str__` for a compact inbox summary and a separate `DisplayFullEmail()` method for the full view, and understanding when each is appropriate
- **`if __name__ == '__main__'`** — Structuring the entry point properly so the script can be imported as a module without running the demo code automatically

## 🛠️ Technologies Used
| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x   | Core Language 
| `datetime`   | Timestamping emails on creation 

## 💡 How It Works

Three classes work together to model the system:
- `Email` — Holds sender, receiver, subject, body, timestamp, and read status
- `User` — Can send emails, check their inbox, read, and delete messages
- `Inbox` — Belongs to each user and manages their list of `Email` objects

**Example Output:**
```
Email sent from Tory to Ramy!

Ramy's Inbox:

Your Emails:
1. [Unread] From: Tory | Subject: Hello | Time: 2026-03-05 14:22

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: 2026-03-05 14:22
Body: Hi Ramy, just saying hello!
------------
```

## 🚀 Future Improvements

- [ ] Add a reply() method that pre-fills the receiver and subject automatically
- [ ] Support CC and BCC fields on the Email class
- [ ] Save and load emails from a JSON file so inboxes persist between sessions
- [ ] Add a search(keyword) method to filter emails by subject or sender
- [ ] Build an interactive CLI menu so users don't have to call functions manually

## 📂 Project Structure

```
email-simulator/
│
├── P6EmailSimulator.py    # Email, User, and Inbox classes + main demo
└── README.md
```

*Part of my Python learning journey 🐍 — practicing object-oriented design with multiple interacting classes*
