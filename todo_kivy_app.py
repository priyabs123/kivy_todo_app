from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class ToDoApp(App):
    def build(self):
        self.tasks = []

        self.layout = BoxLayout(orientation='vertical')

        # Input for tasks
        self.task_input = TextInput(hint_text='Enter a task', multiline=False)
        self.layout.add_widget(self.task_input)

        # Button to add task
        add_button = Button(text='Add Task')
        add_button.bind(on_press=self.add_task)
        self.layout.add_widget(add_button)

        # Label to show tasks
        self.task_label = Label(text='Your tasks will appear here.')
        self.layout.add_widget(self.task_label)

        # Clear all button
        clear_button = Button(text='Clear All Tasks')
        clear_button.bind(on_press=self.clear_tasks)
        self.layout.add_widget(clear_button)

        return self.layout

    def add_task(self, instance):
        task = self.task_input.text
        if task:
            self.tasks.append(task)
            self.task_input.text = ''
            self.update_tasks()

    def update_tasks(self):
        self.task_label.text = '\n'.join(f"• {t}" for t in self.tasks)

    def clear_tasks(self, instance):
        self.tasks = []
        self.update_tasks()

ToDoApp().run()