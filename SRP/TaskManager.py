class TaskManager:
    def __init__(self):
        self.tasks_list = []

    def add_tasks(self, task):
        self.tasks_list.append(task)
        return self.tasks_list

    def delete_tasks(self, task):
        self.tasks_list.remove(task)
        return self.tasks_list

class TaskDisplay:
    @staticmethod
    def display_task(tasks):
        for task in tasks:
            print(task)

class TaskInput:
    @staticmethod
    def enter_task():
        return input("Enter task -> ")

    @staticmethod
    def remove_task():
        return input("Remove task")

def feed_taskS(tasks_number):
    global task_list
    task_man = TaskManager()
    task_display = TaskDisplay
    for i in range(0, tasks_number):
        enter_task = TaskInput.enter_task()
        task_list = task_man.add_tasks(enter_task)

    task_display.display_task(task_list)
    remove_task = TaskInput.remove_task()
    task_list = task_man.delete_tasks(remove_task)
    task_display.display_task(task_list)

feed_taskS(3)