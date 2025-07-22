from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

import random
import string

loading = False

def password_cracker(password):
    attempts = 0
    global loading
    loading = True
    while True:
        guess = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(password)))
        attempts += 1
        if guess == password:
            loading = False
            return attempts

class MyApp(App):
    def build(self):
        outer_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        inner_layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint=(None, None),  
            width=300,
            height=200
        )

        self.password_input = TextInput(
            hint_text='Enter the password to crack',
            size_hint_y=None,
            height=50
        )
        inner_layout.add_widget(self.password_input)

        crack_button = Button(
            text='Crack Password',
            size_hint_y=None,
            height=50,
            on_press=self.crack_password
        )
        inner_layout.add_widget(crack_button)

        self.attempts_label = Label(
            text='',
            size_hint_y=None,
            height=50
        )
        inner_layout.add_widget(self.attempts_label)

        outer_layout.add_widget(inner_layout)
        return outer_layout

    def crack_password(self, instance):
        global loading
        password = self.password_input.text
        self.password_input.text = ''

        print("Cracking password...")

        attempts = password_cracker(password)    
        print(f"The password is {password}. It took {attempts} attempts")

        result_text = f"The password is {password}. It took {attempts} attempts" if not loading else "loading..."
        self.attempts_label.text = result_text

if __name__ == '__main__':
    MyApp().run()
