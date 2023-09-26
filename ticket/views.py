import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket
from .form import CreateTicketForm,UpdateTicketForm
from users.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

# عرض تفاصيل التداكر
@login_required
def ticket_details(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    t = User.objects.get(username=ticket.created_by)
    tickets_per_user = t.created_by.filter(created_by=request.user) # tickets_per_user = t.created_by.filter(assigned_to=request.user)
    tickets_per_emp = t.created_by.filter(assigned_to=request.user)
    context = {'ticket':ticket,'tickets_per_user':tickets_per_user, 'tickets_per_emp':tickets_per_emp }
    return render(request, 'ticket/ticket_details.html', context)

# def all_tickets(request):
#     tickets = Ticket.objects.filter(created_by=request.user).order_by('-date_created')
#     context = {'tickets':tickets}
#     return render(request, 'ticket/all_tickets.html', context)
# ========== For Students ================


# تداكر الطلاب 

# create a ticket
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.ticket_status = 'Opening'
            var.save()
            messages.info(request, 'Your Ticket Has Been Submitted , An Employee Would Be Assigned Soon ...!')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Sorry ! Something Went Wrong , Your Ticket Has Not Been Submitted  ...!!')
            return redirect('create_ticket')
    else:
        form = CreateTicketForm()
        context = {'form':form}
        return render(request, 'ticket/create_ticket.html', context)
    
# تحديث حالة التداكر

# Update ticket
@login_required
def update_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if not ticket.is_resolved:
        if request.method == 'POST':
            form = CreateTicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                messages.info(request, 'Your Ticket Has Been Updated , Changed Will Be Saved ...!')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Sorry ! Something Went Wrong , Your Ticket Has Not Been Submitted  ...!!')
            # return redirect('create_ticket')
        else:
            form = UpdateTicketForm(instance=ticket)
            context = {'form':form}
            return render(request, 'ticket/update_ticket.html', context)
    else:
        messages.warning(request, 'Sorry ! You Can Not Update Ticket , Your Ticket Has Not Been On Progress  ...!!')
        return redirect('dashboard')
    

#  عرض جميع التداكر المضافة بواسطة الطالب
# view all created tickets
# @login_required
# def all_tickets(request):
#     tickets = Ticket.objects.filter(created_by=request.user).order_by('-date_created')
#     context = {'tickets':tickets}
#     return render(request, 'ticket/all_tickets.html', context)


@login_required
def all_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user).order_by('-date_created')
    total_tickets = tickets.count() #  
    complete = tickets.filter(ticket_status='Completed').count()
    reject = tickets.filter(ticket_status='Rejected').count()
    open = tickets.filter(ticket_status='Opening').count()
    proccess = tickets.filter(ticket_status='Processing').count()
    
    context = {'tickets':tickets, 'total_tickets':total_tickets,'complete':complete ,'reject':reject , 'open':open , 'proccess': proccess}
    return render(request, 'ticket/all_tickets.html', context)


# حدف التداكر المرفوظة للطالب

@login_required
def ticket_deletion(request , pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.created_by = request.user
    if ticket.is_deleted == True:
        ticket.delete()
        messages.info(request, 'Ticket Has Been Deleted ...!')
    
        return redirect('dashboard')
    else:
        messages.info(request, 'Ticket Has Not Been Deleted , Please Make Sure If It Is Really Rejected ... ??? ')
    
        return redirect('dashboard')


# ========== For Employeers ================

# عرض جميع التداكر للموظف
@login_required
def ticket_queue(request):
    tickets = Ticket.objects.filter(ticket_status='Opening')
    context = {'tickets':tickets}
    return render(request, 'ticket/ticket_queue.html', context)



# التداكر المقبولة من الجدول
@login_required
def accept_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.assigned_to = request.user
    ticket.ticket_status = 'Processing'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket Has Been Accepted , Please Resolve As Soon As Possible ...!')
    return redirect('workspace')


# التداكر المحدوفة
@login_required
def reject_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.assigned_to = request.user
    ticket.ticket_status = 'Rejected'
    ticket.is_resolved = True
    ticket.is_deleted = True
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket Has Been Rejected , Good Luck Again ...!')
    return redirect('ticket_queue')



# التداكر المنجزة  
@login_required
def close_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.ticket_status = 'Completed'
    ticket.is_resolved = True
    ticket.is_archived = True
    ticket.closed_date = datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket Has Been Resolved , Thank you Support Employee ...!')
    return redirect('ticket_queue')



# التداكر قيد العمل من قبل الموظف 
@login_required
def workspace(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_resolved=False)
    context = {'tickets':tickets}
    return render(request, 'ticket/workspace.html', context)


# كل التداكر المقفلة والمراجعه
@login_required
def all_closed_tickets(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_resolved=True, is_archived=True)
    context = {'tickets':tickets}
    return render(request, 'ticket/all_closed_tickets.html', context)

# كل التداكر المرفوضة
@login_required
def all_rejected_tickets(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_deleted=True)
    context = {'tickets':tickets}
    return render(request, 'ticket/all_rejected_tickets.html', context)