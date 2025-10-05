def calculate_due(total_bill, amount_paid):
    return total_bill - amount_paid

# Example usage
bill = float(input("Enter total bill amount: "))
paid = float(input("Enter amount paid: "))
due = calculate_due(bill, paid)

print("Due amount:", due)
