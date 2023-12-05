import requests
from django.shortcuts import render
from .models import Master, Appointment
# Create your views here.
from datetime import date, datetime, timedelta
from openai import OpenAI


def main(request):
    #del request.session['appointments']
    try:
        print(request.session['appointments'])
    except:
        request.session['appointments'] = []
    if request.method == 'GET':
        all_masters = Master.objects.all()
        today = datetime.today()
        date_ = str(datetime(today.year, today.month, today.day))
        date_ = date_[0:date_.find(' ')].split('-')
        all_weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        d1 = date(int(date_[0]), int(date_[1]), int(date_[2]))
        d2 = date(int(date_[0]) + 1, int(date_[1]), int(date_[2]))
        delta = d2 - d1  # returns timedelta
        final_data = {}
        timings = {}
        for master in all_masters:
            master_name = master.name
            master_time = [i.split(',') for i in master.timetable.split(";")]
            timings[master_name] = master_time
        data_dynamic = []
        for _ in range(today.weekday()):
            data_dynamic.append(f'  -{all_weeks[today.weekday()].split("-")[0]}-{timings}')
        all_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']
        for i in range(delta.days + 1):
            day = d1 + timedelta(days=i)
            weekday = day.weekday()
            curr_day = str(day).split("-")[2]
            if curr_day == '01' and len(data_dynamic) > 1:
                month_year = f"{all_months[int(str(day).split('-')[1]) - 2]}-{str(d1 + timedelta(days=i - 1)).split('-')[0]}"
                final_data[month_year] = data_dynamic
                new_data = []
                for _ in range(len(data_dynamic) % 7):
                    new_data.append(f'  -{all_weeks[weekday].split("-")[0]}-{timings}')
                data_dynamic = [i for i in new_data]
            else:
                pass
            data_dynamic.append(f'{curr_day}-{all_weeks[weekday].split("-")[0]}-{timings}')

        return render(request, 'main/index.html',
                      {'all_masters': all_masters, 'final_data': final_data, 'timings': timings,
                       'all_weeks': all_weeks})
    else:
        all_masters = Master.objects.all()
        today = datetime.today()
        date_ = str(datetime(today.year, today.month, today.day))
        date_ = date_[0:date_.find(' ')].split('-')
        all_weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        d1 = date(int(date_[0]), int(date_[1]), int(date_[2]))
        d2 = date(int(date_[0]) + 1, int(date_[1]), int(date_[2]))
        delta = d2 - d1  # returns timedelta
        final_data = {}
        timings = {}
        for master in all_masters:
            master_name = master.name
            master_time = [i.split(',') for i in master.timetable.split(";")]
            timings[master_name] = master_time
        data_dynamic = []
        for _ in range(today.weekday()):
            data_dynamic.append(f'  -{all_weeks[today.weekday()].split("-")[0]}-{timings}')
        all_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']
        for i in range(delta.days + 1):
            day = d1 + timedelta(days=i)
            weekday = day.weekday()
            curr_day = str(day).split("-")[2]
            if curr_day == '01' and len(data_dynamic) > 1:
                month_year = f"{all_months[int(str(day).split('-')[1]) - 2]}-{str(d1 + timedelta(days=i - 1)).split('-')[0]}"
                final_data[month_year] = data_dynamic
                new_data = []
                for _ in range(len(data_dynamic) % 7):
                    new_data.append(f'  -{all_weeks[weekday].split("-")[0]}-{timings}')
                data_dynamic = [i for i in new_data]
            else:
                pass
            data_dynamic.append(f'{curr_day}-{all_weeks[weekday].split("-")[0]}-{timings}')
        owner_name = request.POST['owner_name']
        master_name = request.POST['master_name']
        master = Master.objects.get(name=master_name)
        month = request.POST['month']
        year = request.POST['year']
        timing = request.POST['select_time'].replace(' ', '')
        new_time = datetime.strptime(timing, '%I:%M%p').strftime("%H:%M")
        dayOfMonth = request.POST['dayOfMonth']
        weekday = request.POST['weekday']
        try: print(Appointment.objects.get(date=f'{year}-{month}-{dayOfMonth} {new_time}'))
        except:
            a = Appointment(master_name=master, date=f"{year}-{month}-{dayOfMonth} {new_time}", owner_name=owner_name)
            a.save()
            a = Appointment.objects.get(date=f"{year}-{month}-{dayOfMonth} {new_time}")
            appointment = [a.id, master_name, f"{year}-{month}-{dayOfMonth} {new_time}"]
            request.session['appointments'].append(appointment)
            return render(request, 'main/index.html',
                          {'all_masters': all_masters, 'final_data': final_data, 'timings': timings,
                           'all_weeks': all_weeks})
        return render(request, 'main/busy.html')

def appointments(request):
    try:
        print(request.session['appointments'])
    except:
        request.session['appointments'] = []
    appointments = request.session['appointments']
    return render(request, 'main/appointments.html', {'appointments': appointments})


def delete_appointment(request, appointment_id):
    Appointment.objects.get(id=appointment_id).delete()
    a = [request.session['appointments'].index(i) for i in request.session['appointments'] if i[0] == appointment_id]
    del request.session['appointments'][a[0]]
    appointments = request.session['appointments']
    return render(request, 'main/appointments.html', {'appointments': appointments})


def ia(request):
    if request.method == 'GET':
        return render(request, 'main/ia.html', {})
    else:
        
        return render(request, 'main/ia.html', {})
