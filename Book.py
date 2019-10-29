class Book:
    def __init__(self, title, author, publisher, year, pages, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.isbn = isbn

        self.is_bulky = (self.pages > 500)

    def is_valuable(self, current_year):
        age = (current_year - self.year)
        return age < 1 or age > 20

    def is_isbn_valid(self):
        check_digit = self.isbn % 10

        digits = list(str(self.isbn))
        digits.pop()
        digits = list(map(int, digits))

        expected_check_digit = 0

        for index in range(len(digits)):
            expected_check_digit += digits[index] * (index + 1)

        expected_check_digit %= 11

        print(expected_check_digit)

        return expected_check_digit == check_digit