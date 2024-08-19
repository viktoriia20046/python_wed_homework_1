from abc import ABC, abstractmethod

class View(ABC):

    @abstractmethod
    def display(self, data):
        pass

class ConsoleView(View):
    def display(self, data):
        print("----- Інформація -----")
        for key, value in data.items():
            print(f"{key}: {value}")
        print("----------------------")

class PersonalAssistant:

    def __init__(self, view: View):
        self.view = view
    
    def show_contact_card(self, contact_info):
        self.view.display(contact_info)

contact_info = {
    "Ім'я": "Іван",
    "Телефон": "+380123456789",
    "Емейл": "ivan@example.com"
}

console_view = ConsoleView()

assistant = PersonalAssistant(console_view)

assistant.show_contact_card(contact_info)