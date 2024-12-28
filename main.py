from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import init_db, insert_user, get_users

class FormScreen(BoxLayout):
    def submit(self):
        name = self.ids.name_input.text
        email = self.ids.email_input.text

        if name and email:
            try:
                insert_user(name, email)
                self.ids.name_input.text = ""
                self.ids.email_input.text = ""
                self.show_popup("Success", "User added successfully!")
            except Exception as e:
                self.show_popup("Error", str(e))
        else:
            self.show_popup("Error", "Please fill all fields!")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message),
                      size_hint=(0.8, 0.4))
        popup.open()

    def display_users(self):
        users = get_users()
        user_list = "\n".join([f"{user[0]}: {user[1]} - {user[2]}" for user in users])
        self.show_popup("Users", user_list if user_list else "No users found.")

class FormApp(App):
    def build(self):
        init_db()  # Initialize the database
        return FormScreen()

if __name__ == "__main__":
    FormApp().run()
