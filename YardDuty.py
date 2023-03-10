import gooeypie as gp
import YardDutyData as yd

Pike = yd.Teachers("P. Pike", "1", "Recess", "L Block")
Currie = yd.Teachers("K. Currie", "2", "Lunch", "Oval")
Green = yd.Teachers("W. Green", "3", "Before School", "Buses")

TeacherIndex = [Pike.name, Currie.name, Green.name]


def swap(event):
    success = 0
    # Column 1 value association
    if Teacher1.selected_index == 0:
        t1 = Pike
        success = success + 1
    elif Teacher1.selected_index == 1:
        t1 = Currie
        success = success + 1
    elif Teacher1.selected_index == 2:
        t1 = Green
        success = success + 1
    # Column 2 Value association
    if Teacher2.selected_index == 0:
        t2 = Pike
        success = success + 1
    elif Teacher2.selected_index == 1:
        t2 = Currie
        success = success + 1
    elif Teacher2.selected_index == 2:
        t2 = Green
        success = success + 1
    
    try:
        # Swap the teacher data using a temporary variable
        temp_day = t1.day
        temp_duty = t1.duty
        temp_time = t1.time

        t1.day = t2.day
        t1.duty = t2.duty
        t1.time = t2.time

        t2.day = temp_day
        t2.duty = temp_duty
        t2.time = temp_time
        print("Successfully Swapped")
    except:
        name1lbl.text = "Please Select a Teacher"
        name2lbl.text = "Please Select a Teacher"
        print(f"Swapping Failed Because Only {success} Teacher/s Was Selected")

    load(event=event)

def load(event):
    success = 0
    try:
        # Column 1
        if Teacher1.selected_index == 0:
            name1lbl.text = "Name: " + Pike.name
            Time1lbl.text = "Time: " + Pike.time
            Day1lbl.text = "Day: " + Pike.day
            Duty1lbl.text = "Duty: " + Pike.duty
            success = success + 1
        elif Teacher1.selected_index == 1:
            name1lbl.text = "Name: " + Currie.name
            Time1lbl.text = "Time: " + Currie.time
            Day1lbl.text = "Day: " + Currie.day
            Duty1lbl.text = "Duty: " + Currie.duty
            success = success + 1
        elif Teacher1.selected_index == 2:
            name1lbl.text = "Name: " + Green.name
            Time1lbl.text = "Time: " + Green.time
            Day1lbl.text = "Day: " + Green.day
            Duty1lbl.text = "Duty: " + Green.duty
            success = success + 1
        # Column 2
        if Teacher2.selected_index == 0:
            name2lbl.text = "Name: " + Pike.name
            Time2lbl.text = "Time: " + Pike.time
            Day2lbl.text = "Day: " + Pike.day
            Duty2lbl.text = "Duty: " + Pike.duty
            success = success + 1
        elif Teacher2.selected_index == 1:
            name2lbl.text = "Name: " + Currie.name
            Time2lbl.text = "Time: " + Currie.time
            Day2lbl.text = "Day: " + Currie.day
            Duty2lbl.text = "Duty: " + Currie.duty
            success = success + 1
        elif Teacher2.selected_index == 2:
            name2lbl.text = "Name: " + Green.name
            Time2lbl.text = "Time: " + Green.time
            Day2lbl.text = "Day: " + Green.day
            Duty2lbl.text = "Duty: " + Green.duty
            success = success + 1
        print(f"Loaded {success} Teacher/s Successfully")
    except:
        print("Failed to load")


# App window settings
app = gp.GooeyPieApp("Yard Duty")
app.set_grid(6, 6)
app.set_icon("icon.png")
# Buttons
swapBtn = gp.ImageButton(app, "swap.png", swap)
Teacher1 = gp.Dropdown(app, TeacherIndex)
Teacher2 = gp.Dropdown(app, TeacherIndex)
# Labels
name1lbl = gp.Label(app, "")
name2lbl = gp.Label(app, "")
Day1lbl = gp.Label(app, "")
Day2lbl = gp.Label(app, "")
Time1lbl = gp.Label(app, "")
Time2lbl = gp.Label(app, "")
Duty1lbl = gp.Label(app, "")
Duty2lbl = gp.Label(app, "")
# Buttons
app.add(Teacher1, 1, 1)
app.add(name1lbl, 2, 1)
app.add(Day1lbl, 3, 1)
app.add(Time1lbl, 4, 1)
app.add(Duty1lbl, 5, 1)
app.add(Teacher2, 1, 2)
app.add(name2lbl, 2, 2)
app.add(Day2lbl, 3, 2)
app.add(Time2lbl, 4, 2)
app.add(Duty2lbl, 5, 2)
app.add(swapBtn, 3, 3)
# Event listeners
Teacher1.add_event_listener("select", load)
Teacher2.add_event_listener("select", load)
# Init app
app.run()

