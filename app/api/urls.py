from django.urls import path, include

urlpatterns = [
    path('employee/', include('app.api.employee.urls')),
    path('position/', include('app.api.position.urls')),
    path('project/', include('app.api.project.urls')),
    path('attendance/', include('app.api.attendance.urls')),
    path('accountant/', include('app.api.accountant.urls')),
    path('statistica/', include('app.api.statistica.urls')),
    path('user/', include('app.api.user.urls')),
    path('group/', include('app.api.group.urls')),
    path('websocket/', include('app.api.websocket.urls'))

]