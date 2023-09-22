export class TodoList {
    constructor() {
      this.tasks = [];
    }
  
    addTask(task) {
      this.tasks.push({ task, complete: false });
    }
  
    markTaskAsComplete(index) {
      if (index >= 0 && index < this.tasks.length) {
        this.tasks[index].complete = true;
      }
    }
  
    listTasks() {
      return this.tasks.map((task, index) => ({
        task: task.task,
        complete: task.complete,
        index,
      }));
    }
  }
  