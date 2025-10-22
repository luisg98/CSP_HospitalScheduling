## Hospital Bed Assignment using CSP (Constraint Satisfaction Problem)

This project implements an intelligent hospital bed assignment system using Constraint Satisfaction Problem (CSP) techniques.
It automatically assigns patients to available beds according to multiple constraints such as age, gender, department, and intensive care requirements.
The project also includes a Gantt chart visualization of bed occupancy over time.

🧠 Overview

The goal of this project is to automatically allocate hospital beds to patients while satisfying a set of logical and temporal constraints, including:

Department compatibility (adults, children, babies)

Gender restrictions per room

Intensive care (ICU) requirements

Non-overlapping stay periods

Bed availability and capacity

The system uses arc consistency algorithms (AC3 / AC4) to ensure all constraints are satisfied.
The resulting assignments are displayed as a Gantt chart, showing when and where each patient is assigned.


🚀 Key Features

✅ Automatic reading and parsing of hospital datasets
✅ Flexible modeling of variables, domains, and constraints
✅ Constraint propagation using AC3 / AC4 algorithms
✅ Graphical Gantt chart visualization of assignments
✅ Department, gender, and ICU-aware scheduling
✅ Support for overlapping admission periods

📊 Output and Visualization

After running, the program prints the patient → bed assignment and generates a Gantt chart illustrating bed occupancy over time.

Color legend:

🟦 Blue: regular care

🟥 Red: intensive care (ICU)

🟩 Green: cleaning day after discharge

🧾 Legend: department zones — Adults, Children, Babies
