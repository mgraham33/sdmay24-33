import random


def generate(data):
    data["correct_answers"]["timer1"] = ""
    data["correct_answers"]["timer2"] = ""
    data["correct_answers"]["timer3"] = ""
    data["correct_answers"]["timer4"] = ""
    data["correct_answers"]["timer5"] = ""
    data["correct_answers"]["timer6"] = ""
    
def grade(data):
    oneShotAnswered = False
    periodicAnswered = False
    rtcAnswered = False
    edgeCountAnswered = False
    edgeTimeAnswered = False
    pwmModeAnswered = False
    
    for i in range(1, 7):
        forString = "timer" + str(i)
        if data["submitted_answers"][forString] == "One-shot" and oneShotAnswered == False:
            data["partial_scores"][forString]["score"] = .1
            data["score"] = 1
            oneShotAnswered = True
        elif data["submitted_answers"][forString] == "Periodic" and periodicAnswered == False:
            data["partial_scores"][forString]["score"] = .1
            data["score"] = 1
            periodicAnswered = True
        elif data["submitted_answers"][forString] == "RTC" and rtcAnswered == False:
            data["partial_scores"][forString]["score"] = .1
            data["score"] = 1
            rtcAnswered = True
        elif data["submitted_answers"][forString] == "Edge Count" and edgeCountAnswered == False:
            data["partial_scores"][forString]["score"] = .1
            data["score"] = 1
            edgeCountAnswered = True
        elif data["submitted_answers"][forString] == "Edge Time" and edgeTimeAnswered == False:
            data["partial_scores"][forString]["score"] = .1
            data["score"] = 1
            edgeTimeAnswered = True
        elif data["submitted_answers"][forString] == "PWM" and pwmModeAnswered == False:
            data["partial_scores"][forString]["score"] = .1
            data["score"] = 1
            pwmModeAnswered = True