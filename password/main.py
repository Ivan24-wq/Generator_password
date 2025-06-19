import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
Window.clearcolor = (0.56, 0.93, 0.56, 1)
Builder.load_file("password.kv")
class Password(BoxLayout):
# generation password
    def generation_password(self, num):
        if num < 2:
            return "пароль должен состоять не менее чем из двух символов!"
        char = '!@#$%^&*()_-+=123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefjhijklmnoprqstuvwxyz'
        password = ' '
        for _ in range(num):
            password += random.choice(char)
        return password

    def on_generate_password(self, instance):
        try:
            num = int(self.ids.length_input.text)
            password = self.generation_password(num)
        except ValueError:
            password = 'Ошибка: введите корректное число'
        self.ids.result_label.text = password
    def open_settings(self):
        popup = Popup(
            title = 'Настройки', 
            content = Label(text = "Настройки"),
            size_hint = (0.8, 0.4)
        )
        popup.open()
class MyApp(App):
    def build(self):
        return Password()
if __name__ == "__main__":
    MyApp().run()