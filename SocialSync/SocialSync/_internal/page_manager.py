

class Book:
    def __init__(self):
        self.pages = []
        self.line_limit = 10
        self.current_page = 0
        self.limit_counter = 1
        self.page_counter = 0

    def fill(self, lines):
        limit_counter = 0
        page = []
        for line in lines:
            if limit_counter == self.line_limit:
                self.pages.append(page)
                page = []
                limit_counter = 0
            page.append(line)
            limit_counter += 1
        self.pages.append(page)

    def add(self, line):
        if self.limit_counter == 1:
            page = []
            page.append(line)
            self.pages.append(page)
            self.limit_counter += 1
        elif self.limit_counter == self.line_limit:
            self.pages[self.page_counter].append(line)
            self.limit_counter = 1
            self.page_counter += 1
        else:
            self.pages[self.page_counter].append(line)
            self.limit_counter += 1

    def empty(self):
        self.pages = []
        self.current_page = 0
        self.limit_counter = 1
        self.page_counter = 0

    def next_page(self):
        if self.current_page == len(self.pages) - 1:
            pass
        else:
            self.current_page += 1

    def previous_page(self):
        if self.current_page == 0:
            pass
        else:
            self.current_page -= 1

    def book_len(self):
        return len(self.pages) - 1

    def get_page(self):
        return self.pages[self.current_page]
