import  {TodoList}  from './todo.js';

const todoList = new TodoList();

todoList.addTask('Buy groceries');
todoList.addTask('Complete homework');

todoList.markTaskAsComplete(1);

const tasks = todoList.listTasks();
console.log('Todo List:');
tasks.forEach((task) => {
  console.log(`${task.complete ? '✅' : '❌'} ${task.task}`);
});
