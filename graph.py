import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def create_gantt_chart(solution, bed_rooms, patients_data):
    tasks = []
    unique_patients = list(set(solution.values()))

    colors = plt.cm.tab20.colors

    for patient_num_str, bed_num in solution.items():
        patient_num = int(patient_num_str.replace('patient', ''))
        admission_day = patients_data[patient_num]['admission_day']
        discharge_day = patients_data[patient_num]['discharge_day']

        start_date = datetime(2023, 1, 1) + timedelta(days=admission_day)
        end_date = datetime(2023, 1, 1) + timedelta(days=discharge_day)

        tasks.append((bed_num, start_date, end_date, f'P{patient_num}'))

    fig, ax = plt.subplots(figsize=(10, 5))

    for idx, task in enumerate(tasks):
        bar_width = mdates.date2num(task[2]) - mdates.date2num(task[1])
        ax.barh(y=task[0], left=mdates.date2num(task[1]), width=bar_width, label=task[3], color=colors[idx % len(colors)], edgecolor='black')

        ax.text(mdates.date2num(task[1]) + bar_width / 2, task[0], task[3],
                va='center', ha='center', color='black', fontweight='bold')

    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))

    ax.set_yticks(list(bed_rooms.keys()))
    ax.set_yticklabels(list(bed_rooms.keys()))

    ax.set_xlim(left=mdates.date2num(datetime(2023, 1, 1)), right=mdates.date2num(max(task[2] for task in tasks)))

    plt.xlabel('Days')
    plt.ylabel('Beds')
    plt.title('CSP Solution Gantt Chart')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    plt.show()
