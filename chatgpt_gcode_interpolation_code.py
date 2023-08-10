## ChatGPT Written code
import re

def interpolate_circular_gcode(gcode_lines, segments_per_circle=100):
    new_gcode = []
    for line in gcode_lines:
        # Regular expression to find G1 commands with X, Y, and optionally Z coordinates
        linear_command = re.match(r'^G1\s+X([-+]?\d*\.?\d+)\s+Y([-+]?\d*\.?\d+)(?:\s+Z([-+]?\d*\.?\d+))?', line)
        if linear_command:
            x_start, y_start, z_start = map(float, linear_command.groups())
            new_gcode.append(line)
            if z_start is not None:
                new_z_command = f'Z{z_start}'
            else:
                new_z_command = ''

            for i in range(1, segments_per_circle + 1):
                angle = 2 * i * 3.141592653589793 / segments_per_circle
                x_end = x_start + (x_start - x_start * 1.05) * 0.5 * (1 - cos(angle))
                y_end = y_start + (y_start - y_start * 1.05) * 0.5 * (1 - cos(angle))
                new_gcode.append(f'G1 X{x_end} Y{y_end} {new_z_command}')
        else:
            new_gcode.append(line)

    return new_gcode

def read_gcode_file(file_path):
    with open(file_path, "r") as file:
        gcode_lines = file.readlines()
    return gcode_lines

def save_interpolated_gcode(interpolated_gcode, output_file_path):
    with open(output_file_path, "w") as output_file:
        for line in interpolated_gcode:
            output_file.write(line + "\n")

# Example usage:
input_gcode_file = "C:\Users\co2_ctl\Documents\Timofei\Gcode\sketch_w_offset_3_DXF_Relativepos.gcode"
output_gcode_file = "C:\Users\co2_ctl\Documents\Timofei\Gcode\interpolated_gcode.gcode"
segments_per_circle = 50

gcode_lines = read_gcode_file(input_gcode_file)
interpolated_gcode = interpolate_circular_gcode(gcode_lines, segments_per_circle)
save_interpolated_gcode(interpolated_gcode, output_gcode_file)
