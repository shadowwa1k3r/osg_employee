from django.contrib import admin

from .model import Employee, Attendance, Employee_group, Group, Position, Task, Project, Accountant, Employee_salary, Chat, Room, Message


admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Employee_group)
admin.site.register(Group)
admin.site.register(Position)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Accountant)
admin.site.register(Employee_salary)
admin.site.register(Chat)
admin.site.register(Room)
admin.site.register(Message)
# Register your models here.
