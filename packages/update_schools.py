def update_schools(self, selected_town): 
        # Update the school dropdown based on the selected town
        schools_by_town = {
            "Central Office": ["Administration", "Archives/Family Resource", "Attendance", "Benefits", "CTE", "School Health", "Finance", "Human Resources", "Instruction", "Nursing", "Nutrition", "Pupil Services", "Safe Schools", "Teacher Center", "Unity"],
            "SSF": ["Technology", "Maintenance", "Transportation", "Lawn Center", "Operations"],
            "Gallatin": ["Benny Bills Elementary", "Howard Elementary", "Guild Elementary",  "Liberty Creek Elementary",
                         "R.T. Fisher Alternative", "Station Camp Elementary", "Union STEM Elementary", "Vena Stewart Elementary",
                         "Liberty Creek Middle", "Shafer Middle", "Rucker-Stewart Middle", "Station Camp Middle", "Gallatin High School", "Liberty Creek High School", "Station Camp High School"],
            "Hendersonville": ["Beech Elementary", "George Whitten Elementary", "Gene Brown Elementary", "Indian Lake Elementary", "Jack Anderson Elementary", "Lakeside Park Elementary",
                               "Merrol Hyde Magnet", "Nannie Berry Elementary", "Walton Ferry Elementary", "William Burrus Elementary", "Ellis Middle", "Hawkins Middle", "Knox Doss Middle",
                               "T.W. Hunter Middle", "Hendersonville High School","Beech High School"],
            "White House": ["H.B. Williams Elementary", "White House Middle", "White House Intermediate",
                            "White House High School (Main)", "White House High School (Annex)"],
            "Portland": ["Clyde Riggs Elementary", "J.W. Wiseman Elementary", "Portland Gateview Elementary",
                         "Watt Hardison Elementary", "Portland East Middle", "Portland West Middle", "Portland High School"],
            "Westmoreland": ["North Sumner Elementary", "Westmoreland Elementary", "Westmoreland Middle", "Westmoreland High School"],
            "Bethpage": ["Bethpage Elementary"],
            "Goodlettsville": ["Madison Creek Elementary"],
            "Millersville": ["Millersville Elementary"],
            "Cottontown": ["Oakmont Elementary"]
        }

        schools = schools_by_town.get(selected_town, [])

        self.school_var.set("Select School")
        self.school_menu['menu'].delete(0, 'end')

        for school in schools:
            self.school_menu['menu'].add_command(label=school, command=lambda s=school: self.select_school(s))

        # Update the selected town without adding to the log
        if selected_town != "Select Town":
            self.town_var.set(selected_town)
