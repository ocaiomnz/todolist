import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Afazeres")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=35)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_task_btn = tk.Button(self.frame, text="Adicionar Tarefa", command=self.add_task)
        self.add_task_btn.pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self.delete_task_btn = tk.Button(self.buttons_frame, text="Excluir Tarefa", command=self.delete_task)
        self.delete_task_btn.pack(side=tk.LEFT, padx=5)

        self.mark_completed_btn = tk.Button(self.buttons_frame, text="Marcar como Concluída", command=self.mark_completed)
        self.mark_completed_btn.pack(side=tk.LEFT, padx=5)

        self.consult_task_btn = tk.Button(self.buttons_frame, text="Consultar Tarefa", command=self.consult_task)
        self.consult_task_btn.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Seleção de Tarefa", "Por favor, selecione uma tarefa para excluir.")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Seleção de Tarefa", "Por favor, selecione uma tarefa para marcar como concluída.")

    def consult_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_info = self.tasks[selected_task_index[0]]
            status = "Concluída" if task_info["completed"] else "Pendente"
            messagebox.showinfo("Informação da Tarefa", f"Tarefa: {task_info['task']}\nStatus: {status}")
        else:
            messagebox.showwarning("Seleção de Tarefa", "Por favor, selecione uma tarefa para consultar.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[Concluída]" if task["completed"] else "[Pendente]"
            self.task_listbox.insert(tk.END, f"{status} {task['task']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
