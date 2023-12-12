""" (U w U)_/××××××××××××××××××××  CLI  ××××××××××××××××××××\_(U w U) """

from datetime import datetime
import click
from uwudu.file import read_todo_list, write_todo_list
from uwudu.table import StyledTable

table = StyledTable()


@click.group()
@click.version_option()
def cli():
    pass


# ----------------- ADD TASK ---------------------
@cli.command(help="--- \033[3madd your task to todo list\033[0m \n")
@click.argument("task", nargs=-1, required=True)
def add(task):
    task = " ".join(task)
    time = datetime.now().strftime("%d %b %y %H:%M")
    new_task = f" {len(read_todo_list()) + 1} │ {task} │ ongoing │ {time} │ {time} "
    todo_list = read_todo_list()
    todo_list.append(new_task)
    write_todo_list(todo_list)
    click.echo(f"Task '{task}' added to the todo list \033[3m\_( U w U )_/\033[0m \n")
    table.display(todo_list)


# ----------------- SET TASK STATUS ---------------------
@cli.command(
    name="status",
    help="--- \033[3mset task status, eg: uwudu status 'task id' 'status'\033[0m \n",
)
@click.argument("task_id", type=int, required=True)
@click.argument("status", required=True)
def set_status(task_id, status):
    todo_list = read_todo_list()
    time = datetime.now().strftime("%d %b %y %H:%M")
    if 1 <= task_id <= len(todo_list):
        task = todo_list[task_id - 1].split("│")
        todo_list[task_id - 1] = f" {task_id} │ {task[1]} │ {status} │ {task[3]} │ {time} "
        write_todo_list(todo_list)
        click.echo(
            f"Updated the status of task-'{task_id}' in the todo list"\
            "  \033[3m\_( U w U )_/\033[0m \n"
        )
    else:
        click.echo(
            "Invalid task number. Use 'show' to see the list and select a valid task number."
        )
    table.display(todo_list)


# ----------------- MARK TASK FINISHED ---------------------
@cli.command(help="--- \033[3mfinish task, eg: uwudu finish 'task id'\033[0m \n")
@click.argument("task_id", type=int, required=True)
def finish(task_id):
    todo_list = read_todo_list()
    time = datetime.now().strftime("%d %b %y %H:%M")
    if 1 <= task_id <= len(todo_list):
        task = todo_list[task_id - 1].split("│")
        todo_list[task_id - 1] = f" {task_id} │ {task[1]} │ done │ {task[3]} │ {time} "
        write_todo_list(todo_list)
        click.echo(f"marked task-'{task_id}' as finished \033[3m\_( U w U )_/\033[0m \n")
    else:
        click.echo(
            "Invalid task number. Use 'show' to see the list and select a valid task number."
        )
    table.display(todo_list)


# ----------------- REMOVE TASK ---------------------
@cli.command(help="--- \033[3mremove the task with task number from the list\033[0m \n")
@click.argument("task_id", type=int)
def remove(task_id):
    todo_list = read_todo_list()

    if 1 <= task_id <= len(todo_list):
        removed_task = todo_list.pop(task_id - 1).split("│")[1].strip()
        write_todo_list(todo_list)
        click.echo(
            f"Task '{removed_task}' removed from the todo list  \033[3m\_( U w U )_/\033[0m \n"
        )
    else:
        click.echo(
            "Invalid task number. Use 'show' to see the list and select a valid task number."
        )
    table.display(todo_list)


# ----------------- SHOW TASK LIST ---------------------
@cli.command(help="--- \033[3mlist all of your tasks\033[0m \n")
def show():
    todo_list = read_todo_list()
    table.display(todo_list)


# ----------------- RESET TASK LIST ---------------------
@cli.command(help="--- \033[3mreset todo list\033[0m \n")
def reset():
    click.echo("your todo list has been reset! \033[3m\_( U w U )_/\033[0m \n")
    write_todo_list([])
    table.display([])


if __name__ == "__main__":
    cli()

############################# (× __ ×) ###############################
