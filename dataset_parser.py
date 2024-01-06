def dataset_parser(dataset):
    bed_rooms = {}
    room_departments = {}
    patients_data = {}

    lines = dataset.strip().split('\n')
    current_section = None

    for line in lines:
        words = line.split()

        if not words:
            continue

        if words[0] in ['DEPARTMENTS:', 'ROOMS:', 'BEDS:', 'PATIENTS:']:
            current_section = words[0].rstrip(':')
            continue

        if current_section == 'DEPARTMENTS':
            if words[0] == 'END.':
                break

            # department_id = int(words[0])
            # department_name = ' '.join(words[1:])

            # room_departments[department_id] = {
            #     'name': department_name
            # }

        elif current_section == 'ROOMS':
            if words[0] == 'END.':
                break

            room_id = int(words[0])
            room_name = ' '.join(words[1:-4])
            room_capacity = int(words[-4])
            room_department = int(words[-3])
            telemetry = int(words[-2])
            oxygen = int(words[-1])

            room_departments[room_id] = {
                'name': room_name,
                'capac': room_capacity,
                'dept': room_department,
                'telemetry': telemetry,
                'oxygen': oxygen
            }

        elif current_section == 'BEDS':
            if words[0] == 'END.':
                break

            bed_id, bed_room_id = map(str, words)
            bed_rooms[int(bed_id)] = bed_room_id



        elif current_section == 'PATIENTS':
            if words[0] == 'END.':
                break

            patient_id = int(words[0])
            #patient_name = ' '.join(words[1:-7])
            patient_age = int(words[-7])
            patient_gender = words[-6]
            admission_day = int(words[-5])
            discharge_day = int(words[-4])
            dept = int(words[-3])
            telemetry = int(words[-2])
            oxygen = int(words[-1])

            patients_data[patient_id] = {
                #'name': patient_name,
                'age': patient_age,
                'gender': patient_gender,
                'admission_day': admission_day,
                'discharge_day': discharge_day,
                'dept': dept,
                'telemetry': telemetry,
                'oxygen': oxygen
            }

    return bed_rooms, room_departments, patients_data
