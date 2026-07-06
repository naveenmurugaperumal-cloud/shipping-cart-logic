
price = float(input("Enter the price of the product: "))
discount = float(input("Enter the discount percentage: "))
gst = float(input("Enter the GST percentage: "))


discount_amount = (price * discount) / 100


price_after_discount = price - discount_amount


gst_amount = (price_after_discount * gst) / 100


total_amount = price_after_discount + gst_amount

print("Original Price      :", price)