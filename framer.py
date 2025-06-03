def framer():

    try:
        import turtle
    except ImportError:
        print("Oops! The 'turtle' module is missing. Make sure you're running a standard Python 3 installation.")
        exit(1)

    print("\n         _________________________\n        |   ___________________   |\n        |  |                   |  |\n        |  |                   |  |\n        |  |     WELCOME TO    |  |\n        |  |       FRAMER!     |  |\n        |  |                   |  |\n        |  |___________________|  |\n        |_________________________|\n\n")
    print("Please enter all dimensions in inches (using decimals for fractions)...\n")

#Built in 1/16" framing tolerance
    #Set 0 to turn off
    frame_tolerance = 0.0625

# Ask for Input Values
    art_w = art_h = mat_overlap = mat_side = mat_top = mat_bottom = frame_width = rabbet_w = None

# Use a while loop to collect inputs until all are valid
    while True:
        try:
            art_w = float(input("Art width: "))
            break
        except ValueError:
            print("\nInvalid input for art width...\n")

    while True:
        try:
            art_h = float(input("Art height: "))
            break
        except ValueError:
            print("\nInvalid input for art height...\n")

    while True:
        try:
            mat_overlap = float(input("Mat Overlap (How much the mat will overlap the art on each side -- min. 0.125 inch suggested): "))
            break
        except ValueError:
            print("\nInvalid input for mat overlap...\n")

    while True:
        try:
            mat_side = float(input("Desired Mat Width for Sides: "))
            break
        except ValueError:
            print("\nInvalid input for side mat width...\n")

    while True:
        try:
            mat_top = float(input("Desired Mat Width for Top: "))
            break
        except ValueError:
            print("\nInvalid input for top mat width...\n")

    while True:
        try:
            mat_bottom = float(input("Desired Mat Width for Bottom: "))
            break
        except ValueError:
            print("\nInvalid input for bottom mat width...\n")

    while True:
        try:
            frame_width = float(input("Frame Width: "))
            break
        except ValueError:
            print("\nInvalid input for frame width...\n")

    while True:
        try:
            rabbet_w = float(input("Rabbet Width (how much the frame overlaps the mat -- min. 0.25 inch suggested): "))
            if rabbet_w + frame_tolerance >= frame_width:
                print("\nRabbet width is too wide for the desired frame width...\n")
                continue
            break
        except ValueError:
            print("\nInvalid input for rabbet width...\n")


# calculate frame measurements
    inner_frame_w = art_w - (mat_overlap*2) + (mat_side*2)
    inner_frame_h = art_h - (mat_overlap*2) + mat_top + mat_bottom 
    outer_frame_w = inner_frame_w + (frame_width*2)
    outer_frame_h = inner_frame_h + (frame_width*2)

# calculate mat measurements
    inner_mat_w = art_w - (mat_overlap*2)
    inner_mat_h = art_h - (mat_overlap*2)
    outer_mat_w = inner_mat_w + (mat_side*2) + (rabbet_w*2)
    outer_mat_h = inner_mat_h + mat_top + mat_bottom + (rabbet_w*2)

    print("\n########## Input Measurements ############ \n")
    print(f"Art Measurements: {art_w} W x {art_h} H")
    print("Mat Overlap:", mat_overlap)
    print("Mat Side Showing:", mat_side)
    print("Mat Top Showing:", mat_top)
    print("Mat Bottom showing:", mat_bottom)
    print("Frame Width:", frame_width)
    print("Rabbet Width:", rabbet_w)

    print("\n########## Mat Measurements ############ \n")
    print("Inner Mat:",inner_mat_w,"W x",inner_mat_h,"H")
    print("Outer Mat:",outer_mat_w,"W x",outer_mat_h,"H")

    print("\n########## Frame Measurements ############ \n")
    print("Inner Frame:",inner_frame_w,"W x",inner_frame_h,"H")
    print("Outer Frame:",outer_frame_w,"W x",outer_frame_h,"H")
    print("Rabbet Depth (with tolerance):",(float(rabbet_w) + frame_tolerance))
    print("\n")

#set scale factor
    if outer_frame_h >= outer_frame_w:
        n = 500/outer_frame_h
    if outer_frame_h < outer_frame_w:
        n = 600/outer_frame_w
    
#set window scaling
    if outer_frame_h >= outer_frame_w:
        win_w = outer_frame_w*n + 400
    if outer_frame_h < outer_frame_w:
        win_w = 1000

#alignment variable
    x_align = (win_w/6) - n*(frame_width + mat_side - mat_overlap)
    y_align = 225 - n*(frame_width + mat_bottom - mat_overlap)

    print(f"Scaling Factor Calculated: {n}\n")

# ****** Drawing *******
#set up canvas
    turtle.setup(width=(win_w), height=(1000), startx=0, starty=0)
#screen colour
    #screen = turtle.Screen()
    #screen.bgcolor("black")
#setting up turtle
    t = turtle.Turtle()
#title
    t.screen.title(f"Framed Art {outer_frame_w} x {outer_frame_h}")
#speed
    t.speed("fast")
#shape
    #t.shape("circle")
#colour
    #t.color("red")
 #line width
    t.width(2)
#Written line spacing variable
    s = 18
#Top Writing
    t.penup()
    t.goto(t.pos() + (x_align - ((art_w + outer_frame_w)*n)/2, ((art_h + outer_frame_h)*n)/2 - y_align + 15))
    t.color("black")
    t.write(f'Frame Tolerance: {frame_tolerance}"', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, s))
    t.write(f'Rabbet Width (with tolerance): {(float(rabbet_w) + frame_tolerance)}"', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, s))
    t.write(f'Frame Width: {frame_width}"', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, s))
    t.write(f'Mat Bottom Showing: {mat_bottom}"', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, s))
    t.write(f'Mat Top Showing: {mat_top}"', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, s))
    t.write(f'Mat Side Showing: {mat_side}"', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, s))
    t.write(f'Mat Overlap: {mat_overlap}"', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, s))
    t.write(f'Art Measurements: {art_w}" W x {art_h}" H', move=False, font=('Futura', 14))

#move turtle to start
    t.penup()
    t.home()
    t.goto(t.pos() + (x_align, -y_align))
    t.pendown()

#draw art print
    t.pencolor("gainsboro")
    t.left(90)
    t.forward(art_h*n)
    t.left(90)
    t.forward(art_w*n)
    t.left(90)
    t.forward(art_h*n)
    t.left(90)
    t.forward(art_w*n)
    t.penup()

#draw mat
    t.pencolor("black")
    t.goto( t.pos() + (-mat_overlap*n, mat_overlap*n) )
    t.pendown()
    t.left(90)
    t.forward(inner_mat_h*n)
    t.left(90)
    t.forward(inner_mat_w*n)
    t.left(90)
    t.forward(inner_mat_h*n)
    t.left(90)
    t.forward(inner_mat_w*n)
    t.penup()
    t.pencolor("gainsboro")
    t.goto( t.pos() + ((mat_side + rabbet_w)*n, -n*(mat_bottom + rabbet_w) ))
    t.pendown()
    t.left(90)
    t.forward(outer_mat_h*n)
    t.left(90)
    t.forward(outer_mat_w*n)
    t.left(90)
    t.forward(outer_mat_h*n)
    t.left(90)
    t.forward(outer_mat_w*n)
    t.penup()

#draw frame
    t.pencolor("black")
    t.goto( t.pos() + (-(rabbet_w)*n, (rabbet_w)*n) )
    t.pendown()
    t.left(90)
    t.forward(inner_frame_h*n)
    t.left(90)
    t.forward(inner_frame_w*n)
    t.left(90)
    t.forward(inner_frame_h*n)
    t.left(90)
    t.forward(inner_frame_w*n)
    t.penup()
    t.goto( t.pos() + (frame_width*n, -frame_width*n) )
    t.pendown()
    t.left(90)
    t.forward(outer_frame_h*n)
    t.left(90)
    t.forward(outer_frame_w*n)
    t.left(90)
    t.forward(outer_frame_h*n)
    t.left(90)
    t.forward(outer_frame_w*n)
    t.penup()

    #scale 
    t.goto( t.pos() + ((outer_frame_w*n)/12, 0) )
    t.pendown()
    t.speed("fastest")
    t.left(90)
    #For frames smaller than or equal to 72 inches in height
    if round(outer_frame_h) <= 72:
        t.forward((round(outer_frame_h))*n)
        t.right(90)
        for i in range((round(outer_frame_h)), -1, -1):
        # Foot Markers
            if i%12 == 0:
                t.color("dark red")
                t.forward(33)
                t.penup()
                  #Feet labels
                if i != 0:
                    t.goto(t.pos() + (9, -7))
                    t.write(f'{int(i/12)}ft', move=False, font=('Futura', 12))
                    t.goto(t.pos() + (-9, 7))
                    t.goto(t.pos() + (-33,-n))
                t.pendown()
            else:
            #Inch Markers
                t.color("black")
                #6 Inch Markers
                #if i%6 == 0:
                """t.forward(20)
                t.penup()
                #Toggle inch marker labels
                if outer_frame_h <= 48:
                    t.goto(t.pos() + (7, -6))
                    t.write(f'{int(i)}', move=False, font=('Futura', 10))
                    t.goto(t.pos() + (-7, 6))
                t.goto(t.pos() + (-20,-n))
                t.pendown()"""
                # Other Inch Markers
                t.forward(10)
                t.penup()
                #Toggle inch marker labels
                if 24 <= outer_frame_h <= 48:
                    t.goto(t.pos() + (7, -5))
                    t.write(f'{int(i)}', move=False, font=('Futura', 8))
                    t.goto(t.pos() + (-7, 5))
                if 12 <= outer_frame_h < 24:
                    t.goto(t.pos() + (7, -7))
                    t.write(f'{int(i)}"', move=False, font=('Futura', 10))
                    t.goto(t.pos() + (-7, 7))
                if outer_frame_h < 12:
                    t.goto(t.pos() + (7, -9))
                    t.write(f'{int(i)}"', move=False, font=('Futura', 14))
                    t.goto(t.pos() + (-7, 9))
                t.goto(t.pos() + (-10,-n))
                t.pendown()
    #For frames larger than 72 inches in height (no inch markers)
    if round(outer_frame_h) > 72 and round(outer_frame_h) <= 400:
        t.forward((round((outer_frame_h//12)))*12*n)
        t.right(90)
        #Feet Markers
        for i in range((round(outer_frame_h//12)), -1, -1):
            t.color("dark red")
            t.forward(30)
            t.penup()
            #Feet Labels
            if i != 0:
                t.goto(t.pos() + (9, -7))
                t.write(f'{int(i)}ft', move=False, font=('Futura', 12))
                t.goto(t.pos() + (-9, 7))
                t.goto(t.pos() + (-30,-(12*n)))
            t.pendown()
    #For gigantinornous art
    if round(outer_frame_h) > 400:
        t.penup()
        t.goto(t.pos() + (30, 0))

    #Bottom writing
    t.penup()
    t.goto(t.pos() + (-((outer_frame_w*n)+(outer_frame_w*n)/12+33), -35))
    t.color("black")
    t.write('Mat Measurements', move=False, font=('Futura', 16))
    t.goto(t.pos() + (0, -1.5*s))
    t.write(f'Inner Mat: {inner_mat_w}" W x {inner_mat_h}" H', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, -s))
    t.write(f'Outer Mat: {outer_mat_w}" W x {outer_mat_h}" H', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, -2*s))
    t.write('Frame Measurements', move=False, font=('Futura', 16))
    t.goto(t.pos() + (0, -1.5*s))
    t.write(f'Inner Frame: {inner_frame_w}" W x {inner_frame_h}" H', move=False, font=('Futura', 14))
    t.goto(t.pos() + (0, -s))
    t.write(f'Outer Frame: {outer_frame_w}" W x {outer_frame_h}" H', move=False, font=('Futura', 14))
    if round(outer_frame_h) > 400:
        t.goto(t.pos() + (0, -2*s))
        t.write('Big art for a big heart <3. You broke the side scale', move=False, font=('Futura', 16))
    t.goto(t.pos() + (0, -2*s))
    t.write('Close this window before re-running Framer', move=False, font=('Futura', 16))

    turtle.done()

if __name__ == "__main__":
    framer()