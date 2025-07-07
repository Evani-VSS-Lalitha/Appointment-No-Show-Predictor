def suggest_intervention(prob):
    if prob > 0.85:
        return "Call + SMS + Reschedule Option"
    elif prob > 0.7:
        return "SMS Reminder + Cab Offer"
    elif prob > 0.6:
        return "SMS Reminder"
    else:
        return "No intervention"
