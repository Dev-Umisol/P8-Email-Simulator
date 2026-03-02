# Build a Email Simulator that simulates sending, receiving, and managing emails between different users
# Practice code organization in a object oriented way

import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        # Initialize all parameters and mark as Unread
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
        self.timestamp = datetime.datetime.now()
    
    # Mark this email as read
    def MarkAsRead(self):
        self.read = True
    
    # Print Email Template
    def DisplayFullEmail(self):
        self.MarkAsRead()
        print("\n--- Email ---")
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f"Body: {self.body}")
        print("------------\n")
        
    # Return a string of when email status, from and what along with time
    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"  

# Send and Receive emails
class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox() # Everyone gets own separate inbox
    
    # Compose and send email
    def SendEmail(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.ReceiveEmail(email)

        print(f"Email sent from {self.name} to {receiver.name}!\n")
    
    # Header for Users inbox
    def CheckInbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.ListEmails()

    # Open message at position x
    def ReadEmail(self, index):
        self.inbox.ReadEmail(index)
    
    # Delete message at position x
    def DeleteEmail(self, index):
        self.inbox.DeleteEmail(index)

class Inbox:
    def __init__(self):
        self.emails = [] # List of email objects
    
    # Add email to inbox
    def ReceiveEmail(self, email):
        self.emails.append(email)
        
    # Print each email to inbox
    def ListEmails(self):
        if not self.emails:
            print("Your inbox is empty.\n")
            return

        print("\nYour Emails:")
        for i, email in enumerate(self.emails ,start=1):
            print(f"{i}. {email}") # 1. Email, 2. Email, etc
    
    # 1 index displaying emails
    def ReadEmail(self, index):
        if not self.emails:
            print("Inbox is empty.\n")
            return
        
        actualIndex = index - 1
        
        if actualIndex < 0 or actualIndex >= len(self.emails):
            print("Invalid email number.\n")
            return

        self.emails[actualIndex].DisplayFullEmail()
    
    # 1 index removing emails
    def DeleteEmail(self, index):
        if not self.emails:
            print("Inbox is empty.\n")
            return
        
        actualIndex = index - 1
        
        if actualIndex < 0 or actualIndex >= len(self.emails):
            print("Invalid email number.\n")
            return
        
        del self.emails[actualIndex]
        print("Email deleted.\n")

# Examples
def main():
    tory = User("Tory")
    ramy = User("Ramy")
    
    tory.SendEmail(ramy, "Hello", "Hi Ramy, just saying hello!")
    ramy.SendEmail(tory, "Re: Hello", "Hi Tory, hope you are fine.")
    
    ramy.CheckInbox()
    ramy.ReadEmail(1)
    ramy.DeleteEmail(1)
    ramy.CheckInbox()
    
if __name__ == '__main__':
    main()