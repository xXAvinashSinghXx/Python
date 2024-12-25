from datetime import datetime, timedelta

# Purchased
a = datetime.strptime(input("Purchased date (YYYY-MM-DD): "), "%Y-%m-%d").date()
purchase_price = float(input("Purchased amount: "))
# Sold
b = datetime.strptime(input("Sold date (YYYY-MM-DD): "), "%Y-%m-%d").date()
sold_price = float(input("Sold amount: "))
# Depreciation
depreciation_rate = float(input("Depreciation rate (%): "))

# Function to calculate difference in years, months, and days
def calculate_date_difference(start_date, end_date):
    years = end_date.year - start_date.year
    months = end_date.month - start_date.month
    days = end_date.day - start_date.day

    if days < 0:
        months -= 1
        previous_month_end = (end_date.replace(day=1) - timedelta(days=1)).day
        days += previous_month_end

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Calculate the difference
years, months, days = calculate_date_difference(a, b)

# Convert days >= 27 to 1 month
if days >= 27:
    months += 1

# Function to calculate the profit or loss
def calculate_profit_or_loss(purchase_price, depreciation_rate, years, months, sold_price):
    if depreciation_rate < 100 and years >= 0 and months >= 0:
        # Calculate yearly depreciation
        yearly_depreciation = purchase_price * depreciation_rate / 100 * years
        
        # Calculate monthly depreciation
        monthly_depreciation = purchase_price * depreciation_rate / 100 * (months / 12)
        
        # Total depreciation
        total_depreciation = yearly_depreciation + monthly_depreciation
        
        # Remaining value after depreciation
        remaining_value = purchase_price - total_depreciation
        
        # Profit or Loss calculation
        profit_or_loss = sold_price - remaining_value
        
        # Display results
        print(f"\nPurchase Price: ${purchase_price}")
        print(f"Depreciation Rate: {depreciation_rate}%")
        print(f"Years: {years}, Months: {months}")
        print(f"Total Depreciation: ${round(total_depreciation, 2)}")
        print(f"Remaining Value: ${round(remaining_value, 2)}")
        print(f"Sold Price: ${sold_price}")
        
        # Check if it's a profit, loss, or neutral
        if profit_or_loss > 0:
            print(f"Profit: ${round(profit_or_loss, 2)}")
        elif profit_or_loss < 0:
            print(f"Loss: ${round(abs(profit_or_loss), 2)}")
        else:
            print("No Profit or Loss.")
    else:
        print("WRONG INPUT! Please ensure depreciation rate is less than 100, and years & months are non-negative.")

# Calculate and output the result
calculate_profit_or_loss(purchase_price, depreciation_rate, years, months, sold_price)
