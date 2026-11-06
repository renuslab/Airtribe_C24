
# main.py

from models import LibraryItem, Book, Magazine, DVD, Member


# ==================================================
# 1. CREATE LIBRARY ITEMS
# ==================================================

book = Book("Python 101", 1, "A. Rao")

magazine = Magazine("Tech Monthly", 2, 45)

dvd = DVD("Python Programming", 3, 120)


# ==================================================
# 2. CREATE MEMBERS
# ==================================================

alice = Member("Alice", 101)

bob = Member("Bob", 102, max_items=1)


print("\n========== LIBRARY MANAGEMENT SYSTEM ==========\n")


# ==================================================
# 3. BORROWING AND ALREADY BORROWED ERROR
# ==================================================

print("1. BORROWING ITEMS")

try:
    alice.borrow(book)

    print("Alice borrowed:", book.describe())

    # Bob attempts to borrow the same book
    bob.borrow(book)

except ValueError as e:
    print("Could not borrow:", e)


# ==================================================
# 4. BORROW LIMIT ERROR
# ==================================================

print("\n2. BORROW LIMIT CHECK")

try:
    bob.borrow(magazine)

    # Bob has a borrowing limit of 1
    bob.borrow(dvd)

except ValueError as e:
    print("Could not borrow:", e)


# ==================================================
# 5. RETURNING AN ITEM NOT BORROWED
# ==================================================

print("\n3. INVALID RETURN CHECK")

try:
    alice.return_item(magazine)

except ValueError as e:
    print("Could not return:", e)


# ==================================================
# 6. POLYMORPHISM - LATE FEE CALCULATION
# ==================================================

print("\n4. POLYMORPHISM - LATE FEE CALCULATION")

items = [book, magazine, dvd]

for item in items:

    print(
        item.describe(),
        "-> Late fee for 3 days: Rs",
        item.late_fee(3)
    )


# ==================================================
# 7. SUCCESSFUL RETURN AND FEE CALCULATION
# ==================================================

print("\n5. RETURN ITEM AND CALCULATE LATE FEE")

try:
    fee = alice.return_item(book, days_late=3)

    print("Late fee to be paid: Rs", fee)

except ValueError as e:
    print("Return failed:", e)


# ==================================================
# 8. ENCAPSULATION DEMONSTRATION
# ==================================================

print("\n6. ENCAPSULATION CHECK")

try:
    print(book.__available)

except AttributeError:
    print("Cannot access private attribute '__available' directly.")

print("Book availability using method:", book.is_available())


# ==================================================
# 9. BORROWED ITEMS LIST
# ==================================================

print("\n7. MEMBER BORROWED ITEMS")

print("Alice's borrowed items:", alice.borrowed_titles())
print("Bob's borrowed items:", bob.borrowed_titles())


# ==================================================
# 10. CLASS ATTRIBUTE
# ==================================================

print("\n8. TOTAL LIBRARY ITEMS")

print("Total items created:", LibraryItem.total_items)


# ==================================================
# 11. ABSTRACT CLASS DEMONSTRATION
# ==================================================

print("\n9. ABSTRACT CLASS CHECK")

try:
    test_item = LibraryItem("Test Item", 99)

except TypeError as e:
    print("Cannot create LibraryItem directly:", e)


print("\n========== PROGRAM COMPLETED ==========")
