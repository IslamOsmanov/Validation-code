def ias_to_tas(ias_kt, altitude_ft, var_celsius=0):
    altitude_meters = altitude_ft * 0.3048
    tas = ias_kt * (171233 * ((288 + var_celsius) - 0.006496 * altitude_meters)**0.5) / ((288 - 0.006496 * altitude_meters)**2.628)
    return round(tas)

if __name__ == "__main__":
    try:
        ias = float(input("Enter IAS "))
        altitude = float(input("Enter Altitude "))
        var = float(input("Enter Var ") or 0)

        tas_result = float(ias_to_tas(ias, altitude, var))
        print(f"TAS = {tas_result} kt")

    except ValueError:
        print("Mistake")