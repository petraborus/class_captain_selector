'''
This program allows the user to enter candidates and have a vote to determine a winner
'''


from guizero import App, Text, Box, PushButton, ButtonGroup, TextBox, Window, ListBox, Picture

# if any of the text boxes are empty --> popup to say that a field is empty and needs to be filled
# a guide to what indexes different candidate information are with the example of candidate 1 (list referring to candidates_info_list)
# candidate 1 name = list[0][1][0]
# candidate 1 goals = list[0][1][2]
# candidate 1 reasons = list[0][1][3]
# candidate 1 votes = list[0][2]
# '1' = list[0][0]

number_of_candidates = 0
candidates_info_list = [[1], [2], [3], [4]]
candidate_hidden_names_list = []
total_votes = 0
candidates_votes_list = []

app = App(title="Captain Selector App", bg="#f1ab86", width=935, height=680)
enter_candidate_window = None
view_candidate_window = None
start_voting_window = None
voting_results_window = None

name_textbox = None
age_textbox = None
goals_textbox = None
reason_of_choice_textbox = None
bottom_margin_enter = None
candidate_to_view_choice = None
candidate_info_box = None
goals_textbox_space = None
reasons_textbox_space = None
number_of_votes_value = None


def check_enough_candidates():
    global number_of_candidates
    if number_of_candidates < 2:
        app.info("Can't Proceed", "There aren't enough candidates to start voting.")
    else:
        start_voting()


def no_candidates_to_view():
    global number_of_candidates
    if number_of_candidates == 0:
        app.info("Can't Proceed", "There are no candidates in the system to view.")
    else:
        view_candidate()


# warning to the user that information may be lost when closing the window
def exit_window1():
    global enter_candidate_window
    if enter_candidate_window.yesno("Warning", "Are you sure you want to go to menu? If save wasn't clicked candidate info will be lost"):
        enter_candidate_window.destroy()
        app.show()


def exit_window2():
    global view_candidate_window
    if view_candidate_window.yesno("Warning", "Are you sure you want to go to menu?"):
        view_candidate_window.destroy()
        app.show()


def exit_window3():
    global start_voting_window
    if start_voting_window.yesno("Warning", "Are you sure you want to go to menu? Votes will be lost if voting isn't finished."):
        start_voting_window.destroy()
        app.show()


def close_final_window():
    global voting_results_window, number_of_candidates, candidates_info_list, candidate_hidden_names_list, total_votes
    voting_results_window.destroy()
    app.show()
    number_of_candidates = 0
    candidates_info_list = [[1], [2], [3], [4]]
    candidate_hidden_names_list = []
    total_votes = 0
    number_of_candidates_value.value = "     " + str(number_of_candidates) + "    "
    candidate_names_box.clear()
    app.update()


def save_candidate_info():
    global name_textbox, candidate_hidden_names_list, candidates_info_list, enter_candidate_window, bottom_margin_enter, number_of_candidates, age_textbox, goals_textbox, reason_of_choice_textbox, candidate_hidden_names_list, candidate_names_box
    # also make sure no more than four candidates can be entered
    if number_of_candidates >= 4:
        enter_candidate_window.warn("too many candidates", "There are already 4 candidates. You can't enter more.")
    # can't proceed unless text boxes are filled out
    elif name_textbox.value == "":
        enter_candidate_window.warn("empty", "One or more fields are empty. Please fill out before saving.")
    elif age_textbox.value == "":
        enter_candidate_window.warn("empty", "One or more fields are empty. Please fill out before saving.")
    elif goals_textbox.value == "":
        enter_candidate_window.warn("empty", "One or more fields are empty. Please fill out before saving.")
    elif reason_of_choice_textbox.value == "":
        enter_candidate_window.warn("empty", "One or more fields are empty. Please fill out before saving.")
    else:
        if number_of_candidates == 0:
            #adds info from text boxes to the list
            candidates_info_list[0].append([name_textbox.value, age_textbox.value, goals_textbox.value, reason_of_choice_textbox.value])
            candidates_info_list[0].append(0)
            candidate_hidden_names_list.append("Candidate 1")
            names_spacer1 = Text(candidate_names_box, text="", size=6)
            name1 = Text(candidate_names_box, text=str(candidates_info_list[0][1][0]), font="PT Sans", size=15)
            app.update()
        elif number_of_candidates == 1:
            candidates_info_list[1].append([name_textbox.value, age_textbox.value, goals_textbox.value, reason_of_choice_textbox.value])
            candidates_info_list[1].append(0)
            candidate_hidden_names_list.append("Candidate 2")
            names_spacer2 = Text(candidate_names_box, text="", size=6)
            name2 = Text(candidate_names_box, text=str(candidates_info_list[1][1][0]), font="PT Sans", size=15)
            app.update()
        elif number_of_candidates == 2:
            candidates_info_list[2].append([name_textbox.value, age_textbox.value, goals_textbox.value, reason_of_choice_textbox.value])
            candidates_info_list[2].append(0)
            candidate_hidden_names_list.append("Candidate 3")
            names_spacer3 = Text(candidate_names_box, text="", size=6)
            name3 = Text(candidate_names_box, text=str(candidates_info_list[2][1][0]), font="PT Sans", size=15)
            app.update()
        elif number_of_candidates == 3:
            candidates_info_list[3].append([name_textbox.value, age_textbox.value, goals_textbox.value, reason_of_choice_textbox.value])
            candidates_info_list[3].append(0)
            candidate_hidden_names_list.append("Candidate 4")
            names_spacer4 = Text(candidate_names_box, text="", size=6)
            name4 = Text(candidate_names_box, text=str(candidates_info_list[3][1][0]), font="PT Sans", size=15)
            app.update()

        name_textbox.clear()
        age_textbox.clear()
        goals_textbox.clear()
        reason_of_choice_textbox.clear()

        number_of_candidates += 1
        number_of_candidates_value.value = "     " + str(number_of_candidates) + "    "
        successful_save_message = Text(bottom_margin_enter, text="Information successfully saved.", font="PT Sans", size="16", align="right")

    app.update()


def enter_candidate():
    global enter_candidate_window, name_textbox, bottom_margin_enter, age_textbox, goals_textbox, reason_of_choice_textbox, number_of_candidates
    app.hide()

    # basic layout
    enter_candidate_window = Window(app, title="Enter Candidate", bg="#f1ab86", width=935, height=680)
    side_margin_space = Box(enter_candidate_window, width=19, height="fill", align="left")
    ec_title_box = Box(enter_candidate_window, width="fill", height=60, align="top")
    ec_subtitle_box = Box(enter_candidate_window, width="fill", height=22, align="top")
    ec_title = Text(ec_title_box, text="Enter Candidate", size="38", font="Titan One", align="left")
    ec_subtitle = Text(ec_subtitle_box, text="Fill all questions and click save.", size="20", font="PT Sans", align="left")

    # ensures that no more than 4 candidates can be entered --> success criteria
    if number_of_candidates > 4:
        enter_candidate_window.warn("too many candidates", "There are already 4 candidates. You can't enter more.")
    else:
        bottom_margin_enter = Box(enter_candidate_window, width="fill", height="44", align="bottom")
        enter_info_box = Box(enter_candidate_window, width=317, height=520, align="left")
        middle_margin = Box(enter_candidate_window, width=112, height="fill", align="left")
        other_info_box = Box(enter_candidate_window, width=400, height="fill", align="left")
        candidate_age_name_box = Box(enter_info_box, height=201, width="fill", align="top")
        heading_box = Box(candidate_age_name_box, height=39, width="fill", align="top")
        info_details_heading = Text(heading_box, text="INFORMATION TO FILL:", size="20", font="PT Sans", align="left")

        # Setting up containers for the different questions and their text boxes
        name_box = Box(candidate_age_name_box, height=45, width="fill", align="top")
        name_box_text = Text(name_box, text="Candidate name:  ", align="left", font="PT Sans", size="17")
        name_textbox = TextBox(name_box, width=161, height=27, align="left")
        age_box = Box(candidate_age_name_box, height=45, width="fill", align="top")
        age_box_text = Text(age_box, text="Candidate age:     ", align="left", font="PT Sans", size="17")
        age_textbox = TextBox(age_box, width=161, height=27, align="left")
        spacer_text1 = Text(candidate_age_name_box, text="", align="top", font="PT Sans", size="28")
        goals_heading = Text(candidate_age_name_box, text="Main goals: ", align="left", font="PT Sans", size="17")
        candidate_goals_box = Box(enter_info_box, width="fill", height="fill", align="top")
        goals_textbox = TextBox(candidate_goals_box, height=8, width="fill", align="top", multiline=True)
        spacer_text2 = Text(candidate_goals_box, text="", align="top", font="PT Sans", size="18")
        reason_of_choice_heading = Text(candidate_goals_box, text="Why they think they should be chosen:", align="top", font="PT Sans", size="17")
        spacer_text3 = Text(candidate_goals_box, text="", align="top", font="PT Sans", size="18")
        reason_of_choice_textbox = TextBox(candidate_goals_box, height=8, width="fill", align="top", multiline=True)

        # note to say that candidates will be anonymised
        notes_heading_box = Box(other_info_box, height=38, width="fill", align="top")
        notes_heading_box.bg = "#d28b69"
        notes_heading = Text(notes_heading_box, text=" Note that...", font="PT Sans", size=17, align="left")
        notes_box = Box(other_info_box, height=167, width="fill", align="top")
        notes_box.bg = "white"
        note_spacer = Text(notes_box, text="", align="top")
        note = Text(notes_box, text="The candidate names will only be displayed at the end.", align="top", font="PT Sans")
        note_pt2 = Text(notes_box, text="Before the results, candidates will be anonymised using 'Candidate 1' etc.", font="PT Sans")

        info_sb1 = Box(other_info_box, height=98, width="fill", align="top")

        # saving information when button is pressed
        save_button_box = Box(other_info_box, height=51, width="fill", align="top")
        save_button = PushButton(save_button_box, height="fill", width=20, align="left", text="SAVE", command=save_candidate_info)
        info_sb2 = Box(other_info_box, height=76, width="fill", align="top")

        # button to close down window etc.
        menu_button_box = Box(other_info_box, height=51, width="fill", align="top")
        menu_button = PushButton(menu_button_box, height="fill", width=20, align="left", text="Return to MENU")
        menu_button.when_clicked = exit_window1
        enter_candidate_window.when_closed = exit_window1


def view_candidate():
    global candidate_to_view_choice, candidate_info_box, view_candidate_window, goals_textbox_space, reasons_textbox_space, candidate_hidden_names_list
    app.hide()

    # basic layout
    view_candidate_window = Window(app, title="View Candidates", bg="#f1ab86", width=935, height=680)
    side_margin_space = Box(view_candidate_window, width=19, height="fill", align="left")
    vc_title_box = Box(view_candidate_window, width="fill", height=60, align="top")
    vc_subtitle_box = Box(view_candidate_window, width="fill", height=22, align="top")
    vc_title = Text(vc_title_box, text="View Candidates", size="38", font="Titan One", align="left")
    vc_subtitle = Text(vc_subtitle_box, text="Select which candidate you would like to view", size="20", font="PT Sans", align="left")
    bottom_margin = Box(view_candidate_window, width="fill", height=214, align="bottom")
    select_candidate_box = Box(view_candidate_window, width=317, height="fill", align="left")
    middle_margin = Box(view_candidate_window, width=122, height="fill", align="left")
    show_info_box = Box(view_candidate_window, width=432, height="fill", align="left")
    candidate_selection_box = Box(select_candidate_box, height="fill", width="fill", align="top")
    selection_heading_box = Box(candidate_selection_box, height=42, width="fill", align="top")
    info_heading_box = Box(show_info_box, height=42, width="fill", align="top")
    spacer_text_selection = Text(candidate_selection_box, text="")

    # the user can select which candidate they want to view
    selection_heading = Text(selection_heading_box, text="SELECT OPTION:", size="20", font="PT Sans", align="left")
    candidate_to_view_choice = ButtonGroup(candidate_selection_box, options=candidate_hidden_names_list, width="fill", height="fill", command=candidate_details)

    # text boxes for the different information
    show_info_heading = Text(info_heading_box, text="CANDIDATE INFORMATION:", align="left", font="PT Sans", size="20")
    candidate_info_box = Box(show_info_box, width="fill", height=310, align="top")
    candidate_info_box.bg = "#d28b69"
    goals_box = Box(candidate_info_box, width="fill", height=141)
    reason_to_be_chosen_box = Box(candidate_info_box, width="fill", height="fill")
    goals_heading_box = Box(goals_box, width="fill", height=38, align="top")
    goals_heading = Text(goals_heading_box, text="  Main Goal:", font="PT Sans", size="17", align="left")
    goals_info_box = Box(goals_box, width="fill", height="fill", align="top")
    goals_textbox_space = TextBox(goals_info_box, width=54, height=6, multiline=True)
    reasons_heading_box = Box(reason_to_be_chosen_box, width="fill", height=38, align="top")
    reasons_heading = Text(reasons_heading_box, text="  Reason why they think they should be chosen:", font="PT Sans", size="17", align="left")
    reasons_info_box = Box(reason_to_be_chosen_box, width="fill", height="fill", align="top")
    reasons_textbox_space = TextBox(reasons_info_box, width=54, height=6, multiline=True)
    spacer_box = Box(candidate_selection_box, height=12, width="fill", align="top")

    # button to close window etc.
    menu_button = PushButton(candidate_selection_box, text="Return to MENU", height=3, width="fill", align="top")
    menu_button.when_clicked = exit_window2
    view_candidate_window.when_closed = exit_window2


def candidate_details():
    global candidate_to_view_choice, candidate_info_box, candidates_info_list, view_candidate_window, goals_textbox_space, reasons_textbox_space

    # text boxes disabled so that the user can't edit the information in it
    goals_textbox_space.disable()
    reasons_textbox_space.disable()

    # information needed are retrieved from the information list and displayed in the text boxes when the candidate option is selected
    if candidate_to_view_choice.value == "Candidate 1":
        goals_textbox_space.value = candidates_info_list[0][1][2]
        reasons_textbox_space.value = candidates_info_list[0][1][3]
        view_candidate_window.update()
    elif candidate_to_view_choice.value == "Candidate 2":
        goals_textbox_space.value = candidates_info_list[1][1][2]
        reasons_textbox_space.value = candidates_info_list[1][1][3]
        view_candidate_window.update()
    elif candidate_to_view_choice.value == "Candidate 3":
        goals_textbox_space.value = candidates_info_list[2][1][2]
        reasons_textbox_space.value = candidates_info_list[2][1][3]
        view_candidate_window.update()
    elif candidate_to_view_choice.value == "Candidate 4":
        goals_textbox_space.value = candidates_info_list[3][1][2]
        reasons_textbox_space.value = candidates_info_list[3][1][3]
        view_candidate_window.update()


def start_voting():
    global start_voting_window, candidates_info_list, number_of_candidates, total_votes, number_of_votes_value
    app.hide()

    # main layout for the window
    start_voting_window = Window(app, title="Candidate Voting", bg="#f1ab86", width=935, height=680)
    side_margin_space = Box(start_voting_window, width=19, height="fill", align="left")
    sv_title_box = Box(start_voting_window, width="fill", height=60, align="top")
    sv_subtitle_box = Box(start_voting_window, width="fill", height=26, align="top")
    sv_title = Text(sv_title_box, text="Candidate Voting", size="38", font="Titan One", align="left")
    sv_subtitle = Text(sv_subtitle_box, text="Choose which candidate you would like to vote for by clicking on the corresponding button", size="20", font="PT Sans", align="left")
    voting_options_box = Box(start_voting_window, width=353, height="fill", align="left")
    middle_margin = Box(start_voting_window, width=63, height="fill", align="left")
    extra_info_box = Box(start_voting_window, width=432, height="fill", align="left")
    right_margin_voting_box = Box(start_voting_window, width="fill", height="fill", align="left")
    options_given_heading_box = Box(voting_options_box, height=43, width="fill", align="top")
    options_heading = Text(options_given_heading_box, text="OPTIONS AND THEIR MAIN GOALS:", size="20", font="PT Sans", align="left")

    # box to show the candidate names
    candidate_names_heading_box = Box(extra_info_box, height=39, width="fill", align="top")
    names_heading = Text(candidate_names_heading_box, text="CANDIDATE NAMES:", size="20", font="PT Sans", align="left")
    candidate_names_display_box = Box(extra_info_box, align="top", width="fill", height=225)
    candidate_names_display_box.bg = "#d28b69"
    note = Text(candidate_names_display_box, text="Note that the order of names doesn't correspond to the numbered candidates.", font="PT Sans", align="top")
    space1 = Text(candidate_names_display_box, text="", size="6")
    name1 = Text(candidate_names_display_box, text=str(candidates_info_list[1][1][0]), font="PT Sans")
    space2 = Text(candidate_names_display_box, text="", size="6")
    name2 = Text(candidate_names_display_box, text=str(candidates_info_list[0][1][0]), font="PT Sans")
    if number_of_candidates == 3:
        space3 = Text(candidate_names_display_box, text="", size="6")
        name3 = Text(candidate_names_display_box, text=str(candidates_info_list[2][1][0]), font="PT Sans")
    elif number_of_candidates == 4:
        space3 = Text(candidate_names_display_box, text="", size="6")
        name3 = Text(candidate_names_display_box, text=str(candidates_info_list[3][1][0]), font="PT Sans")
        space4 = Text(candidate_names_display_box, text="", size="6")
        name4 = Text(candidate_names_display_box, text=str(candidates_info_list[2][1][0]), font="PT Sans")
    spacer = Box(extra_info_box, height=47, width="fill", align="top")

    # heading and boxes needed to show the number of votes, which is a gv and updates each time there is a new vote
    number_of_votes_heading_box = Box(extra_info_box, height=26, width="fill", align="top")
    number_of_votes_heading = Text(number_of_votes_heading_box, text="NUMBER OF VOTES CAST:", align="left", font="PT Sans", size=20)
    votes_space = Box(extra_info_box, width="fill", height=22, align="top")
    number_of_votes_box = Box(master=extra_info_box, height=50, width=60, align="top")
    number_of_votes_box.bg = "#9cafb7"
    number_of_votes_value = Text(number_of_votes_box, text="    " + str(total_votes) + "    ", font="PT Sans", size="18")
    votes_space2 = Box(extra_info_box, height=40, width="fill", align="top")

    # buttons for each candidate which then triggers a yes no pop up plus further action within the function
    buttons_box = Box(extra_info_box, height=51, align="top", width="fill")
    candidate1_button = PushButton(voting_options_box, width="fill", height=2, align="top", text="Candidate 1")
    c1_show_goals = Box(voting_options_box, align="top", height=73, width="fill")
    c1_spacer = Box(c1_show_goals, width="fill", height=20, align="top")
    c1_goals_text = Text(c1_show_goals, text="1 - " + str(candidates_info_list[0][1][2]), font="PT Sans", size=15, align="left")
    candidate1_button.when_clicked = make_sure1

    candidate2_button = PushButton(voting_options_box, width="fill", height=2, align="top", text="Candidate 2")
    c2_show_goals = Box(voting_options_box, align="top", height=73, width="fill")
    c2_spacer = Box(c2_show_goals, width="fill", height=20, align="top")
    c2_goals_text = Text(c2_show_goals, text="2 - " + str(candidates_info_list[1][1][2]), font="PT Sans", size=15, align="left")
    candidate2_button.when_clicked = make_sure2

    # if statements used as there should only be buttons for candidates 3 and 4 if there are that many candidates
    if number_of_candidates >= 3:
        candidate3_button = PushButton(voting_options_box, width="fill", height=2, align="top", text="Candidate 3")
        c3_show_goals = Box(voting_options_box, align="top", height=73, width="fill")
        c3_spacer = Box(c3_show_goals, width="fill", height=20, align="top")
        c3_goals_text = Text(c3_show_goals, text="3 - " + str(candidates_info_list[2][1][2]), font="PT Sans", size=15, align="left")
        candidate3_button.when_clicked = make_sure3
    if number_of_candidates == 4:
        candidate4_button = PushButton(voting_options_box, width="fill", height=2, align="top", text="Candidate 4")
        c4_show_goals = Box(voting_options_box, align="top", height=73, width="fill")
        c4_spacer = Box(c4_show_goals, width="fill", height=20, align="top")
        c4_goals_text = Text(c4_show_goals, text="4 - " + str(candidates_info_list[3][1][2]), font="PT Sans", size=15, align="left")
        candidate4_button.when_clicked = make_sure4
    start_voting_window.update()

    # menu button and closing the window lead to a function that ensures that the user wants to leave it, end voting buttons moves on to results function
    end_voting_button = PushButton(buttons_box, width=13, height="fill", align="left", text="END VOTING")
    menu_button = PushButton(buttons_box, width=13, height="fill", align="right", text="RETURN TO MENU")
    menu_button.when_clicked = exit_window3
    end_voting_button.when_clicked = voting_results
    start_voting_window.when_closed = exit_window3


# take second element for sort
def take_second(elem):
    return elem[1]


def voting_results():
    global start_voting_window, candidates_info_list, number_of_candidates, voting_results_window, candidates_votes_list
    start_voting_window.destroy()

    # basic layout
    voting_results_window = Window(app, title="Candidate Voting", bg="#f1ab86", width=935, height=680)
    side_margin_space = Box(voting_results_window, width=19, height="fill", align="left")
    vr_title_box = Box(voting_results_window, width="fill", height=60, align="top")
    vr_subtitle_box = Box(voting_results_window, width="fill", height=26, align="top")
    vr_title = Text(vr_title_box, text="Voting Results", size="38", font="Titan One", align="left")
    vr_subtitle = Text(vr_subtitle_box, text="Number of votes each candidate received and the winner", size="20", font="PT Sans", align="left")
    sb1 = Box(voting_results_window, width="fill", height=25, align="top")
    names_and_votes_box = Box(voting_results_window, width="fill", height=136, align="top")
    sb2 = Box(voting_results_window, width="fill", height=60, align="top")
    winner_text_box = Box(voting_results_window, width="fill", height=40, align="top")

    if number_of_candidates == 2:
        candidates_votes_list.append([candidates_info_list[0][1][0], candidates_info_list[0][2]])
        candidates_votes_list.append([candidates_info_list[1][1][0], candidates_info_list[1][2]])
        candidates_votes_list.sort(key=take_second, reverse=True)
        candidate_results = ListBox(names_and_votes_box, items=[str(candidates_votes_list[0][0]) + " - " + str(candidates_votes_list[0][1]), str(candidates_votes_list[1][0]) + " - " + str(candidates_votes_list[1][1])])
        if candidates_votes_list[0][1] > candidates_votes_list[1][1]:
            winner_text = Text(winner_text_box, text="NEW CLASS CAPTAIN: " + str(candidates_votes_list[0][0]), font="PT Sans", size=24)
        else:
            winner_text = Text(winner_text_box, text="NO OVERALL WINNER", font="PT Sans", size=24)
    elif number_of_candidates == 3:
        candidates_votes_list.append([candidates_info_list[0][1][0], candidates_info_list[0][2]])
        candidates_votes_list.append([candidates_info_list[1][1][0], candidates_info_list[1][2]])
        candidates_votes_list.append([candidates_info_list[2][1][0], candidates_info_list[2][2]])
        candidates_votes_list.sort(key=take_second, reverse=True)
        candidate_results = ListBox(names_and_votes_box, items=[str(candidates_votes_list[0][0]) + " - " + str(candidates_votes_list[0][1]), str(candidates_votes_list[1][0]) + " - " + str(candidates_votes_list[1][1]), str(candidates_votes_list[2][0]) + " - " + str(candidates_votes_list[2][1])])
        if candidates_votes_list[0][1] > candidates_votes_list[1][1]:
            winner_text = Text(winner_text_box, text="NEW CLASS CAPTAIN: " + str(candidates_votes_list[0][0]), font="PT Sans", size=24)
        else:
            winner_text = Text(winner_text_box, text="NO OVERALL WINNER", font="PT Sans", size=24)
    elif number_of_candidates == 4:
        candidates_votes_list.append([candidates_info_list[0][1][0], candidates_info_list[0][2]])
        candidates_votes_list.append([candidates_info_list[1][1][0], candidates_info_list[1][2]])
        candidates_votes_list.append([candidates_info_list[2][1][0], candidates_info_list[2][2]])
        candidates_votes_list.append([candidates_info_list[3][1][0], candidates_info_list[3][2]])
        candidates_votes_list.sort(key=take_second, reverse=True)
        candidate_results = ListBox(names_and_votes_box, items=[str(candidates_votes_list[0][0]) + " - " + str(candidates_votes_list[0][1]), str(candidates_votes_list[1][0]) + " - " + str(candidates_votes_list[1][1]), str(candidates_votes_list[2][0]) + " - " + str(candidates_votes_list[2][1]), str(candidates_votes_list[3][0]) + " - " + str(candidates_votes_list[3][1])])
        if candidates_votes_list[0][1] > candidates_votes_list[1][1]:
            winner_text = Text(winner_text_box, text="NEW CLASS CAPTAIN: " + str(candidates_votes_list[0][0]), font="PT Sans", size=24)
        else:
            winner_text = Text(winner_text_box, text="NO OVERALL WINNER", font="PT Sans", size=24)

    '''
    # results put in a list box depending on descending order + winner/no overall winner texts displayed if it's a tie or not
    if number_of_candidates == 2:
        if candidates_info_list[0][2] > candidates_info_list[1][2]:
            candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2]), str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2])])
            winner_text = Text(winner_text_box, text="NEW CLASS CAPTAIN: " + str(candidates_info_list[0][1][0]), font="PT Sans", size=24)
        elif candidates_info_list[1][2] > candidates_info_list[0][2]:
            candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2]), str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2])])
            winner_text = Text(winner_text_box, text="NEW CLASS CAPTAIN: " + str(candidates_info_list[1][1][0]), font="PT Sans", size=24)
        elif candidates_info_list[1][2] == candidates_info_list[0][2]:
            candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2]), str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2])])
            winner_text = Text(winner_text_box, text="NO OVERALL WINNER", font="PT Sans", size=24)
    elif number_of_candidates == 3:
        if candidates_info_list[0][2] > candidates_info_list[1][2] and candidates_info_list[0][2] > candidates_info_list[2][2]:
            if candidates_info_list[1][2] >= candidates_info_list[2][2]:
                candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2]), str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2]), str(candidates_info_list[2][1][0]) + " - " + str(candidates_info_list[2][2])])
            elif candidates_info_list[1][2] < candidates_info_list[2][2]:
                candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2]), str(candidates_info_list[2][1][0]) + " - " + str(candidates_info_list[2][2]), str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2])])
            winner_text = Text(winner_text_box, text="NEW CLASS CAPTAIN: " + str(candidates_info_list[0][1][0]), font="PT Sans", size=24)
        elif candidates_info_list[1][2] > candidates_info_list[0][2] and candidates_info_list[1][2] > candidates_info_list[2][2]:
            if candidates_info_list[0][2] >= candidates_info_list[2][2]:
                candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2]), str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2]), str(candidates_info_list[2][1][0]) + " - " + str(candidates_info_list[2][2])])
            elif candidates_info_list[2][2] < candidates_info_list[0][2]:
                candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2]), str(candidates_info_list[2][1][0]) + " - " + str(candidates_info_list[2][2]), str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2])])
            winner_text = Text(winner_text_box, text="NEW CLASS CAPTAIN: " + str(candidates_info_list[1][1][0]), font="PT Sans", size=24)
        elif candidates_info_list[2][2] > candidates_info_list[0][2] and candidates_info_list[2][2] > candidates_info_list[1][2]:
            if candidates_info_list[0][2] >= candidates_info_list[1][2]:
                candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[2][1][0]) + " - " + str(candidates_info_list[2][2]), str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2]), str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2])])
            elif candidates_info_list[2][2] < candidates_info_list[0][2]:
                candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[2][1][0]) + " - " + str(candidates_info_list[2][2]), str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2]), str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2])])
            winner_text = Text(winner_text_box, text="NEW CLASS CAPTAIN: " + str(candidates_info_list[2][1][0]), font="PT Sans", size=24)
        elif candidates_info_list[2][2] > candidates_info_list[0][2] and candidates_info_list[2][2] == candidates_info_list[1][2]:
            candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[2][1][0]) + " - " + str(candidates_info_list[2][2]), str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2]), str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2])])
            winner_text = Text(winner_text_box, text="NO OVERALL WINNER", font="PT Sans", size=24)
        elif candidates_info_list[1][2] > candidates_info_list[2][2] and candidates_info_list[1][2] == candidates_info_list[0][2]:
            candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2]), str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2]), str(candidates_info_list[2][1][0]) + " - " + str(candidates_info_list[2][2])])
            winner_text = Text(winner_text_box, text="NO OVERALL WINNER", font="PT Sans", size=24)
    elif number_of_candidates == 4:
        candidate_results = ListBox(names_and_votes_box, items=[str(candidates_info_list[0][1][0]) + " - " + str(candidates_info_list[0][2]), str(candidates_info_list[1][1][0]) + " - " + str(candidates_info_list[1][2]), str(candidates_info_list[2][1][0]) + " - " + str(candidates_info_list[2][2]), str(candidates_info_list[3][1][0]) + " - " + str(candidates_info_list[3][2])])
'''

    voting_results_window.when_closed = close_final_window


# these functions just make sure that the user does want to vote for the selected candidate, adding a vote if yes
def make_sure1():
    global total_votes, candidates_info_list, start_voting_window, number_of_votes_value
    if total_votes < 30:
        if start_voting_window.yesno("make sure", "Are you sure that you want to vote for candidate 1?"):
            total_votes += 1
            candidates_info_list[0][2] += 1
            number_of_votes_value.value = "     " + str(total_votes) + "    "
            start_voting_window.update()
    else:
        start_voting_window.warn("too many votes", "You can't have more than 30 votes. Please proceed to voting results.")


def make_sure2():
    global total_votes, candidates_info_list, start_voting_window, number_of_votes_value
    if total_votes < 30:
        if start_voting_window.yesno("make sure", "Are you sure that you want to vote for candidate 2?"):
            total_votes += 1
            candidates_info_list[1][2] += 1
            number_of_votes_value.value = "     " + str(total_votes) + "    "
            start_voting_window.update()
    else:
        start_voting_window.warn("too many votes", "You can't have more than 30 votes. Please proceed to voting results.")


def make_sure3():
    global total_votes, candidates_info_list, start_voting_window, number_of_votes_value
    if total_votes < 30:
        if start_voting_window.yesno("make sure", "Are you sure that you want to vote for candidate 3?"):
            total_votes += 1
            candidates_info_list[2][2] += 1
            number_of_votes_value.value = "     " + str(total_votes) + "    "
            start_voting_window.update()
    else:
        start_voting_window.warn("too many votes", "You can't have more than 30 votes. Please proceed to voting results.")


def make_sure4():
    global total_votes, candidates_info_list, start_voting_window, number_of_votes_value
    if total_votes < 30:
        if start_voting_window.yesno("make sure", "Are you sure that you want to vote for candidate 4?"):
            total_votes += 1
            candidates_info_list[3][2] += 1
            number_of_votes_value.value = "     " + str(total_votes) + "    "
            start_voting_window.update()
    else:
        start_voting_window.warn("too many votes", "You can't have more than 30 votes. Please proceed to voting results.")


# layout for menu
title_box = Box(app, width="fill", height=247, align="top")
lowest_box = Box(app, width="fill", height=70, align="bottom")
bottom_box = Box(app, width="fill", height="fill", align="bottom")

left_image_box = Box(title_box, height="fill", width=179, align="left")
left_sb = Box(left_image_box, width="fill", height=83, align="top")
right_image_box = Box(title_box, height="fill", width=179, align="right")
right_sb = Box(right_image_box, width="fill", height=83, align="top")
title_text_box = Box(title_box, height="fill", width="fill")

title_space = Text(master=title_text_box, text="", size="40")
title_pt1 = Text(master=title_text_box, text="Classroom Captain", size="56", font="Titan One")
title_pt2 = Text(master=title_text_box, text="Voting", size="56", font="Titan One")
left_picture = Picture(left_image_box, image="school.gif", align="top")
right_picture = Picture(right_image_box, image="school.gif", align="top")

left_margin_box = Box(master=bottom_box, height="fill", width=68, align="left")
options_box = Box(master=bottom_box, height="fill", width=365, align="left")
options_heading_box = Box(master=options_box, height=38, width="fill", align="top")
options_heading_box.bg = "#d28b69"
options_heading_text = Text(master=options_heading_box, text=" Select Option:", font="PT Sans", size="17", align="left")
options_buttons_box = Box(master=options_box, height="fill", width="fill", align="bottom")
options_buttons_box.bg = "white"
options_sb1 = Box(options_buttons_box, height="33", width="fill")
enter_candidate_button = PushButton(options_buttons_box, height=2, width=20, text="Enter Candidate")
enter_candidate_button.when_clicked = enter_candidate
options_sb2 = Box(options_buttons_box, height="40", width="fill")
view_or_edit_button = PushButton(options_buttons_box, height=2, width=20, text="View Candidates")
view_or_edit_button.when_clicked = no_candidates_to_view
options_sb3 = Box(options_buttons_box, height="40", width="fill")
start_voting_button = PushButton(options_buttons_box, height=2, width=20, text="Start Voting")
start_voting_button.when_clicked = check_enough_candidates
middle_margin_box = Box(master=bottom_box, height="fill", width=116, align="left")
candidates_box = Box(master=bottom_box, height="fill", width=314, align="left")
# adding the number of candidates
number_heading_box = Box(master=candidates_box, height=38, width="fill", align="top")
number_heading_box.bg = "#d28b69"
number_heading_text = Text(master=number_heading_box, text=" Current Number of Candidates:", font="PT Sans", size="17", align="left")
number_value_box = Box(master=candidates_box, height="100", width="fill", align="top")
number_value_box.bg = "white"
number_sb1 = Box(master=number_value_box, height="25")
number_background_box = Box(master=number_value_box, height="50", width="60")
number_background_box.bg = "#9cafb7"
number_text_spacer = Text(number_background_box, text="", size="6")
number_of_candidates_value = Text(number_background_box, text="    " + str(number_of_candidates) + "    ", font="PT Sans", size="18")
number_text_spacer = Text(number_background_box, text="", size="6")
number_sb2 = Box(master=number_value_box, height="25")
divider_margin_box = Box(master=candidates_box, height="28", width="fill", align="top")
divider_margin_box.bg = "#f1ab86"

candidate_heading_box = Box(master=candidates_box, height=38, width="fill", align="top")
candidate_heading_box.bg = "#d28b69"
candidate_heading_text = Text(master=candidate_heading_box, text=" Candidate Names:", font="PT Sans", size="17", align="left")
candidate_names_box = Box(master=candidates_box, height="fill", width="fill", align="top")
candidate_names_box.bg = "white"


right_margin_box = Box(master=bottom_box, height="fill", width="fill", align="left")
right_margin_box.bg = "#f1ab86"

app.display()


