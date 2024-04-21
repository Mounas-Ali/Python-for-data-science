def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ calcul bmi """
    if len(height) != len(weight):
        print("Error: list should have the same length")
        return []

    bmi_values = []
    for h, w in zip(height, weight):
        if not (isinstance(h, int) or isinstance(h, float)) and not (isinstance(w, int) or isinstance(w, float)):
            print("Error: Should be int or float")
            return []
        if h == 0 or w == 0:
            print("Error: can't be 0")
            return []

        bmi = w/(h*h)
        bmi_values.append(bmi)

    return bmi_values

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ if bigger than the limit = true else false """
    bmi_values = []
    for i in bmi:
        if not (isinstance(i, int) or isinstance(i, float)):
            print("Error: Should be int or float")
            return []
        if i > limit:
            bmi_values.append(True)
        else:
            bmi_values.append(False)
    return bmi_values
        