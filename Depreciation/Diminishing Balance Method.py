from datetime import datetime, timedelta

try:
    # Purchased
    a = datetime.strptime(input("Purchased date (YYYY-MM-DD): "), "%Y-%m-%d").date()
    initial_value = float(input("Purchased amount: "))
    # Sold
    b = datetime.strptime(input("Sold date (YYYY-MM-DD): "), "%Y-%m-%d").date()
    sold_price = float(input("Sold amount: "))
    # Depreciation
    depreciation_rate = float(input("Depreciation rate (%): "))

    # Function to calculate difference in years and months
    def calculate_date_difference(start_date, end_date):
        years = end_date.year - start_date.year
        months = end_date.month - start_date.month
        days = end_date.day - start_date.day

        if days < 0:
            months -= 1
            # Calculate the days in the previous month
            days += (start_date.replace(year=end_date.year, month=end_date.month) - timedelta(days=start_date.day)).day

        if months < 0:
            years -= 1
            months += 12

        return years, months, days

    # Calculate the difference
    years, months, days = calculate_date_difference(a, b)

    # Convert days >= 27 to 1 month
    if days >= 27:
        months += 1

    # Convert remaining months to a fractional year
    fractional_year = months / 12

    def calculate_diminishing_balance_depreciation_yearly(initial_value, rate, years):
        book_value = initial_value
        rate_decimal = rate / 100
        depreciation_schedule = []

        for year in range(1, years + 1):
            depreciation = book_value * rate_decimal
            book_value -= depreciation
            depreciation_schedule.append({
                "Year": year,
                "Depreciation": round(depreciation, 2),
                "Book Value": round(book_value, 2)
            })
            if book_value <= 0:
                break

        return depreciation_schedule

    # Validate input
    if initial_value <= 0 or depreciation_rate <= 0 or years < 0:
        print("Please enter valid positive values.")
    else:
        # Calculate yearly depreciation schedule
        schedule = calculate_diminishing_balance_depreciation_yearly(initial_value, depreciation_rate, years)

        # Add depreciation for the fractional year
        if fractional_year > 0:
            last_book_value = schedule[-1]['Book Value'] if schedule else initial_value
            fractional_depreciation = last_book_value * depreciation_rate / 100 * fractional_year
            final_book_value = last_book_value - fractional_depreciation
            schedule.append({
                "Year": years + 1,
                "Depreciation": round(fractional_depreciation, 2),
                "Book Value": round(final_book_value, 2)
            })

        # Display the schedule
        print("\nDepreciation Schedule:")
        for entry in schedule:
            print(f"Year {entry['Year']}: Depreciation = {entry['Depreciation']}, Book Value = {entry['Book Value']}")

        profit_or_loss = sold_price - entry['Book Value']
        
        # Convert decimal value into integer
        result = int(profit_or_loss)
        
        # Check for profit, loss, or no profit/loss
        if result > 0:
            print(f"Profit: {result}")
        elif result < 0:
            # Convert negative value into positive (loss)
            loss = result * (-1)
            print(f"Loss: {loss}")
        else:
            print("NO PROFIT & LOSS")

except ValueError:
    print("Invalid input. Please enter numeric values.")
