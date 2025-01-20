import csv
import sys

class TicketSystem:
    def __init__(self, buyer):
        self.buyer = buyer
        self.available_tickets = 0
        self.user_tickets = {}
        self.quantity = 0

    def create_ticket(self):
        self.quantity = input(input("Enter numeber of tickets to create: "))
