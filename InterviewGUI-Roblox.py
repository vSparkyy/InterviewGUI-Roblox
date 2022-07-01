import pyautogui as pg
import PySimpleGUI as sg

finalstring = ["/e"]
conc1 = []
kick = [":kick"]
ending_msg = "Okay, this concludes the interview. Thank you for attending and good luck in the future."

questions = {
    "Question 1" : "1) Explain why you're here to become a Professor.",
    "Question 2" : "2) Do you understand the duties of a Professor? If so, explain them.",
    "Question 3" : "3) If you see a staff member giving people invalid warnings, how would you handle the situation?",
    "Question 4" : "4) A student is running around classrooms and continuously talking. What is the correct way to handle this?",
    "Question 5" : "5) If a student is killing inside of a safe zone/just outside of the safe zone, what would you do?",
    "Question 6" : "6) Explain why we should choose you over other candidates?",
    "Question 7" : "7) Do you have any past experience? This could be anything from a Roblox group, volunteering etc. If not, please say “I have no past experience.”",
    "Question 8" : "8) Do you have any questions before this interview concludes?",
}

rules = {
    "Greeting" : "Hello there! My name is Sparky and I will be your interviewer for today. If you have any questions at all please dont hesitate to ask but remember to use PTS as it is currently in effect.",
    "Grammar rule" : "Please note that grammar is crucial in this interview and you must be proficient when typing your responses back to me.",
    "GS" : "You will have 3 Grammar Strikes each (GS), once you reach 3 grammar strikes you will automatically fail.",
    "Detail rule" : "When being asked the questions, please answer in as much detail as you can within 1-3 sentences unless the question doesn't require particular attention.",
    "Time limit" : "You will have exactly 3 minutes to answer each question, if you fail to respond within this time, you will be kicked for the assumption of being AFK. ",
    "Plagiarism" : "Please do not copy paste any answers as that is plagiarism and if you are caught doing so, you will automatically fail. ",
}

kicktemp = {
    "Grammar Strikes" : "Thank you for attending this session. Unfortunately, you reached 3 Grammar strikes, better luck next time!",
    "Copy paste" : "Unfortunately, it has been deemed that you were plagiarising by using copy/paste or other methods. Please do not do this in the future.",
    "Time limit" : "AFK ~ Gone over 3 minute time limit.",
    "Passed kick (Safechat)" : "Congratulations, you passed the interview! You will be ranked within a day", 
    "Failed kick (Safechat)" : "Unfortunately, you failed the interview. Better luck next time!", 
    "End of interview kick (No Safechat)" : "Thank you for attending. The results will be posted on dizzycourd at the end of the interview."
}


def create_window(theme):
    sg.theme(theme)
    secondarytab_layout = [[sg.Text("Greeting edit: "), sg.Multiline(key = 'change_g', size = (50,5)), sg.Button("Edit greeting"), sg.Button("Reset Greet")],
                           [sg.Text("Ending edit: "), sg.Multiline(key = 'change_e', size = (50,5)), sg.Button("Edit ending"), sg.Button("Reset End")],
                           [sg.Text("Theme edit: "), sg.Listbox(values = sg.theme_list(), size = (20, 5), key = "theme", enable_events = True), sg.Button("Edit theme")]]

    maintab_layout = [[sg.Text("Sparky's Interview Helper", font = 'Arial 20')],
            [sg.Text("Team name: "), sg.Input(key = 'team'), sg.Button('Confirm')],
            [sg.Checkbox("/e enabled?", default = True, key = "/e", enable_events = True), sg.Checkbox("Autocopy", key = "copy", enable_events = True), sg.Text("USAGE: Click on the output box when clicking question / rule button", visible = False, key = 'usage')],
            [sg.Multiline("Notepad", size = (50,10))],
            [sg.Text("Intro", font = 'Arial 16'), sg.Text("Disclaimer: If updating teamname or /e usage please click button twice")],
            [sg.Button("Greeting"), sg.Button("Grammar rule"), sg.Button("GS", size = (6))],
            [sg.Button("Detail rule"), sg.Button("Time limit"), sg.Button("Plagiarism")],
            [sg.Text("Questions", font = 'Arial 16')],
            [sg.Button("Question 1"), sg.Button("Question 2"), sg.Button("Question 3"), sg.Button("Question 4")],
            [sg.Button("Question 5"), sg.Button("Question 6"), sg.Button("Question 7"), sg.Button("Question 8")],
            [sg.Text("Output", font = "Arial 16")],
            [sg.Multiline("Concatenated Text:", size = (50,5), key = 'concat')],
            [sg.Text("End", font = 'Arial 16')],
            [sg.Button("Ending message", size = (15))],
            [sg.Text("Kick message template:"), sg.Combo(["No reason", "Grammar Strikes", "Copy paste", "Time limit", "Passed kick (Safechat)", "Failed kick (Safechat)", "End of interview kick (No Safechat)"], readonly = True, key = 'reason'), sg.Text("Username for kick"), sg.Input(key ='user'), sg.Button("OK")],
            [sg.Text("Kick user message: "), sg.Input("Generate kick message", key = 'kickmsg', expand_x = True)]]

    layout = [[sg.TabGroup(
            [[sg.Tab('Main', maintab_layout), sg.Tab('Config', secondarytab_layout)]]
            )]]

    return sg.Window("Interview Helper", layout, finalize = True)

window = create_window('Dark Amber')

def checks():
    global finalstring, conc1
    teamvalue = values["team"]
    if conc1 != []:
        finalstring.append("".join(conc1))
        print(finalstring)
        window["concat"].update("Concatenated Text:")
        window["concat"].update(" ".join(finalstring))
        if values['copy'] == True:
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
        finalstring = ["/e"]
        finalstring.append(("%"+teamvalue) if teamvalue is not None else None)


while True:
    event, values = window.read()
    if event is None:
        break
    if event == "Edit greeting":
        rules['Greeting'] = values['change_g']
    if event == "Edit ending":
        ending_msg = values['change_e']
    if event == "Reset Greet":
        rules['Greeting'] = "Hello there! My name is Sparky and I will be your interviewer for today. If you have any questions at all please dont hesitate to ask but remember to use PTS as it is currently in effect."
        window['change_g'].update("")
    if event == "Reset End":
        ending_msg = "Okay, this concludes the interview. Thank you for attending and good luck in the future."
        window['change_e'].update("")
    if event == "Edit theme":
        window.close()
        window = create_window("".join(values['theme']))
    if event ==  "Confirm":
        finalstring.append("%"+values['team'])
        #window["concat"].update(" ".join(finalstring))
    if values['copy'] == True:
        window['usage'].update(visible = True)
    if values['copy'] == False:
        window['usage'].update(visible = False)
    if values['/e'] == True:
        if "/e" not in finalstring:
            finalstring.insert(0, "/e")
            #window["concat"].update(" ".join(finalstring))
    elif values['/e'] == False and "/e" in finalstring:
        finalstring.pop(0)
        #window["concat"].update(" ".join(finalstring))
    if event in questions:
        conc1.clear()
        if values['/e'] == False:
            finalstring.insert(0,":pm")
        elif values['/e'] == True:
            finalstring.insert(1,":pm")
        conc1.append(questions[event])
        checks()
    if event in rules:
        conc1.clear()
        finalstring.clear()
        conc1.append(rules[event])
        checks()
    if event == "Ending message":
        if values['copy'] == True:
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
        window["concat"].update(ending_msg)
    if event == "OK":
        kick = [":kick"]
        while kick == [":kick"]:
            if values['/e'] == True and "/e" not in kick:
                kick.insert(0, "/e")
            kick.append(values['user'])
            kick.append(kicktemp[values['reason']])
            window['kickmsg'].update(" ".join(kick))
            if values['copy'] == True:
                pg.hotkey('ctrl', 'a')
                pg.hotkey('ctrl', 'c')
        
window.close()
