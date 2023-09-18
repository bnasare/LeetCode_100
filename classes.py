class Cookies:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookies_one = Cookies('red')
cookies_two = Cookies('red')

cookies_one.set_color('yellow')

print('I love', cookies_two.get_color())
print('I love', cookies_one.get_color())
