from django.shortcuts import render, redirect, get_object_or_404
from .models import TeamMember, OffDay
from .forms import TeamMemberForm, OffDayForm
from django.utils import timezone
import pytz

# Singapore timezone
singapore_tz = pytz.timezone('Asia/Singapore')

def offdayapp(request):
    team_members = TeamMember.objects.all()

    # Prepare team schedule with off days and leave days
    team_schedule = []
    for member in team_members:
        off_days = OffDay.objects.filter(team_member=member, type='off').values_list('day', flat=True)
        leave_days = OffDay.objects.filter(team_member=member, type='leave').values_list('day', flat=True)
        team_schedule.append({
            'member': member,
            'off_days': list(off_days),
            'leave_days': list(leave_days)
        })

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if request.method == 'POST':
        # Handle clearing all off days
        if 'clear_off_days' in request.POST and request.user.is_staff:
            OffDay.objects.all().delete()
            return redirect('offdayapp')

        # Handle adding a member
        elif 'add_member' in request.POST:
            form = TeamMemberForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('offdayapp')

        # Handle submitting an off day or leave
        elif 'submit_day' in request.POST:
            team_member_id = request.POST.get('team_member')
            selected_day = request.POST.get('day')
            selected_type = request.POST.get('type')  # 'off' or 'leave'

            if team_member_id and selected_day and selected_type:
                team_member = get_object_or_404(TeamMember, id=team_member_id)

                # Check if an entry already exists for the same day and member
                existing_entry = OffDay.objects.filter(team_member=team_member, day=selected_day).first()
                if existing_entry:
                    existing_entry.type = selected_type  # Update type if it exists
                    existing_entry.save()
                else:
                    OffDay.objects.create(team_member=team_member, day=selected_day, type=selected_type)

                return redirect('offdayapp')

    # Initialize forms
    form = TeamMemberForm()
    off_day_form = OffDayForm()

    return render(request, 'home.html', {
        'team_members': team_members,
        'team_schedule': team_schedule,
        'days_of_week': days_of_week,
        'form': form,
        'off_day_form': off_day_form,
    })
