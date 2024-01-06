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
            room_name = ' '.join(words[1:-3])
            room_gender = words[-3]
            room_department = int(words[-2])
            intensive_care = int(words[-1])

            room_departments[room_id] = {
                'name': room_name,
                'gender': room_gender,
                'dept': room_department,
                'intensive_care': intensive_care
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
            patient_age = int(words[-5])
            patient_gender = words[-4]
            admission_day = int(words[-3])
            discharge_day = int(words[-2])
            intensive_care = int(words[-1])

            patients_data[patient_id] = {
                #'name': patient_name,
                'age': patient_age,
                'gender': patient_gender,
                'admission_day': admission_day,
                'discharge_day': discharge_day,
                'intensive_care': intensive_care
            }

    return bed_rooms, room_departments, patients_data
