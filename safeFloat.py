def safeFloat(x):
    try:
         return float(x)
    except ValueError:
        return 0.0
