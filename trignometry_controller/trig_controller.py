import math
def calc_trig_function(payload):



    fun = payload["function"]
    measurement = payload["measurement"]
    value = payload["value_of_theta"]
    if fun == "sin":
        if measurement == "in_degree":
            result = math.sin(value)

        elif measurement == "radian":
            value = (math.radians(180 / math.pi))
            result = math.sin(value)


        else:
            result = "invalid_measurement"

    elif fun == "cos":
        if measurement == "in_degree":
            result = math.cos(value)

        elif measurement == "radian":
            value = (math.radians(180 / math.pi))
            result = math.cos(value)

        else:
            result = "invalid_measurement"

    elif fun == "tan":
        if measurement == "in_degree":
            result = math.tan(value)
        elif measurement == "radian":
            value = (math.radians(180 / math.pi))
            result = math.tan(value)
        else:
            result = "invalid_measurement"

    elif fun == "cosec":
        if measurement == "in_degree":
            result = 1 / math.sin(value)
        elif measurement == "radian":
            value = (math.radians(180 / math.pi))
            result = 1 / math.sin(value)
        else:
            result = "invalid_measurement"

    elif fun == "sec":
        if measurement == "in_degree":
            result = 1 / math.cos(value)
        elif measurement == "radian":
            value = (math.radians(180 / math.pi))
            result = 1 / math.cos(value)

        else:
            result = "invalid_measurement"

    elif fun == "cot":
        if measurement == "in_degree":
            result = 1 / math.tan(value)
        elif measurement == "radian":
            value = (math.radians(180 / math.pi))
            result = 1 / math.tan(value)
        else:
            result = "invalid_measurement"
    return result