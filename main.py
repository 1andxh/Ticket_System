import csv
import sys

class TicketSystem:
    def __init__(self, owner):
        self.owner = owner
        self.available_tickets = 0
        self.user_tickets = {}
        self.quantity = 0

    def create_ticket(self):
        self.quantity = input(input("Enter numeber of tickets to create: "))
        self.available_tickets += self.quantity
        print(f"{self.quantity} tickets created successfully!")
