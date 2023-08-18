# GCode Speed conversion
# Adjusts for the gantry speed decrease on the curves
#

#F10 (10mm/s) is the standard line speed
LinSpeed = "F10\n"
#F75 (75mm/s) is the standard Arc speed
ArcSpeed = "F75\n"

# Reading File INPUT GCODE FILE HERE
file1 = open('sketch_w_offset_3_DXF_Relativepos.gcode', 'r')
Lines = file1.readlines()

output_Lines = []
# Checks lines for large linear (>0 before decimal) moves and does speed adjustment
for line in Lines:
    if len(line) > 6:
        if int(line[line.find('.')-1])>0  or int(line[line.find('.',10)-1])>0:
            #Write to lines
            output_Lines.append(LinSpeed + line + ArcSpeed)
        else: output_Lines.append(line)
    else: output_Lines.append(line)
    

# writing saved lines to file
file1 = open('adjusted_speed_output.gcode', 'w')
for line in output_Lines:
    file1.write(line)




