from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ticket.models import Ticket
from users.models import User
# Create your views here.

@login_required
def dashboard(request):
    user = User.objects.all()

    if request.user.is_student == True:
        tickets = Ticket.objects.filter(created_by=request.user)
        total_tickets = tickets.count() #  
        complete = tickets.filter(ticket_status='Completed').count()
        reject = tickets.filter(ticket_status='Rejected').count()
        open = tickets.filter(ticket_status='Opening').count()
        proccess = tickets.filter(ticket_status='Processing').count()
    
        context = {'tickets':tickets, 'total_tickets':total_tickets,'complete':complete ,'reject':reject , 'open':open , 'proccess': proccess}
        return render(request, 'dashboard/dashboard.html', context)

    elif request.user.is_employee == True:
        tickets = Ticket.objects.filter(assigned_to=request.user)
        total_tickets = tickets.count() #  
        complete = tickets.filter(ticket_status='Completed').count()
        reject = tickets.filter(ticket_status='Rejected').count()
        op_tic = Ticket.objects.filter(ticket_status='Opening')
        all_tic = op_tic.count()
        # open = tickets.filter(ticket_status='Opening').count()
        proccess = tickets.filter(ticket_status='Processing').count()
    
        context = {'tickets':tickets, 'total_tickets':total_tickets,'complete':complete ,'reject':reject , 'all_tic':all_tic , 'proccess': proccess}
        return render(request, 'dashboard/dashboard.html', context)
    else:
        return render(request, 'dashboard/admin.html')
    

def admin_here(request):

    return render(request, 'dashboard/admin.html')
        