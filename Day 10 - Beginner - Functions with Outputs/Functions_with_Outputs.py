def format_name(f_name, l_name):
    """Take a first name e last name and capitalize the first letter"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("bRuNo", "danieL")
print(formated_string)
