class Task:
    def __init__(self):
        self.tasks = []

    def add_tasks(self, deadline, description):
        self.tasks.append({"deadline": deadline,
                           "description": description, "status": "Не выполнено"})

    def complete_task(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "Выполнено"
                print(f"Задача '{description}' выполнена")
                return
        print(f"Задача '{description}' не найдена")

    def show_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            print(f"{task['description']} - {task['deadline']} - {task['status']}")

    def show_completed_tasks(self):
        print("Выполненные задачи:")
        for task in self.tasks:
            if task["status"] == "Выполнено":
                print(f"{task['description']} - {task['deadline']}")

    def show_incomplete_tasks(self):
        print("Невыполненные задачи:")
        for task in self.tasks:
            if task["status"] == "Не выполнено":
                print(f"{task['description']} - {task['deadline']}")

# Создание экземпляра класса Task и добавление задач
t = Task()
t.add_tasks(deadline="01.09.2024", description="Прочитать книгу")
t.add_tasks(deadline="05.09.2024", description="Сделать зарядку")
t.add_tasks(deadline="20.09.2024", description="Выучить стих")

# Отметка задачи как выполненной
t.complete_task("Прочитать книгу")

# Вывод всех задач
t.show_tasks()

# Вывод только выполненных задач
t.show_completed_tasks()

# Вывод только невыполненных задач
t.show_incomplete_tasks()

