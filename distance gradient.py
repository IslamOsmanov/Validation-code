def calculate_delta_altitude(descent_gradient_percent, distance_nm, prev_altitude_ft=16827):
  if descent_gradient_percent is None or distance_nm is None:
    return None, None

  altitude_change_nm = (descent_gradient_percent * distance_nm) / 100
  altitude_change_ft = altitude_change_nm * 6076.12

  start_altitude_ft = prev_altitude_ft + altitude_change_ft
  delta_altitude_ft = altitude_change_ft

  return start_altitude_ft, delta_altitude_ft

if __name__ == "__main__":
  while True:
    try:
      descent_gradient = float(input("Enter the descent gradient in percent: "))
      distance = float(input("Enter the distance in nautical miles: "))
      break
    except ValueError:
      print("Please enter numeric values.")

  prev_altitude = 16827

  start_altitude, delta_altitude = calculate_delta_altitude(descent_gradient, distance, prev_altitude)

  if start_altitude is not None and delta_altitude is not None:
    print(f"Descent Gradient: {descent_gradient}%")
    print(f"Distance: {distance} nautical miles")
  
    print(f"start Altitude: {start_altitude:.2f} feet")
  
  else:
    print("Invalid input.")