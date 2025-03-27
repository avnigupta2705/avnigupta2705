import pandas as pd
import random

# Sample synthetic dataset
data = {
    "Bill_ID": range(1, 11),
    "Invoice_Text": [
        "Hotel Invoice: Radisson, Amount ₹5000, Date: 01-03-2025",
        "Flight Ticket: New York to Delhi, Amount ₹12000, Date: 10-03-2025",
        "Hotel Invoice: Radisson, Amount ₹5000, Date: 05-03-2025",  # Duplicate
        "Restaurant Bill: McDonald's, Amount ₹800, Date: 02-03-2025",
        "Flight Ticket: New York to Delhi, Amount ₹12000, Date: 12-03-2025",  # Similar entry
        "Electricity Bill, Amount ₹2000, Date: 03-03-2025",  # Non-business
        "Train Ticket: Mumbai to Pune, Amount ₹1500, Date: 06-03-2025",
        "Hotel Invoice: Taj, Amount ₹6000, Date: 07-03-2025",
        "Grocery Bill: Big Bazaar, Amount ₹3000, Date: 08-03-2025",  # Non-business
        "Uber Ride: Office Travel, Amount ₹500, Date: 09-03-2025"
    ],
    "Expense_Entry_Date": [
        "01-03-2025", "12-03-2025", "05-03-2025", "02-03-2025",
        "14-03-2025", "03-03-2025", "06-03-2025", "07-03-2025",
        "08-03-2025", "09-03-2025"
    ]
}

df = pd.DataFrame(data)
df.to_csv("synthetic_bills.csv", index=False)
print("✅ Synthetic dataset created!")
