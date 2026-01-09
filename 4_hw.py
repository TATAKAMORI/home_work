class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

r1 = Rectangle(10, 20)
print(r1.area())
print(r1.perimeter())

r2 = Rectangle(25, 50)
print(r2.area())
print(r2.perimeter())

r3 = Rectangle(30, 40)
print(r3.area())
print(r3.perimeter())


class Math:

    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

print(Math().addition(5, 6))
print(Math().subtraction(5, 6))
print(Math().multiplication(5, 6))
print(Math().division(5, 6))


class Button:

    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print('Клик по кнопке {}'.format(self.text))

Text_Box = Button('Text Box', 'button', 'loc')
Text_Box.click()

Check_Box = Button('Check Box', 'button', 'loc')
Check_Box.click()

Radio_Button = Button('Radio Button', 'button', 'loc')
Radio_Button.click()

Web_Tables = Button('Web Tables', 'button', 'loc')
Web_Tables.click()

Buttons = Button('Buttons', 'button', 'loc')
Buttons.click()

Links = Button('Links', 'button', 'loc')
Links.click()

Broken_Links = Button('Broken Links - Images', 'button', 'loc')
Broken_Links.click()

Upload_and_Download = Button('Upload and Download', 'button', 'loc')
Upload_and_Download.click()

Dynamic_Properties = Button('Dynamic Properties', 'button', 'loc')
Dynamic_Properties.click()


