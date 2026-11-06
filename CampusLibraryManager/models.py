
# models.py

from abc import ABC, abstractmethod


# ==================================================
# 1. ABSTRACT PARENT CLASS
# ==================================================

class LibraryItem(ABC):

    # Class attribute shared by all LibraryItem objects
    total_items = 0

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

        # Private attribute (Encapsulation)
        self.__available = True

        # Increment total item count
        LibraryItem.total_items += 1

    def is_available(self):
        """Return the availability status of the item."""
        return self.__available

    def mark_borrowed(self):
        """Mark the item as borrowed."""
        if not self.__available:
            raise ValueError(
                f"'{self.title}' is already borrowed."
            )

        self.__available = False

    def mark_returned(self):
        """Mark the item as available."""
        if self.__available:
            raise ValueError(
                f"'{self.title}' is already available."
            )

        self.__available = True

    @abstractmethod
    def late_fee(self, days_late):
        """Every child class must implement its own late fee."""
        pass


# ==================================================
# 2. BOOK CLASS
# ==================================================

class Book(LibraryItem):

    DAILY_RATE = 2

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return (
            f"Book: {self.title} by {self.author} "
            f"(ID {self.item_id})"
        )


# ==================================================
# 3. MAGAZINE CLASS
# ==================================================

class Magazine(LibraryItem):

    DAILY_RATE = 1

    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return (
            f"Magazine: {self.title}, "
            f"Issue No: {self.issue_number} "
            f"(ID {self.item_id})"
        )


# ==================================================
# 4. DVD CLASS
# ==================================================

class DVD(LibraryItem):

    DAILY_RATE = 5

    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return (
            f"DVD: {self.title}, "
            f"Duration: {self.duration_minutes} minutes "
            f"(ID {self.item_id})"
        )


# ==================================================
# 5. MEMBER CLASS
# ==================================================

class Member:

    def __init__(self, name, member_id, max_items=3):
        self.name = name
        self.member_id = member_id
        self.max_items = max_items

        # Private list (Encapsulation)
        self.__borrowed = []

    def borrow(self, item):
        """Allow a member to borrow an available library item."""

        if not isinstance(item, LibraryItem):
            raise ValueError("Invalid library item.")

        if not item.is_available():
            raise ValueError(
                f"'{item.title}' is already borrowed."
            )

        if len(self.__borrowed) >= self.max_items:
            raise ValueError(
                f"{self.name} has reached the borrowing limit "
                f"of {self.max_items} items."
            )

        # Update item availability and member's borrowed list
        item.mark_borrowed()
        self.__borrowed.append(item)

        print(f"{self.name} successfully borrowed '{item.title}'.")

    def return_item(self, item, days_late=0):
        """Return a borrowed item and calculate its late fee."""

        if item not in self.__borrowed:
            raise ValueError(
                f"{self.name} has not borrowed '{item.title}'."
            )

        if isinstance(days_late, bool) or not isinstance(days_late, int) or days_late < 0:
            raise ValueError(
                "Days late must be a non-negative integer."
            )

        # Calculate fee using the item's own implementation
        fee = item.late_fee(days_late)

        # Update availability and borrowed list
        item.mark_returned()
        self.__borrowed.remove(item)

        print(f"{self.name} successfully returned '{item.title}'.")

        return fee

    def borrowed_titles(self):
        """Return a copy of borrowed item titles."""
        return [item.title for item in self.__borrowed]
