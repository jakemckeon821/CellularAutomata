def rule110(arr):
  next_arr = [0] * len(arr)
  for i in range(len(arr)):
      left = arr[i - 1] if i > 0 else 0
      center = arr[i]
      right = arr[i + 1] if i < len(arr) - 1 else 0
      next_arr[i] = (left ^ center) or (center ^ right)
  return next_arr

while True:
  try:
      user_input = input("Enter 10 binary numbers (0 or 1) separated by spaces: ")
      initial_config = list(map(int, user_input.split()))
      if len(initial_config) == 10 and all(num in (0, 1) for num in initial_config):
          break
      else:
          print("Invalid input. Please enter exactly 10 binary numbers (0 or 1).")
  except ValueError:
      print("Invalid input. Please enter numbers only.")

current_config = initial_config[:]
for t in range(10):
  print("Instance",t, ":", current_config)
  current_config = rule110(current_config)
