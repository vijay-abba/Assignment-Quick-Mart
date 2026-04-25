# Feature 2: Product & Inventory
# Concepts: classes, inheritance, lists, dicts, loops, file I/O, **kwargs,

# Input (what user types)                                            |       Output (what program shows)
# (Menu) 1.Add  2.Update  3.Delete 4.Search  5.View All  6.Low Stock | ===== Inventory =====
# Choice: 1 Type (1-General 2-Perishable 3-Electronic 4-Clothing): 3 | --- Add Product ---
# Name: Samsung S24 Price: 79999 Qty: 25 Warranty months: 12         | Added! ID: PRD-0001
# Choice: 4 Search: sam                                              | Found 1 result: PRD-0001 | Samsung S24 | ₹79999 | Qty:25
# Choice: 6                                                          | LOW STOCK ALERT: PRD-0005 | USB Cable | Qty: 3

# Rules:
# Base class Product → subclasses: PerishableProduct (expiry_date), ElectronicProduct (warranty), ClothingProduct (size, material)
# Search must be case-insensitive partial match (e.g., "sam" finds "Samsung")
# Show warning for products with quantity < 5
# Save to data/products.txt

# Think 
"""
eample 1 
{
id: "PRD-001",
product_name: "apples",
expiry_date

}
5
"""


