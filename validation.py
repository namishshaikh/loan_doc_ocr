def validate_data(fields):
    validated = {}
    for key, value in fields.items():
        if value:
            validated[key] = "Valid"
        else:
            validated[key] = "Missing"
    return validated