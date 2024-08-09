import numpy as np
import matplotlib.pyplot as plt

def pid_controller(Kp, Ki, Kd, error, previous_error, integral):
  """Implements a PID controller.

  Args:
    Kp: Proportional gain
    Ki: Integral gain
    Kd: Derivative gain
    error: Current error
    previous_error: Previous error
    integral: Accumulated error

  Returns:
    Control output
  """

  proportional = Kp * error
  integral += Ki * error
  derivative = Kd * (error - previous_error)
  output = proportional + integral + derivative
  return output, integral

def simulate_system(setpoint, initial_value, Kp, Ki, Kd, time_step, simulation_time):
  """Simulates a simple first-order system with PID control.

  Args:
    setpoint: Desired value
    initial_value: Initial value of the system
    Kp: Proportional gain
    Ki: Integral gain
    Kd: Derivative gain
    time_step: Simulation time step
    simulation_time: Total simulation time

  Returns:
    Time array, output values, and error values
  """

  time = np.arange(0, simulation_time, time_step)
  output = []
  error = []
  integral = 0
  previous_error = 0

  for t in time:
    process_value = output[-1] if len(output) > 0 else initial_value
    error.append(setpoint - process_value)
    output_value, integral = pid_controller(Kp, Ki, Kd, error[-1], previous_error, integral)
    output.append(output_value)
    previous_error = error[-1]

  return time, output, error

def main():
  setpoint = float(input("Enter setpoint: "))
  initial_value = float(input("Enter initial value: "))
  Kp = float(input("Enter proportional gain (Kp): "))
  Ki = float(input("Enter integral gain (Ki): "))
  Kd = float(input("Enter derivative gain (Kd): "))
  time_step = float(input("Enter time step: "))
  simulation_time = float(input("Enter simulation time: "))

  time, output, error = simulate_system(setpoint, initial_value, Kp, Ki, Kd, time_step, simulation_time)

  plt.plot(time, output, label="Output")
  plt.plot(time, [setpoint] * len(time), label="Setpoint")
  plt.xlabel("Time")
  plt.ylabel("Value")
  plt.legend()
  plt.show()

if __name__ == "__main__":
  main()
