def create_array(path):
    with open(path, "r") as file:
            lines = []
            file.readline()
            height_line=file.readline().strip()
            height=height_line.split(" ")[1]
            width_line=file.readline().strip()
            width=width_line.split(" ")[1]
            file.readline()
            for l in file:
                line = l.strip()
                #print(line) 
                lines.append(line)
    return lines
        
