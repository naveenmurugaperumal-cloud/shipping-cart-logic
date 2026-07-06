# Shipping Cart Logic

# Get input from user
price = float(input("Enter the price of the product: "))
discount = float(input("Enter the discount percentage: "))
gst = float(input("Enter the GST percentage: "))

# Calculate discount amount
discount_amount = (price * discount) / 100

# Price after discount
price_after_discount = price - discount_amount

# Calculate GST
gst_amount = (price_after_discount * gst) / 100

# Final amount
total_amount = price_after_discount + gst_amount

# Display results
print("\n------ Bill Details ------")
print("Original Price      :", price)