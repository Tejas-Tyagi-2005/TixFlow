def map_output(category):
    if category == "Billing / Payment":
        return "Finance Team", "High"
    elif category == "Technical Issue":
        return "Tech Team", "Medium"
    elif category == "Service Complaint":
        return "Support Team", "Medium"
    else:
        return "General Team", "Low"