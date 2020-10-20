"""
File: my_drawing.py
Name: Fangching Su
----------------------
Chibi Maruko Chan considers attending SC101.
"""
# import Class from file
from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Using GOval, GRect, GLine, GPolygon and GLabel draws Chibi Maruko Chan.
    """
    # setup window size and title
    window = GWindow(width=1000, height=600, title="Chibi Maruko Chan")
    # setup background color
    bg = GRect(1000, 600, x=0, y=0)
    bg.filled = "lightskyblue"
    bg.fill_color = "lightskyblue"
    window.add(bg)
    # draw hair part
    hair = GOval(450, 550, x=150, y=50)
    hair.filled = True
    hair.fill_color = "black"
    hair_remove = GRect(450, 275, x=150, y=345)
    hair_remove.filled = True
    hair_remove.fill_color = "lightskyblue"
    hair_remove.color = "lightskyblue"
    window.add(hair)
    window.add(hair_remove)
    # draw face part
    face_1 = GRect(350, 100, x=200, y=250)
    face_1.filled = True
    face_1.fill_color = "bisque"
    face_1.color = "bisque"
    face_circle_1 = GOval(100, 100, x=315, y=160)
    face_circle_1.filled = True
    face_circle_1.fill_color = "bisque"
    face_circle_1.color = "bisque"
    face_circle_2 = GOval(350, 150, x=200, y=280)
    face_circle_2.filled = True
    face_circle_2.fill_color = "bisque"
    face_circle_2.color = "bisque"
    window.add(face_1)
    window.add(face_circle_1)
    window.add(face_circle_2)
    # draw hair part
    hair_r = GRect(50, 30, x=350, y=150)
    hair_r.filled = True
    hair_r.fill_color = "black"
    window.add(hair_r)
    # draw face part
    face_2 = GPolygon()
    face_2.add_vertex((200, 250))
    face_2.add_vertex((215, 200))
    face_2.add_vertex((230, 250))
    window.add(face_2)
    face_2.filled = True
    face_2.fill_color = "bisque"
    face_2.fill_color = "bisque"
    face_2.color = "bisque"
    face_3 = GPolygon()
    face_3.add_vertex((220, 220))
    face_3.add_vertex((245, 160))
    face_3.add_vertex((270, 200))
    window.add(face_3)
    face_3.filled = True
    face_3.fill_color = "bisque"
    face_3.fill_color = "bisque"
    face_3.color = "bisque"
    face_4 = GPolygon()
    face_4.add_vertex((250, 200))
    face_4.add_vertex((290, 140))
    face_4.add_vertex((322, 188))
    window.add(face_4)
    face_4.filled = True
    face_4.fill_color = "bisque"
    face_4.fill_color = "bisque"
    face_4.color = "bisque"
    face_5 = GPolygon()
    face_5.add_vertex((320, 185))
    face_5.add_vertex((350, 135))
    face_5.add_vertex((380, 180))
    window.add(face_5)
    face_5.filled = True
    face_5.fill_color = "bisque"
    face_5.fill_color = "bisque"
    face_5.color = "bisque"
    face_6 = GPolygon()
    face_6.add_vertex((378, 185))
    face_6.add_vertex((408, 138))
    face_6.add_vertex((448, 203))
    window.add(face_6)
    face_6.filled = True
    face_6.fill_color = "bisque"
    face_6.fill_color = "bisque"
    face_6.color = "bisque"
    face_7 = GPolygon()
    face_7.add_vertex((435, 185))
    face_7.add_vertex((465, 145))
    face_7.add_vertex((485, 190))
    window.add(face_7)
    face_7.filled = True
    face_7.fill_color = "bisque"
    face_7.fill_color = "bisque"
    face_7.color = "bisque"
    face_8 = GPolygon()
    face_8.add_vertex((480, 190))
    face_8.add_vertex((500, 160))
    face_8.add_vertex((525, 230))
    window.add(face_8)
    face_8.filled = True
    face_8.fill_color = "bisque"
    face_8.fill_color = "bisque"
    face_8.color = "bisque"
    face_9 = GPolygon()
    face_9.add_vertex((490, 245))
    face_9.add_vertex((532, 190))
    face_9.add_vertex((550, 250))
    window.add(face_9)
    face_9.filled = True
    face_9.fill_color = "bisque"
    face_9.fill_color = "bisque"
    face_9.color = "bisque"
    # draw eye brow part
    for i in range(4):
        eye_brow_1 = GOval(130, 100, x=220, y=180 + i)
        eye_brow_1.filled = True
        eye_brow_1.fill_color = "bisque"
        window.add(eye_brow_1)
    for i in range(4):
        eye_brow_2 = GOval(130, 100, x=395, y=180 + i)
        eye_brow_2.filled = True
        eye_brow_2.fill_color = "bisque"
        window.add(eye_brow_2)
    eye_brow_remove_1 = GRect(140, 80, x=220, y=220)
    eye_brow_remove_1.filled = True
    eye_brow_remove_1.fill_color = "bisque"
    eye_brow_remove_1.color = "bisque"
    eye_brow_remove_2 = GRect(140, 80, x=395, y=220)
    eye_brow_remove_2.filled = True
    eye_brow_remove_2.fill_color = "bisque"
    eye_brow_remove_2.color = "bisque"
    window.add(eye_brow_remove_1)
    window.add(eye_brow_remove_2)
    # draw ear part
    ear_1 = GOval(30, 50, x=180, y=260)
    ear_1.filled = True
    ear_1.fill_color = "bisque"
    ear_1.color = "bisque"
    ear_2 = GOval(30, 50, x=540, y=260)
    ear_2.filled = True
    ear_2.fill_color = "bisque"
    ear_2.color = "bisque"
    window.add(ear_1)
    window.add(ear_2)
    # draw eye part
    eye_1 = GOval(35, 35, x=280, y=230)
    eye_1.filled = True
    eye_1.fill_color = "black"
    eye_2 = GOval(35, 35, x=435, y=230)
    eye_2.filled = True
    eye_2.fill_color = "black"
    window.add(eye_1)
    window.add(eye_2)
    # draw blush part
    blush_1 = GOval(35, 35, x=235, y=340)
    blush_1.filled = True
    blush_1.fill_color = "salmon"
    blush_1.color = "salmon"
    blush_2 = GOval(35, 35, x=475, y=340)
    blush_2.filled = True
    blush_2.fill_color = "salmon"
    blush_2.color = "salmon"
    window.add(blush_1)
    window.add(blush_2)
    # draw mouth part
    mouth = GOval(60, 80, x=345, y=330)
    mouth.filled = True
    mouth.fill_color = "palevioletred"
    mouth.color = "palevioletred"
    window.add(mouth)
    # draw shirt part
    shirt_1 = GOval(400, 300, x=175, y=430)
    shirt_1.filled = True
    shirt_1.fill_color = "gold"
    shirt_1.color = "gold"
    window.add(shirt_1)
    shirt_2 = GRect(25, 155, x=260, y=445)
    shirt_2.filled = True
    shirt_2.fill_color = "firebrick"
    shirt_2.color = "firebrick"
    shirt_3 = GRect(25, 155, x=465, y=445)
    shirt_3.filled = True
    shirt_3.fill_color = "firebrick"
    shirt_3.color = "firebrick"
    window.add(shirt_2)
    window.add(shirt_3)
    # draw neck part
    neck = GOval(50, 30, x=350, y=420)
    neck.filled = True
    neck.fill_color = "bisque"
    neck.color = "bisque"
    window.add(neck)
    # draw sleeve part
    sleeve_1 = GLine(240, 530, 235, 600)
    sleeve_1.color = "black"
    sleeve_2 = GLine(510, 530, 515, 600)
    sleeve_2.color = "black"
    window.add(sleeve_1)
    window.add(sleeve_2)
    # draw sign part
    circle_1 = GOval(100, 100, x=50, y=470)
    circle_1.filled = True
    circle_1.fill_color = "white"
    circle_1.color = "white"
    circle_2 = GOval(100, 100, x=600, y=470)
    circle_2.filled = True
    circle_2.fill_color = "white"
    circle_2.color = "white"
    window.add(circle_1)
    window.add(circle_2)
    # draw stick part
    stick_1 = GRect(20, 50, x=90, y=550)
    stick_1.filled = True
    stick_1.fill_color = "white"
    stick_1.color = "white"
    stick_2 = GRect(20, 50, x=640, y=550)
    stick_2.filled = True
    stick_2.fill_color = "white"
    stick_2.color = "white"
    window.add(stick_1)
    window.add(stick_2)
    # draw yes part
    yes = GOval(80, 80, x=60, y=480)
    yes.filled = True
    yes.fill_color = "red"
    yes.color = "red"
    window.add(yes)
    s_yes = GOval(60, 60, x=70, y=490)
    s_yes.filled = True
    s_yes.fill_color = "white"
    s_yes.color = "white"
    window.add(s_yes)
    # draw no part
    for i in range(15):
        cross_1 = GLine(615 + i, 490, 670 + i, 550)
        cross_1.color = "blue"
        cross_2 = GLine(670 + i, 490, 615 + i, 550)
        cross_2.color = "blue"
        window.add(cross_1)
        window.add(cross_2)
    # draw cloud part
    cloud_1 = GOval(150, 135, x=650, y=80)
    cloud_1.filled = True
    cloud_1.fill_color = "white"
    cloud_1.color = "white"
    cloud_2 = GOval(100, 80, x=700, y=50)
    cloud_2.filled = True
    cloud_2.fill_color = "white"
    cloud_2.color = "white"
    cloud_3 = GOval(100, 80, x=700, y=160)
    cloud_3.filled = True
    cloud_3.fill_color = "white"
    cloud_3.color = "white"
    cloud_4 = GOval(100, 90, x=780, y=45)
    cloud_4.filled = True
    cloud_4.fill_color = "white"
    cloud_4.color = "white"
    cloud_5 = GOval(100, 90, x=780, y=160)
    cloud_5.filled = True
    cloud_5.fill_color = "white"
    cloud_5.color = "white"
    cloud_6 = GOval(150, 135, x=790, y=80)
    cloud_6.filled = True
    cloud_6.fill_color = "white"
    cloud_6.color = "white"
    cloud_7 = GOval(80, 30, x=700, y=260)
    cloud_7.filled = True
    cloud_7.fill_color = "white"
    cloud_7.color = "white"
    cloud_8 = GOval(50, 23, x=655, y=295)
    cloud_8.filled = True
    cloud_8.fill_color = "white"
    cloud_8.color = "white"
    cloud_9 = GOval(25, 15, x=620, y=320)
    cloud_9.filled = True
    cloud_9.fill_color = "white"
    cloud_9.color = "white"
    window.add(cloud_1)
    window.add(cloud_2)
    window.add(cloud_3)
    window.add(cloud_4)
    window.add(cloud_5)
    window.add(cloud_6)
    window.add(cloud_7)
    window.add(cloud_8)
    window.add(cloud_9)
    # draw label part
    label_1 = GLabel("Attend", x=700, y=140)
    label_1.font = "-50"
    label_2 = GLabel("SC101?", x=725, y=200)
    label_2.font = "-50"
    window.add(label_1)
    window.add(label_2)
    # draw logo part
    stancode = GLabel("#stanCode", x=750, y=550)
    stancode.font = "Courier-40-italic"
    stancode.color = "white"
    window.add(stancode)

    # grid line
    # for i in range(1000):
    #     if i % 50 == 0:
    #         line = GLine(i, 0, i, 600)
    #         line.filled = True
    #         line.color = "orange"
    #         window.add(line)
    #
    # for i in range(600):
    #     if i % 50 == 0:
    #         line = GLine(0, i, 1000, i)
    #         line.filled = True
    #         line.color = "green"
    #         window.add(line)


if __name__ == '__main__':
    main()
