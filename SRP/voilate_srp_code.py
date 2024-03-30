class Tasks:
    def __init__(self):
        self.tasks_list = []

    def add_tasks(self, task):
        self.tasks_list.append(task)
        return self.tasks_list

    def delete_tasks(self, task):
        self.tasks_list.remove(task)
        return self.tasks_list

    def display_task(self, tasks):
        for task in tasks:
            print(task)

    def enter_task(self):
        return input("Enter task -> ")

    def remove_task(self):
        return input("Remove task")