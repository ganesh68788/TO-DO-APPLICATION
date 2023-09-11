from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do Application')
        self.root.geometry('800x500+300+150')

        self.label1 = Label(self.root, text='To-Do Application', font='ariel, 25 bold', width=30, bd=5, bg='blue', fg='black')
        self.label1.pack(side='top', fill=BOTH, padx=10, pady=10)

        self.label2 = Label(self.root, text='Add Task', font='ariel, 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=20, y=54)

        self.label3 = Label(self.root, text='Tasks', font='ariel, 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=460, y=54)

        self.main_text = Listbox(self.root, height=12, bd=5, width=40, font="ariel, 14")
        self.main_text.place(x=460, y=100)

        self.text = Text(self.root, height=3, bd=5, width=40, font="ariel, 12")
        self.text.place(x=20, y=100)

        self.priority_var = StringVar(self.root)
        self.priority_var.set("Medium")  # Default priority is Medium
        self.priority_options = ["High", "Medium", "Low"]
        self.priority_menu = OptionMenu(self.root, self.priority_var, *self.priority_options)
        self.priority_menu.place(x=140, y=220)

        self.due_date_label = Label(self.root, text="Due Date:", font='ariel, 12 bold', bd=5, bg='orange', fg='black')
        self.due_date_label.place(x=20, y=270)

        self.due_date_entry = Entry(self.root, font='ariel, 12')
        self.due_date_entry.place(x=140, y=270)

        self.load_tasks()

        self.add_button = Button(self.root, text="Add Task", font='arial, 18 bold italic', width=10, bd=5, bg='yellow', fg='black', command=self.add_task)
        self.add_button.place(x=20, y=320)

        self.remove_button = Button(self.root, text="Remove Task", font='arial, 18 bold italic', width=12, bd=5, bg='red', fg='black', command=self.remove_task)
        self.remove_button.place(x=160, y=320)

        self.complete_button = Button(self.root, text="Mark as Completed", font='arial, 16 bold italic', width=18, bd=5, bg='green', fg='black', command=self.mark_completed)
        self.complete_button.place(x=20, y=370)

    def add_task(self):
        task_text = self.text.get(1.0, END).strip()
        if task_text:
            priority = self.priority_var.get()
            due_date = self.due_date_entry.get()
            formatted_task = f"[{priority}] {task_text} (Due: {due_date})"
            self.main_text.insert(END, formatted_task)
            self.save_tasks()
            self.clear_input()

    def remove_task(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            index = selected_index[0]
            self.main_text.delete(index)
            self.save_tasks()

    def mark_completed(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            index = selected_index[0]
            task_text = self.main_text.get(index)
            if "(Completed)" not in task_text:
                self.main_text.delete(index)
                completed_task = task_text.replace("]", "] (Completed)")
                self.main_text.insert(END, completed_task)
                self.save_tasks()

    def load_tasks(self):
        try:
            with open('todo.txt', 'r') as file:
                tasks = [line.strip() for line in file.readlines()]
                for task in tasks:
                    self.main_text.insert(END, task)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        tasks = self.main_text.get(0, END)
        with open('todo.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')

    def clear_input(self):
        self.text.delete(1.0, END)
        self.due_date_entry.delete(0, END)
        self.priority_var.set("Medium")

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()

