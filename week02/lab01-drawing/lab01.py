import turtle

def main():
    filename = input("Please input filename: ")
    t = turtle.Turtle()
    screen = t.getscreen()
    # Had to use the absolute file path for my computer to access my text file
    #realFileName = r"C:\Users\crazz\OneDrive - Indiana University\Documents\(current) IU Spring 2022\(CSCI-A) Big Data\Labs\Lab1" + "\\" + filename
    file = open(filename, "r")
    for line in file:
        text = line.strip()
        commandList = text.split(", ")
        command = commandList[0]
        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file:", command)
    file.close()
    t.ht() #hide turtle
    screen.exitonclick()
    print("Program Execution Completed")

if __name__ == "__main__":
    main()