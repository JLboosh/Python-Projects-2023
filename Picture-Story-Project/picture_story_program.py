# May 22 2024

from graphics import*
import winsound
import time
import random

# set function to draw all the parking slots and labels around it
def parking_slots(winOne):
    slot_color = color_rgb(0,0,0)
    outline = color_rgb(255, 255, 0)
    label_color = color_rgb(128, 128, 128)
    num_color = color_rgb(255, 255, 255)

    slot_1 = Rectangle(Point(498, 46), Point(591, 114))
    slot_1.setFill(slot_color)
    slot_1.setOutline(outline)
    slot_1.draw(winOne)
    
    label_1 = Rectangle(Point(469, 9) ,Point(627, 23))
    label_1.setFill(label_color)
    label_1.setOutline(label_color)
    label_1.draw(winOne)

    name_1 = Text(Point(547, 17), "Millennium Falcon")
    name_1.setSize(8)
    name_1.draw(winOne)

    num_slot1 = Rectangle(Point(597, 68) ,Point(627, 93))
    num_slot1.setFill(slot_color)
    num_slot1.draw(winOne)

    num_1 = Text(Point(612, 82), "1")
    num_1.setSize(12)
    num_1.setTextColor(num_color)
    num_1.draw(winOne)

    slot_2 = Rectangle(Point(498, 214) ,Point(590, 280))
    slot_2.setFill(slot_color)
    slot_2.setOutline(outline)
    slot_2.draw(winOne)

    label_2 = Rectangle(Point(466, 192) ,Point(624, 204))
    label_2.setFill(label_color)
    label_2.setOutline(label_color)
    label_2.draw(winOne)

    name_2 = Text(Point(545, 198), "The Outrider")
    name_2.setSize(8)
    name_2.draw(winOne)

    num_slot2 = Rectangle(Point(597, 239) ,Point(626, 262))
    num_slot2.setFill(slot_color)
    num_slot2.draw(winOne)

    num_2 = Text(Point(612, 252), "2")
    num_2.setSize(12)
    num_2.setTextColor(num_color)
    num_2.draw(winOne)

    slot_3 = Rectangle(Point(66, 47), Point(131, 88))
    slot_3.setFill(slot_color)
    slot_3.setOutline(outline)
    slot_3.draw(winOne)

    label_3 = Rectangle(Point(20, 14) ,Point(176, 30))
    label_3.setFill(label_color)
    label_3.setOutline(label_color)
    label_3.draw(winOne)

    name_3 = Text(Point(96, 23), "X-wing")
    name_3.setSize(8)
    name_3.draw(winOne)

    num_slot3 = Rectangle(Point(22, 52) ,Point(53, 78))
    num_slot3.setFill(slot_color)
    num_slot3.draw(winOne)

    num_3 = Text(Point(37, 65), "3")
    num_3.setSize(12)
    num_3.setTextColor(num_color)
    num_3.draw(winOne)

    slot_4 = Rectangle(Point(64, 168) ,Point(131, 209))
    slot_4.setFill(slot_color)
    slot_4.setOutline(outline)
    slot_4.draw(winOne)

    label_4 = Rectangle(Point(19, 137) ,Point(176, 152))
    label_4.setFill(label_color)
    label_4.setOutline(label_color)
    label_4.draw(winOne)

    name_4 = Text(Point(96, 146), "TIE Fighters")
    name_4.setSize(8)
    name_4.draw(winOne)

    num_slot4 = Rectangle(Point(23, 179) ,Point(53, 204))
    num_slot4.setFill(slot_color)
    num_slot4.draw(winOne)

    num_4 = Text(Point(38, 191), "4")
    num_4.setSize(12)
    num_4.setTextColor(num_color)
    num_4.draw(winOne)

    slot_5 = Rectangle(Point(65, 288) ,Point(131, 332))
    slot_5.setFill(slot_color)
    slot_5.setOutline(outline)
    slot_5.draw(winOne)

    label_5 = Rectangle(Point(20, 259) ,Point(177, 276))
    label_5.setFill(label_color)
    label_5.setOutline(label_color)
    label_5.draw(winOne)

    name_5 = Text(Point(97, 269), "TIE Bombers")
    name_5.setSize(8)
    name_5.draw(winOne)

    num_slot5 = Rectangle(Point(23, 300) ,Point(53, 325))
    num_slot5.setFill(slot_color)
    num_slot5.draw(winOne)

    num_5 = Text(Point(37, 312), "5")
    num_5.setSize(12)
    num_5.setTextColor(num_color)
    num_5.draw(winOne)

# set function to draw the walls on each end of the window
def draw_walls(winOne):
    wall_color = color_rgb(192, 192, 192)

    wall_1 = Rectangle(Point(630, 0), Point(640, 360))
    wall_1.setFill(wall_color)
    wall_1.draw(winOne)

    wall_2 = Rectangle(Point(0, 0), Point(10, 360))
    wall_2.setFill(wall_color)
    wall_2.draw(winOne)
    
# set function to import an alarm sound affect 
def play_sound(winOne):
    winsound.PlaySound("alarm_sound", winsound.SND_ALIAS)

# set function draw the runway and all the lights beside it
def draw_runway(winOne):
    runway = Rectangle(Point(296, 0) ,Point(342, 360))
    runway.setFill(color_rgb(0, 0, 0))
    runway.setOutline(color_rgb(255, 0, 0))
    runway.draw(winOne)

    radius = 5
    light_color = color_rgb(255, 165, 0)

    y_shift = 36
    light_distance = 45

    for i in range(8):
        light_1 = Circle(Point(291, y_shift), radius)
        light_1.setFill(light_color)
        light_1.draw(winOne)

        light_2 = Circle(Point(347, y_shift), radius)
        light_2.setFill(light_color)
        light_2.draw(winOne)
        
        y_shift += light_distance

    stripes_distance = 90
    for i in range(5):
        stripes = Rectangle(Point(316, 29 + (stripes_distance*i)) ,Point(320, 88 + (stripes_distance*i)))
        stripes.setFill(color_rgb(255, 255, 0))
        stripes.draw(winOne)

# set function to draw the millennium falcon 
def draw_falcon(winOne):
    falcon_center = Point(546, 82)
    falcon_radius = 40

    body_color = color_rgb(192, 192, 192)
    wing_color = color_rgb(128, 128, 128)
    outline = color_rgb(105, 105, 105)

    thruster = Oval(Point(557, 50), Point(589, 113))
    thruster.setFill(color_rgb(224, 255, 255))
    thruster.setOutline(color_rgb(0, 255, 255))
    thruster.draw(winOne)
    
    body = Circle(falcon_center, falcon_radius)
    body.setFill(body_color)
    body.setOutline(body_color)
    body.draw(winOne)

    wing = Polygon(Point(510, 32), Point(512, 52), Point(519, 52),
                   Point(533, 74), Point(547, 62), Point(528, 27))
    
    wing.setFill(wing_color)
    wing.setOutline(wing_color)
    wing.draw(winOne)

    wing_line = Polygon(Point(522, 40), Point(536, 65), Point(538, 63), Point(524, 38))
    wing_line.setFill(outline)
    wing_line.setOutline(outline)
    wing_line.draw(winOne)

    vent_radius = 5
    
    vent_one = Circle(Point(554, 70), vent_radius)
    vent_two = Circle(Point(569, 70), vent_radius)
    vent_three = Circle(Point(575, 82), vent_radius)
    vent_four = Circle(Point(561, 82), vent_radius)
    vent_five = Circle(Point(556, 93), vent_radius)
    vent_six = Circle(Point(570, 94), vent_radius)

    vent_one.setFill(wing_color)
    vent_one.setOutline(outline)
    vent_one.draw(winOne)

    vent_two.setFill(wing_color)
    vent_two.setOutline(outline)
    vent_two.draw(winOne)

    vent_three.setFill(wing_color)
    vent_three.setOutline(outline)
    vent_three.draw(winOne)

    vent_four.setFill(wing_color)
    vent_four.setOutline(outline)
    vent_four.draw(winOne)
    
    vent_five.setFill(wing_color)
    vent_five.setOutline(outline)
    vent_five.draw(winOne)

    vent_six.setFill(wing_color)
    vent_six.setOutline(outline)
    vent_six.draw(winOne)

    cannon = Rectangle(Point(542, 100), Point(548, 122))
    cannon.setFill(wing_color)
    cannon.setOutline(wing_color)
    cannon.draw(winOne)

    front_cannon = Rectangle(Point(508, 74), Point(541, 90))
    front_cannon.setFill(wing_color)
    front_cannon.setOutline(wing_color)
    front_cannon.draw(winOne)

    right_control = Polygon(Point(516, 56), Point(483, 72), Point(483, 77), Point(507, 77))
    right_control.setFill(body_color)
    right_control.setOutline(body_color)
    right_control.draw(winOne)

    left_control = Polygon(Point(516, 109), Point(483, 89), Point(483, 83), Point(507, 83))
    left_control.setFill(body_color)
    left_control.setOutline(body_color)
    left_control.draw(winOne)

    left_win = Polygon(Point(491, 95), Point(493, 93), Point(509, 102), Point(510, 106))
    left_win.setFill(wing_color)
    left_win.setOutline(wing_color)
    left_win.draw(winOne)

    right_win = Polygon(Point(488, 66), Point(506, 57), Point(506, 61), Point(489, 70))
    right_win.setFill(wing_color)
    right_win.setOutline(wing_color)
    right_win.draw(winOne)

    return[body, wing, wing_line, vent_one, vent_two, vent_three, vent_four, vent_five,
           vent_six, cannon, front_cannon, right_control, left_control, left_win, right_win, thruster]

# setting function to draw The Outrider
def draw_outrider(winOne):
    main_color = color_rgb(192, 192, 192)
    secondary_color = color_rgb(128, 128, 128)
    third_color = color_rgb(105, 105, 105)

    outrider_center = Point(559, 247)

    outrider_window = Oval(Point(550, 209), Point(566, 217))
    outrider_window.setFill(color_rgb(224, 255, 255))
    outrider_window.setOutline(color_rgb(224, 255, 255))
    outrider_window.draw(winOne)
    
    outrider_body = Oval(Point(525, 212), Point(592, 281))
    outrider_body.setFill(main_color)
    outrider_body.setOutline(main_color)
    outrider_body.draw(winOne)

    outrider_end = Polygon(Point(536, 225), Point(494, 234), Point(500, 266), Point(547, 279))
    outrider_end.setFill(main_color)
    outrider_end.setOutline(main_color)
    outrider_end.draw(winOne)

    outline_1 = Circle(outrider_center, 26)
    outline_1.setFill(main_color)
    outline_1.draw(winOne)

    outline_2 = Circle(outrider_center, 12)
    outline_2.setFill(main_color)
    outline_2.draw(winOne)

    connector = Polygon(Point(490, 251), Point(503, 251), Point(502, 256), Point(492, 256))
    connector.setFill(third_color)
    connector.setOutline(third_color)
    connector.draw(winOne)

    thruster_1 = Rectangle(Point(486, 216), Point(507, 251))
    thruster_1.setFill(secondary_color)
    thruster_1.setOutline(secondary_color)
    thruster_1.draw(winOne)

    thruster_2 = Polygon(Point(486, 256), Point(486, 278), Point(489, 286), Point(505, 286), Point(507, 278), Point(506, 256))
    thruster_2.setFill(secondary_color)
    thruster_2.setOutline(secondary_color)
    thruster_2.draw(winOne)

    stripe_1 = Rectangle(Point(508, 240), Point(546, 252))
    stripe_1.setFill(secondary_color)
    stripe_1.setOutline(secondary_color)
    stripe_1.draw(winOne)

    stripe_2 = Rectangle(Point(552, 212), Point(565, 221))
    stripe_2.setFill(secondary_color)
    stripe_2.setOutline(secondary_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(582, 240), Point(592, 249))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    stripe_4 = Polygon(Point(544, 263), Point(550, 267), Point(548, 271), Point(540, 266))
    stripe_4.setFill(secondary_color)
    stripe_4.setOutline(secondary_color)
    stripe_4.draw(winOne)

    stripe_5 = Polygon(Point(568, 267), Point(575, 263), Point(578, 265), Point(570, 271))
    stripe_5.setFill(secondary_color)
    stripe_5.setOutline(secondary_color)
    stripe_5.draw(winOne)

    cannon_base = Rectangle(Point(553, 240), Point(564, 252))
    cannon_base.setFill(secondary_color)
    cannon_base.setOutline(secondary_color)
    cannon_base.draw(winOne)

    left_cannon = Rectangle(Point(555, 251), Point(556, 265))
    right_cannon = Rectangle(Point(562, 251), Point(563, 265))
    left_cannon.setFill(secondary_color)
    left_cannon.setOutline(secondary_color)
    right_cannon.setFill(secondary_color)
    right_cannon.setOutline(secondary_color)
    left_cannon.draw(winOne)
    right_cannon.draw(winOne)

    return[outrider_window, outrider_body, outrider_end, outline_1, outline_2,
           connector, thruster_1, thruster_2, stripe_1, stripe_2, stripe_3, stripe_4,
           stripe_5, cannon_base, left_cannon, right_cannon]

# Setting function to draw the X-wing
def draw_xwing(winOne):
    main_color = color_rgb(192, 192, 192)
    stripe_color = color_rgb(255, 160, 122)
    secondary_color = color_rgb(128, 128, 128)

    xwing_back = Oval(Point(75, 55), Point(86, 79))
    xwing_back.setFill(main_color)
    xwing_back.setOutline(main_color)
    xwing_back.draw(winOne)
    
    xwing_body = Rectangle(Point(80, 48), Point(91, 87))
    xwing_body.setFill(main_color)
    xwing_body.setOutline(main_color)
    xwing_body.draw(winOne)

    xwing_control = Rectangle(Point(70, 65), Point(95, 71))
    xwing_control.setFill(main_color)
    xwing_control.setOutline(main_color)
    xwing_control.draw(winOne)

    xwing_front = Polygon(Point(95, 66), Point(120, 66), Point(143, 67), Point(143, 69), Point(120, 70), Point(95, 70))
    xwing_front.setFill(main_color)
    xwing_front.setOutline(main_color)
    xwing_front.draw(winOne)
    
    stripe_1 = Line(Point(95, 66), Point(130, 66))
    stripe_1.setOutline(stripe_color)
    stripe_1.draw(winOne)

    stripe_2 = Line(Point(95, 70), Point(130, 70))
    stripe_2.setOutline(stripe_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(74, 67), Point(92, 70))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    engine_1 = Rectangle(Point(82, 61), Point(95, 64))
    engine_1.setFill(secondary_color)
    engine_1.setOutline(secondary_color)
    engine_1.draw(winOne)

    engine_2 = Rectangle(Point(82, 72), Point(95, 75))
    engine_2.setFill(secondary_color)
    engine_2.setOutline(secondary_color)
    engine_2.draw(winOne)

    stripe_4 = Rectangle(Point(82, 50), Point(90, 52))
    stripe_5 = Rectangle(Point(82, 83), Point(90, 85))
    stripe_4.setFill(stripe_color)
    stripe_4.setOutline(stripe_color)
    stripe_5.setFill(stripe_color)
    stripe_5.setOutline(stripe_color)
    stripe_4.draw(winOne)
    stripe_5.draw(winOne)

    left_wing = Rectangle(Point(80, 87), Point(95, 89))
    left_wing.setFill(secondary_color)
    left_wing.setOutline(secondary_color)
    left_wing.draw(winOne)

    right_wing = Rectangle(Point(80, 47), Point(95, 49))
    right_wing.setFill(secondary_color)
    right_wing.setOutline(secondary_color)
    right_wing.draw(winOne)

    right_cannon = Rectangle(Point(95, 47), Point(121, 47))
    right_cannon.setFill(main_color)
    right_cannon.setOutline(main_color)
    right_cannon.draw(winOne)

    left_cannon = Rectangle(Point(95, 87), Point(121, 87))
    left_cannon.setFill(main_color)
    left_cannon.setOutline(main_color)
    left_cannon.draw(winOne)

    thruster_1 = Rectangle(Point(67, 58), Point(82, 61))
    thruster_1.setFill(main_color)
    thruster_1.setOutline(main_color)
    thruster_1.draw(winOne)

    thruster_2 = Rectangle(Point(67, 74) ,Point(82, 77))
    thruster_2.setFill(main_color)
    thruster_2.setOutline(main_color)
    thruster_2.draw(winOne)

    return[xwing_back, xwing_body, xwing_control, xwing_front, stripe_1, stripe_2, stripe_3, 
        engine_1, engine_2, stripe_4, stripe_5,
        left_wing, right_wing, right_cannon, left_cannon, thruster_1, thruster_2] 

# setting function to draw the TIE fighters    
def draw_fighters(winOne):
    main_color = color_rgb(192, 192, 192)
    secondary_color = color_rgb(128, 128, 128)
    third_color = color_rgb(169, 169, 169)

    connector = Rectangle(Point(89, 172) ,Point(95, 207))
    connector.setFill(main_color)
    connector.setOutline(main_color)
    connector.draw(winOne)

    connector_base_1 = Polygon(Point(87, 166) ,Point(97, 166) ,Point(95, 173) ,Point(89, 173))
    connector_base_1.setFill(third_color)
    connector_base_1.setOutline(third_color)
    connector_base_1.draw(winOne)

    connector_base_2 = Polygon(Point(89, 206) ,Point(95, 206) ,Point(97, 213) ,Point(87, 213))
    connector_base_2.setFill(third_color)
    connector_base_2.setOutline(third_color)
    connector_base_2.draw(winOne)
    
    body = Circle(Point(91, 189), 9)
    body.setFill(main_color)
    body.setOutline(main_color)
    body.draw(winOne)

    left_wing = Rectangle(Point(69, 213) ,Point(117, 216))
    left_wing.setFill(secondary_color)
    left_wing.setOutline(secondary_color)
    left_wing.draw(winOne)

    right_wing = Rectangle(Point(68, 162) ,Point(116, 165))
    right_wing.setFill(secondary_color)
    right_wing.setOutline(secondary_color)
    right_wing.draw(winOne)

    stripe_1 = Circle(Point(91, 189), 6)
    stripe_1.setFill(third_color)
    stripe_1.setOutline(third_color)
    stripe_1.draw(winOne)

    front = Rectangle(Point(98, 185) ,Point(102, 194))
    front.setFill(main_color)
    front.setOutline(main_color)
    front.draw(winOne)

    stripe_2 = Rectangle(Point(91, 184) ,Point(95, 185))
    stripe_2.setFill(secondary_color)
    stripe_2.setOutline(secondary_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(91, 187) ,Point(96, 188))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    stripe_4 = Rectangle(Point(92, 190) ,Point(96, 191))
    stripe_4.setFill(secondary_color)
    stripe_4.setOutline(secondary_color)
    stripe_4.draw(winOne)

    stripe_5 = Rectangle(Point(91, 193) ,Point(95, 194))
    stripe_5.setFill(secondary_color)
    stripe_5.setOutline(secondary_color)
    stripe_5.draw(winOne)

    stripe_6 = Rectangle(Point(91, 171) ,Point(93, 180))
    stripe_6.setFill(third_color)
    stripe_6.setOutline(third_color)
    stripe_6.draw(winOne)

    stripe_7 = Rectangle(Point(91, 198) ,Point(93, 206))
    stripe_7.setFill(third_color)
    stripe_7.setOutline(third_color)
    stripe_7.draw(winOne)

    return[connector, body, left_wing, right_wing, connector_base_1, connector_base_2,
           stripe_1, front, stripe_2, stripe_3,
           stripe_4, stripe_5, stripe_6, stripe_7]

# setting function to draw the TIE bombers
def draw_bombers(winOne):
    main = color_rgb(192, 192, 192)
    secondary = color_rgb(0, 0, 0)
    third = color_rgb(169, 169, 169)
    fourth = color_rgb(75, 75, 75)
    
    left_body = Polygon(Point(86, 292) ,Point(114, 292) ,
                        Point(115, 295) ,Point(115, 308) ,Point(114, 310) ,Point(86, 310) ,Point(84, 308), Point(84, 295))

    left_body.setFill(main)
    left_body.setOutline(main)
    left_body.draw(winOne)

    right_body = Polygon(Point(85, 316) ,Point(115, 316) ,
                         Point(119, 319) ,Point(119, 330) ,Point(116, 332) ,Point(86, 332) ,Point(84, 330) ,Point(84, 318))

    right_body.setFill(main)
    right_body.setOutline(main)
    right_body.draw(winOne)

    connector = Rectangle(Point(103, 307), Point(110, 317))
    connector.setFill(third)
    connector.setOutline(third)
    connector.draw(winOne)

    left_wing = Polygon(Point(73, 281), Point(126, 281), Point(124, 291), Point(76, 291))
    left_wing.setFill(fourth)
    left_wing.draw(winOne)

    right_wing = Polygon(Point(76, 334), Point(124, 334), Point(128, 344), Point(73, 344))
    right_wing.setFill(fourth)
    right_wing.draw(winOne)

    front = Rectangle(Point(118, 320), Point(121, 329))
    front.setFill(third)
    front.setOutline(third)
    front.draw(winOne)

    stripe_1 = Rectangle(Point(90, 295), Point(107, 297))
    stripe_1.setFill(third)
    stripe_1.setOutline(third)
    stripe_1.draw(winOne)

    stripe_2 = Rectangle(Point(90, 304), Point(107, 305))
    stripe_2.setFill(third)
    stripe_2.setOutline(third)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(89, 321), Point(103, 330))
    stripe_3.setFill(third)
    stripe_3.setOutline(third)
    stripe_3.draw(winOne)

    stripe_4 = Circle(Point(111, 324), 5)
    stripe_4.setFill(third)
    stripe_4.setOutline(third)
    stripe_4.draw(winOne)

    stripe_5 = Rectangle(Point(79, 283), Point(107, 289))
    stripe_5.setFill(secondary)
    stripe_5.draw(winOne)

    stripe_6 = Polygon(Point(112, 283), Point(124, 283), Point(121, 289), Point(112, 289))
    stripe_6.setFill(secondary)
    stripe_6.draw(winOne)

    stripe_7 = Rectangle(Point(78, 336), Point(106, 342))
    stripe_7.setFill(secondary)
    stripe_7.draw(winOne)

    stripe_8 = Polygon(Point(113, 336), Point(121, 336), Point(125, 342), Point(113, 342))
    stripe_8.setFill(secondary)
    stripe_8.draw(winOne)

    return[left_body, right_body, connector, left_wing, right_wing, front, stripe_1, stripe_2,
           stripe_3, stripe_4, stripe_5, stripe_6, stripe_7, stripe_8]

# setting function to draw the opening message of the first scene
def opening_message(winOne):
    message_box = Rectangle(Point(254, 114), Point(388, 223))
    message_box.setFill(color_rgb(255, 255, 255))
    message_box.draw(winOne)

    line_1 = Text(Point(318, 135), "WARNING:")
    line_1.setSize(14)
    line_1.draw(winOne)

    line_2 = Text(Point(319, 154), "You are trapped inside an")
    line_2.setSize(8)
    line_2.draw(winOne)

    line_3 = Text(Point(318, 166), "enemy spaceship. You")
    line_3.setSize(8)
    line_3.draw(winOne)

    line_4 = Text(Point(320, 177), "must escape into space by")
    line_4.setSize(8)
    line_4.draw(winOne)

    line_5 = Text(Point(317, 189), "taking over one of these")
    line_5.setSize(8)
    line_5.draw(winOne)

    line_6 = Text(Point(320, 200), "spacecrafts.")
    line_6.setSize(8)
    line_6.draw(winOne)

    for i in range(5):
        time.sleep(0.001)

    message_box.undraw()    
    line_1.undraw()
    line_2.undraw()
    line_3.undraw()
    line_4.undraw()
    line_5.undraw()
    line_6.undraw()
    
# setting function to execute all the programs in scene one 
def scene_one():
    winOne = GraphWin("Scene One", 640, 360)
    winOne.setBackground(color_rgb(70, 70, 70))

    MAX_X = 640
    MAX_Y = 360

    MIN_X = 0
    MIN_Y = 0

    parking_slots(winOne)
    draw_runway(winOne)
    falcon_parts = draw_falcon(winOne)
    outrider_parts = draw_outrider(winOne)
    xwing_parts = draw_xwing(winOne)
    fighters_parts = draw_fighters(winOne)
    bombers_parts = draw_bombers(winOne)
    draw_walls(winOne)

    light_color = color_rgb(0, 255, 0)
    light_off = color_rgb(255, 0, 0)
    light_radius = 8
    
    parking_light_1 = Circle(Point(470, 80), light_radius)
    parking_light_1.setFill(light_color)
    parking_light_1.draw(winOne)

    parking_light_2 = Circle(Point(470, 246), light_radius)
    parking_light_2.setFill(light_color)
    parking_light_2.draw(winOne)

    parking_light_3 = Circle(Point(167, 64), light_radius)
    parking_light_3.setFill(light_color)
    parking_light_3.draw(winOne)

    parking_light_4 = Circle(Point(167, 186), light_radius)
    parking_light_4.setFill(light_color)
    parking_light_4.draw(winOne)

    parking_light_5 = Circle(Point(167, 310), light_radius)
    parking_light_5.setFill(light_color)
    parking_light_5.draw(winOne)

    opening_message(winOne)
    
    text_box = Rectangle(Point(180, 165), Point(458, 193))
    text_box.setFill(color_rgb(255, 255, 255))
    text_box.draw(winOne)

    entry_size = 30
    user_input = Entry(Point(320, 180), entry_size)
    user_input.setText("Select your spacecraft (Enter number): ")
    user_input.draw(winOne)

    key_pressed = winOne.getKey()
    if key_pressed == "BackSpace":
        key_pressed = ""   
    selection = user_input.clone()
    selection.setText(key_pressed)
    selection.draw(winOne)

    # setting for loop
    # determines which spacecraft user has chosen and moves it until its off the scene
    while True:
        winOne.getMouse()
        user_choice = selection.getText()
        if user_choice == "1":
            user_input.undraw()
            selection.undraw()
            text_box.undraw()

            parking_light_1.undraw()
            parking_light_1.setFill(light_off)
            parking_light_1.draw(winOne)

            play_sound(winOne)

            falcon_vertex = 483
            while falcon_vertex <= MAX_X:
                for parts in falcon_parts:
                    parts.move(1, 0)
                    time.sleep(0.001)
                    
                falcon_vertex += 1

            break

        elif user_choice == "2":
            user_input.undraw()
            selection.undraw()
            text_box.undraw()

            parking_light_2.undraw()
            parking_light_2.setFill(light_off)
            parking_light_2.draw(winOne)

            play_sound(winOne)

            outrider_vertex = 485
            while outrider_vertex <= MAX_X:
                for parts in outrider_parts:
                    parts.move(1, 0)
                    time.sleep(0.001)

                outrider_vertex += 1
                

            break
            

        elif user_choice == "3":
            user_input.undraw()
            selection.undraw()
            text_box.undraw()

            parking_light_3.undraw()
            parking_light_3.setFill(light_off)
            parking_light_3.draw(winOne)

            play_sound(winOne)

            xwing_vertex = 144
            while xwing_vertex >= MIN_X:
                for parts in xwing_parts:
                    parts.move(-1, 0)
                    time.sleep(0.001)

                xwing_vertex -= 1
                    
            break
    

        elif user_choice == "4":
            user_input.undraw()
            selection.undraw()
            text_box.undraw()

            parking_light_4.undraw()
            parking_light_4.setFill(light_off)
            parking_light_4.draw(winOne)

            play_sound(winOne)

            fighters_vertex = 115
            while fighters_vertex >= MIN_X:
                for parts in fighters_parts:
                    parts.move(-1, 0)
                    time.sleep(0.001)

                fighters_vertex -= 1
                    
            break

        elif user_choice == "5":
            user_input.undraw()
            selection.undraw()
            text_box.undraw()

            parking_light_5.undraw()
            parking_light_5.setFill(light_off)
            parking_light_5.draw(winOne)

            play_sound(winOne)
            
            bombers_vertex = 130
            while bombers_vertex >= MIN_X:
                for parts in bombers_parts:
                    parts.move(-1, 0)
                    time.sleep(0.001)

                bombers_vertex -= 1

            break
        
    winOne.close()
    return user_choice


# setting function to draw 70 stars at random positions on the screen
def draw_stars(winTwo):
    num_stars = 70
    star_color = color_rgb(255, 255, 255)

    for s in range(num_stars):
        star_radius = 2
        if s >= (num_stars/2):
            star_X = random.randint(321, 640)
            
        else:
            star_X = random.randint(1, 320)

        star_Y = random.randint(1, 360)   
        stars = Oval(Point(star_X, star_Y), Point(star_X + star_radius, star_Y + (star_radius+1)))
        stars.setFill(star_color)
        stars.setOutline(star_color)
        stars.draw(winTwo)

# setting fucntion to draw the floor of the big spaceship
def draw_floor(winTwo):
    floor_color = color_rgb(70, 70, 70)
    floor = Rectangle(Point(0, 129), Point(640, 360))
    floor.setFill(floor_color)
    floor.draw(winTwo)

    return[floor]

# setting function to draw all parking slots and labels located on the right side
def right_parking_s2(winTwo):
    slot_color = color_rgb(0,0,0)
    outline = color_rgb(255, 255, 0)
    label_color = color_rgb(128, 128, 128)
    num_color = color_rgb(255, 255, 255)

    slot_1 = Polygon(Point(433, 144), Point(520, 144), Point(539, 210), Point(454, 210))
    slot_1.setFill(slot_color)
    slot_1.setOutline(outline)
    slot_1.draw(winTwo)    

    num_slot1 = Polygon( Point(550, 166), Point(577, 166), Point(584, 183), Point(556, 183))
    num_slot1.setFill(slot_color)
    num_slot1.draw(winTwo)

    num_1 = Text(Point(569, 174), "1")
    num_1.setSize(12)
    num_1.setTextColor(num_color)
    num_1.draw(winTwo)

    slot_2 = Polygon(Point(460, 244), Point(559, 244), Point(582, 327), Point(484, 327))
    slot_2.setFill(slot_color)
    slot_2.setOutline(outline)
    slot_2.draw(winTwo)

    num_slot2 = Polygon(Point(583, 267), Point(611, 267), Point(618, 290), Point(588, 290))
    num_slot2.setFill(slot_color)
    num_slot2.draw(winTwo)

    num_2 = Text(Point(601, 279), "2")
    num_2.setSize(12)
    num_2.setTextColor(num_color)
    num_2.draw(winTwo)

    return[slot_1, num_slot1, num_1, slot_2, num_slot2, num_2]

# setting function to draw all parking slots located towards the left
def left_parking_s2(winTwo):
    slot_color = color_rgb(0,0,0)
    outline = color_rgb(255, 255, 0)
    label_color = color_rgb(128, 128, 128)
    
    num_color = color_rgb(255, 255, 255)
    slot_3 = Polygon(Point(198, 145), Point(123, 145), Point(107, 187), Point(181, 187))
    slot_3.setFill(slot_color)
    slot_3.setOutline(outline)
    slot_3.draw(winTwo)

    num_slot3 = Polygon(Point(76, 152), Point(102, 152), Point(96, 170), Point(68, 170))
    num_slot3.setFill(slot_color)
    num_slot3.draw(winTwo)

    num_3 = Text(Point(84, 161), "3")
    num_3.setSize(12)
    num_3.setTextColor(num_color)
    num_3.draw(winTwo)

    slot_4 = Polygon(Point(93, 211), Point(174, 211), Point(155, 255), Point(74, 255))
    slot_4.setFill(slot_color)
    slot_4.setOutline(outline)
    slot_4.draw(winTwo)

    num_slot4 = Polygon(Point(46, 222), Point(73, 222), Point(66, 240), Point(39, 240))
    num_slot4.setFill(slot_color)
    num_slot4.draw(winTwo)

    num_4 = Text(Point(55, 230), "4")
    num_4.setSize(12)
    num_4.setTextColor(num_color)
    num_4.draw(winTwo)

    slot_5 = Polygon(Point(59, 287), Point(145, 287), Point(124, 335), Point(37, 335))
    slot_5.setFill(slot_color)
    slot_5.setOutline(outline)
    slot_5.draw(winTwo)

    num_slot5 = Polygon(Point(12, 297), Point(39, 297), Point(32, 314), Point(6, 314))
    num_slot5.setFill(slot_color)
    num_slot5.draw(winTwo)

    num_5 = Text(Point(21, 304), "5")
    num_5.setSize(12)
    num_5.setTextColor(num_color)
    num_5.draw(winTwo)


    return[slot_3, num_slot3, num_3, slot_4, num_slot4, num_4, slot_5, num_slot5, num_5]

# setting function to draw the runway in the second perspective
def draw_runway_s2(winTwo):
    runway = Polygon(Point(300, 127), Point(340, 127), Point(370, 360), Point(268, 360))
    runway.setFill(color_rgb(0, 0 ,0 ))
    runway.setOutline(color_rgb(255, 0 ,0))
    runway.draw(winTwo)

    return[runway]

# setting function to draw all runway lights that are on the left side
def runway_left_lights(winTwo):
    light_radius = 5
    light_color = color_rgb(255, 165, 0)

    left_light1 = Circle(Point(291, 135), light_radius)
    left_light1.setFill(light_color)
    left_light1.draw(winTwo)
    
    left_light2 = Circle(Point(281, 185), light_radius)
    left_light2.setFill(light_color)
    left_light2.draw(winTwo)
    
    left_light3 = Circle(Point(270, 235), light_radius)
    left_light3.setFill(light_color)
    left_light3.draw(winTwo)
    
    left_light4 = Circle(Point(261, 285), light_radius)
    left_light4.setFill(light_color)
    left_light4.draw(winTwo)

    left_light5 = Circle(Point(250, 335), light_radius)
    left_light5.setFill(light_color)
    left_light5.draw(winTwo)    

    return[left_light1, left_light2, left_light3, left_light4, left_light5]

# setting function to draw all runway lights that are on the right side
def runway_right_lights(winTwo):
    light_radius = 5
    light_color = color_rgb(255, 165, 0)

    right_light1 = Circle(Point(351, 135), light_radius)
    right_light1.setFill(light_color)
    right_light1.draw(winTwo)
    
    right_light2 = Circle(Point(360, 185), light_radius)
    right_light2.setFill(light_color)
    right_light2.draw(winTwo)
    
    right_light3 = Circle(Point(370, 235), light_radius)
    right_light3.setFill(light_color)
    right_light3.draw(winTwo)
    
    right_light4 = Circle(Point(380, 285), light_radius)
    right_light4.setFill(light_color)
    right_light4.draw(winTwo)
    
    right_light5 = Circle(Point(391, 335), light_radius)
    right_light5.setFill(light_color)
    right_light5.draw(winTwo)

    return[right_light1, right_light2, right_light3, right_light4, right_light5]

# setting function to draw the lines under the runway
def runway_markings(winTwo):
    stripes_color = color_rgb(255, 255, 0)

    mark1 = Line(Point(320, 134), Point(320, 153))
    mark1.setFill(stripes_color)
    mark1.draw(winTwo)

    mark2 = Line(Point(320, 184), Point(320, 203))
    mark2.setFill(stripes_color)
    mark2.draw(winTwo)
    
    mark3 = Line(Point(320, 234), Point(320, 253))
    mark3.setFill(stripes_color)
    mark3.draw(winTwo)
    
    mark4 = Line(Point(320, 284), Point(320, 303))
    mark4.setFill(stripes_color)
    mark4.draw(winTwo)
    
    mark5 = Line(Point(320, 334), Point(320, 353))
    mark5.setFill(stripes_color)
    mark5.draw(winTwo)

    return[mark1, mark2, mark3, mark4, mark5]
    
    for i in range(5):
        stripes = Line(Point(stripes_x1, stripes_y1), Point(stripes_x1, stripes_y2))
        stripes.setFill(stripes_color)
        stripes.draw(winTwo)

        stripes_y1 += stripes_distance
        stripes_y2 += stripes_distance

# setting function to draw millennium falcon (second perspective) 
def falcon_s2_p1(winOne):
    body_color = color_rgb(192, 192, 192)
    wing_color = color_rgb(128, 128, 128)
    outline = color_rgb(105, 105, 105)

    thruster = Oval(Point(505, 146), Point(538, 190))
    thruster.setFill(color_rgb(224, 255, 255))
    thruster.setOutline(color_rgb(0, 255, 255))
    thruster.draw(winOne)
    
    body = Oval(Point(452, 142), Point(537, 196))
    body.setFill(body_color)
    body.setOutline(body_color)
    body.draw(winOne)
    
    vent_one = Oval(Point(497, 158), Point(506, 162))
    vent_two = Oval(Point(503, 165), Point(513, 170))
    vent_three = Oval(Point(497, 172), Point(507, 177))
    vent_four = Oval(Point(512, 157), Point(522, 162))
    vent_five = Oval(Point(519, 164), Point(528, 170))
    vent_six = Oval(Point(512, 172), Point(522, 177))

    vent_one.setFill(wing_color)
    vent_one.setOutline(outline)
    vent_one.draw(winOne)

    vent_two.setFill(wing_color)
    vent_two.setOutline(outline)
    vent_two.draw(winOne)

    vent_three.setFill(wing_color)
    vent_three.setOutline(outline)
    vent_three.draw(winOne)

    vent_four.setFill(wing_color)
    vent_four.setOutline(outline)
    vent_four.draw(winOne)
    
    vent_five.setFill(wing_color)
    vent_five.setOutline(outline)
    vent_five.draw(winOne)

    vent_six.setFill(wing_color)
    vent_six.setOutline(outline)
    vent_six.draw(winOne)

    cannon = Rectangle(Point(487, 181), Point(494, 196))
    cannon.setFill(wing_color)
    cannon.setOutline(wing_color)
    cannon.draw(winOne)

    right_control = Polygon(Point(465, 149), Point(424, 163), Point(424, 167), Point(465, 167))
    right_control.setFill(body_color)
    right_control.setOutline(body_color)
    right_control.draw(winOne)

    left_control = Polygon(Point(465, 189), Point(465, 170), Point(424, 170), Point(424, 175))
    left_control.setFill(body_color)
    left_control.setOutline(body_color)
    left_control.draw(winOne)

    wing = Polygon(Point(452, 138), Point(474, 132), Point(494, 155),
                   Point(479, 163), Point(464, 149), Point(457, 151))
    
    wing.setFill(wing_color)
    wing.setOutline(wing_color)
    wing.draw(winOne)

    wing_line = Polygon(Point(468, 142), Point(470, 141), Point(485, 156), Point(483, 157))
    wing_line.setFill(outline)
    wing_line.setOutline(outline)
    wing_line.draw(winOne)

    front_cannon = Rectangle(Point(452, 164), Point(486, 171))
    front_cannon.setFill(wing_color)
    front_cannon.setOutline(wing_color)
    front_cannon.draw(winOne)

    left_win = Polygon(Point(430, 160), Point(450, 152), Point(452, 155), Point(432, 162))
    left_win.setFill(wing_color)
    left_win.setOutline(wing_color)
    left_win.draw(winOne)

    right_win = Polygon(Point(433, 178), Point(451, 185), Point(452, 183), Point(434, 176))
    right_win.setFill(wing_color)
    right_win.setOutline(wing_color)
    right_win.draw(winOne)

    return[body, wing, wing_line, vent_one, vent_two, vent_three, vent_four, vent_five,
           vent_six, cannon, front_cannon, right_control, left_control, left_win, right_win, thruster]


# setting function to draw outrider (second perspective)
def outrider_s2_p1(winOne):
    main_color = color_rgb(192, 192, 192)
    secondary_color = color_rgb(128, 128, 128)
    third_color = color_rgb(105, 105, 105)

    y_shift = 6
    
    outrider_window = Oval(Point(550 - 17, 209 + 38), Point(566 - 17, 217 + 38))
    outrider_window.setFill(color_rgb(224, 255, 255))
    outrider_window.setOutline(color_rgb(224, 255, 255))
    outrider_window.draw(winOne)
    
    outrider_body = Oval(Point(504, 244+y_shift), Point(580, 296+y_shift))
    outrider_body.setFill(main_color)
    outrider_body.setOutline(main_color)
    outrider_body.draw(winOne)

    outrider_end = Polygon(Point(517, 252+y_shift), Point(464, 265+y_shift), Point(471, 289+y_shift), Point(529, 295+y_shift))
    outrider_end.setFill(main_color)
    outrider_end.setOutline(main_color)
    outrider_end.draw(winOne)

    outline_1 = Oval(Point(574, 287+y_shift), Point(509, 250+y_shift))
    outline_1.setFill(main_color)
    outline_1.draw(winOne)

    outline_2 = Oval(Point(525, 261+y_shift), Point(558, 278+y_shift))
    outline_2.setFill(main_color)
    outline_2.draw(winOne)

    connector = Polygon(Point(490 - 32, 251 + 25), Point(503 - 32, 251 + 25), Point(502 - 32, 256 + 25), Point(492 - 32, 256 + 25))
    connector.setFill(third_color)
    connector.setOutline(third_color)
    connector.draw(winOne)

    thruster_1 = Rectangle(Point(448, 249), Point(479, 275))
    thruster_1.setFill(secondary_color)
    thruster_1.setOutline(secondary_color)
    thruster_1.draw(winOne)

    thruster_2 = Polygon(Point(451, 281), Point(451, 300), Point(454, 307), Point(473, 307), Point(476, 301), Point(476, 281))
    thruster_2.setFill(secondary_color)
    thruster_2.setOutline(secondary_color)
    thruster_2.draw(winOne)

    stripe_1 = Rectangle(Point(481, 270), Point(527, 281))
    stripe_1.setFill(secondary_color)
    stripe_1.setOutline(secondary_color)
    stripe_1.draw(winOne)

    stripe_2 = Rectangle(Point(535, 250), Point(549, 259))
    stripe_2.setFill(secondary_color)
    stripe_2.setOutline(secondary_color)
    stripe_2.draw(winOne)

    stripe_4 = Polygon(Point(525, 287), Point(532, 289), Point(530, 292), Point(522, 289))
    stripe_4.setFill(secondary_color)
    stripe_4.setOutline(secondary_color)
    stripe_4.draw(winOne)

    stripe_5 = Polygon(Point(557, 288), Point(562, 285), Point(565, 288), Point(556, 291))
    stripe_5.setFill(secondary_color)
    stripe_5.setOutline(secondary_color)
    stripe_5.draw(winOne)

    cannon_base = Rectangle(Point(536, 272), Point(548, 279))
    cannon_base.setFill(secondary_color)
    cannon_base.setOutline(secondary_color)
    cannon_base.draw(winOne)

    left_cannon = Rectangle(Point(539, 278), Point(540, 287))
    right_cannon = Rectangle(Point(544, 278), Point(545, 287))
    left_cannon.setFill(secondary_color)
    left_cannon.setOutline(secondary_color)
    right_cannon.setFill(secondary_color)
    right_cannon.setOutline(secondary_color)
    left_cannon.draw(winOne)
    right_cannon.draw(winOne)

    return[outrider_window, outrider_body, outrider_end, outline_1, outline_2,
           connector, thruster_1, thruster_2, stripe_1, stripe_2, stripe_4,
           stripe_5, cannon_base, left_cannon, right_cannon]

# setting function to draw X-wing (second perspective)
def xwing_s2_p1(winOne):
    x_shift = 0
    y_shift = 0
    main_color = color_rgb(192, 192, 192)
    stripe_color = color_rgb(255, 160, 122)
    secondary_color = color_rgb(128, 128, 128)

    xwing_back = Oval(Point(126, 150), Point(141, 168))
    xwing_back.setFill(main_color)
    xwing_back.setOutline(main_color)
    xwing_back.draw(winOne)
    
    xwing_body = Rectangle(Point(132, 144), Point(148, 175))
    xwing_body.setFill(main_color)
    xwing_body.setOutline(main_color)
    xwing_body.draw(winOne)

    xwing_control = Rectangle(Point(124, 157), Point(151, 162))
    xwing_control.setFill(main_color)
    xwing_control.setOutline(main_color)
    xwing_control.draw(winOne)

    xwing_front = Rectangle(Point(152, 158), Point(218, 160))
    xwing_front.setFill(main_color)
    xwing_front.setOutline(main_color)
    xwing_front.draw(winOne)
    
    stripe_1 = Line(Point(152, 158), Point(200, 158))
    stripe_1.setOutline(stripe_color)
    stripe_1.draw(winOne)

    stripe_2 = Line(Point(152, 160), Point(200, 160))
    stripe_2.setOutline(stripe_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(126, 159), Point(148, 161))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    engine_1 = Rectangle(Point(134, 154), Point(151, 157))
    engine_1.setFill(secondary_color)
    engine_1.setOutline(secondary_color)
    engine_1.draw(winOne)

    engine_2 = Rectangle(Point(134, 163), Point(151, 165))
    engine_2.setFill(secondary_color)
    engine_2.setOutline(secondary_color)
    engine_2.draw(winOne)

    stripe_4 = Rectangle(Point(133, 145), Point(144, 147))
    stripe_5 = Rectangle(Point(134, 172), Point(145, 174))
    stripe_4.setFill(stripe_color)
    stripe_4.setOutline(stripe_color)
    stripe_5.setFill(stripe_color)
    stripe_5.setOutline(stripe_color)
    stripe_4.draw(winOne)
    stripe_5.draw(winOne)

    left_wing = Rectangle(Point(131, 143), Point(151, 145))
    left_wing.setFill(secondary_color)
    left_wing.setOutline(secondary_color)
    left_wing.draw(winOne)

    right_wing = Rectangle(Point(131, 175), Point(151, 177))
    right_wing.setFill(secondary_color)
    right_wing.setOutline(secondary_color)
    right_wing.draw(winOne)

    right_cannon = Line(Point(152, 177), Point(187, 177))
    right_cannon.setFill(main_color)
    right_cannon.setOutline(main_color)
    right_cannon.draw(winOne)

    left_cannon = Line(Point(151, 143), Point(187, 143))
    left_cannon.setFill(main_color)
    left_cannon.setOutline(main_color)
    left_cannon.draw(winOne)

    thruster_1 = Rectangle(Point(115, 153), Point(133, 155))
    thruster_1.setFill(main_color)
    thruster_1.setOutline(main_color)
    thruster_1.draw(winOne)

    thruster_2 = Rectangle(Point(115, 164), Point(133, 166))
    thruster_2.setFill(main_color)
    thruster_2.setOutline(main_color)
    thruster_2.draw(winOne)

    return[xwing_back, xwing_body, xwing_control, xwing_front, stripe_1, stripe_2, stripe_3, 
        engine_1, engine_2, stripe_4, stripe_5,
        left_wing, right_wing, right_cannon, left_cannon, thruster_1, thruster_2] 

# setting function to draw TIE fighters (second perspective)
def fighters_s2_p1(winOne):
    main_color = color_rgb(192, 192, 192)
    secondary_color = color_rgb(128, 128, 128)
    third_color = color_rgb(169, 169, 169)

    connector = Rectangle(Point(129, 239), Point(126, 216))
    connector.setFill(main_color)
    connector.setOutline(main_color)
    connector.draw(winOne)

    connector_base_1 = Polygon(Point(121, 210), Point(133, 210), Point(131, 215), Point(124, 215))
    connector_base_1.setFill(third_color)
    connector_base_1.setOutline(third_color)
    connector_base_1.draw(winOne)

    connector_base_2 = Polygon(Point(123, 239), Point(131, 239), Point(133, 244), Point(121, 244))
    connector_base_2.setFill(third_color)
    connector_base_2.setOutline(third_color)
    connector_base_2.draw(winOne)
    
    body = Oval(Point(119, 220), Point(136, 233))
    body.setFill(main_color)
    body.setOutline(main_color)
    body.draw(winOne)

    left_wing = Rectangle(Point(104, 208), Point(159, 209))
    left_wing.setFill(secondary_color)
    left_wing.setOutline(secondary_color)
    left_wing.draw(winOne)

    right_wing = Rectangle(Point(96, 245), Point(151, 246))
    right_wing.setFill(secondary_color)
    right_wing.setOutline(secondary_color)
    right_wing.draw(winOne)

    stripe_1 = Oval(Point(123, 222), Point(133, 231))
    stripe_1.setFill(third_color)
    stripe_1.setOutline(third_color)
    stripe_1.draw(winOne)

    stripe_2 = Line(Point(127, 224), Point(131, 224))
    stripe_2.setFill(secondary_color)
    stripe_2.setOutline(secondary_color)
    stripe_2.draw(winOne)

    stripe_3 = Line(Point(127, 226), Point(133, 226))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    stripe_4 = Line(Point(128, 228), Point(133, 228))
    stripe_4.setFill(secondary_color)
    stripe_4.setOutline(secondary_color)
    stripe_4.draw(winOne)

    stripe_5 = Line(Point(126, 230), Point(130, 230))
    stripe_5.setFill(secondary_color)
    stripe_5.setOutline(secondary_color)
    stripe_5.draw(winOne)

    stripe_6 = Rectangle(Point(127, 215), Point(128, 221))
    stripe_6.setFill(third_color)
    stripe_6.setOutline(third_color)
    stripe_6.draw(winOne)

    stripe_7 = Rectangle(Point(127, 234), Point(128, 240))
    stripe_7.setFill(third_color)
    stripe_7.setOutline(third_color)
    stripe_7.draw(winOne)

    return[connector, body, left_wing, right_wing, connector_base_1, connector_base_2,
           stripe_1, stripe_2, stripe_3,
           stripe_4, stripe_5, stripe_6, stripe_7]

# setting function to draw TIE bombers (second perspective)
def bombers_s2_p1(winOne):
    main = color_rgb(192, 192, 192)
    secondary = color_rgb(0, 0, 0)
    third = color_rgb(169, 169, 169)
    fourth = color_rgb(75, 75, 75)
    
    left_body = Polygon(Point(65, 292), Point(111, 292), Point(113, 294),
                        Point(113, 298), Point(110, 303), Point(65, 303))

    left_body.setFill(main)
    left_body.setOutline(main)
    left_body.draw(winOne)

    right_body = Polygon(Point(64, 307), Point(64, 317),
                         Point(115, 317), Point(119, 316), Point(119, 308), Point(113, 307))

    right_body.setFill(main)
    right_body.setOutline(main)
    right_body.draw(winOne)

    connector = Rectangle(Point(92, 302), Point(105, 310))
    connector.setFill(third)
    connector.setOutline(third)
    connector.draw(winOne)

    left_wing = Polygon(Point(48, 280), Point(138, 280), Point(137, 290), Point(51, 290))
    left_wing.setFill(fourth)
    left_wing.draw(winOne)

    right_wing = Polygon(Point(54, 318), Point(141, 318), Point(143, 329), Point(53, 329))
    right_wing.setFill(fourth)
    right_wing.draw(winOne)

    front = Rectangle(Point(120, 308), Point(123, 316))
    front.setFill(third)
    front.setOutline(third)
    front.draw(winOne)

    stripe_1 = Rectangle(Point(72, 294), Point(100, 295))
    stripe_1.setFill(third)
    stripe_1.setOutline(third)
    stripe_1.draw(winOne)

    stripe_2 = Rectangle(Point(72, 299), Point(100, 300))
    stripe_2.setFill(third)
    stripe_2.setOutline(third)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(68, 309), Point(89, 315))
    stripe_3.setFill(third)
    stripe_3.setOutline(third)
    stripe_3.draw(winOne)

    stripe_4 = Oval(Point(101, 310), Point(113, 316))
    stripe_4.setFill(third)
    stripe_4.setOutline(third)
    stripe_4.draw(winOne)

    stripe_5 = Rectangle(Point(59, 282), Point(106, 288))
    stripe_5.setFill(secondary)
    stripe_5.draw(winOne)

    stripe_6 = Polygon(Point(113, 282), Point(128, 282), Point(125, 288), Point(113, 288))
    stripe_6.setFill(secondary)
    stripe_6.draw(winOne)
    
    stripe_7 = Rectangle(Point(63, 320), Point(110, 327))
    stripe_7.setFill(secondary)
    stripe_7.draw(winOne)

    stripe_8 = Polygon(Point(117, 320), Point(131, 320), Point(136, 327), Point(117, 327))
    stripe_8.setFill(secondary)
    stripe_8.draw(winOne)

    return[left_body, right_body, connector, left_wing, right_wing, front, stripe_1, stripe_2,
           stripe_3, stripe_4, stripe_5, stripe_6, stripe_7, stripe_8]

# setting function to draw millennium falcon in launching perspective
def falcon_s2_p2(winOne):
    # x shift and y_shift helps to adjust shape position in the right place
    x_shift = 8
    y_shift = 110
    
    body_color = color_rgb(192, 192, 192)
    wing_color = color_rgb(128, 128, 128)
    outline = color_rgb(105, 105, 105)

    thruster = Oval(Point(359, 360+y_shift), Point(278, 329+y_shift))
    thruster.setFill(color_rgb(224, 255, 255))
    thruster.setOutline(color_rgb(0, 255, 255))
    thruster.draw(winOne)
    
    body = Oval(Point(266, 284+y_shift), Point(370, 356+y_shift))
    body.setFill(body_color)
    body.setOutline(body_color)
    body.draw(winOne)

    right_control = Polygon(Point(347+x_shift, 294+y_shift), Point(323+x_shift, 255+y_shift), Point(317+x_shift, 255+y_shift), Point(317+x_shift, 294+y_shift))
    right_control.setFill(body_color)
    right_control.setOutline(body_color)
    right_control.draw(winOne)

    left_control = Polygon(Point(265+x_shift, 301+y_shift), Point(301+x_shift, 255+y_shift), Point(306+x_shift, 255+y_shift), Point(305+x_shift, 301+y_shift))
    left_control.setFill(body_color)
    left_control.setOutline(body_color)
    left_control.draw(winOne)
    
    wing = Polygon(Point(319+x_shift, 302+y_shift), Point(334+x_shift, 316+y_shift), Point(378+x_shift, 297+y_shift),
                   Point(370+x_shift, 278+y_shift), Point(344+x_shift, 281+y_shift), Point(348+x_shift, 290+y_shift))
    
    wing.setFill(wing_color)
    wing.setOutline(wing_color)
    wing.draw(winOne)

    wing_line = Polygon(Point(332+x_shift, 305+y_shift), Point(332+x_shift, 307+y_shift), Point(364+x_shift, 293+y_shift), Point(362+x_shift, 292+y_shift))
    wing_line.setFill(outline)
    wing_line.setOutline(outline)
    wing_line.draw(winOne)

    vent_radius = 5
    
    vent_one = Circle(Point(295+x_shift, 323+y_shift), vent_radius)
    vent_two = Circle(Point(310+x_shift, 328+y_shift), vent_radius)
    vent_three = Circle(Point(323+x_shift, 322+y_shift), vent_radius)
    vent_four = Circle(Point(323+x_shift, 335+y_shift), vent_radius)
    vent_five = Circle(Point(310+x_shift, 342+y_shift), vent_radius)
    vent_six = Circle(Point(295+x_shift, 336+y_shift), vent_radius)

    vent_one.setFill(wing_color)
    vent_one.setOutline(outline)
    vent_one.draw(winOne)

    vent_two.setFill(wing_color)
    vent_two.setOutline(outline)
    vent_two.draw(winOne)

    vent_three.setFill(wing_color)
    vent_three.setOutline(outline)
    vent_three.draw(winOne)

    vent_four.setFill(wing_color)
    vent_four.setOutline(outline)
    vent_four.draw(winOne)
    
    vent_five.setFill(wing_color)
    vent_five.setOutline(outline)
    vent_five.draw(winOne)

    vent_six.setFill(wing_color)
    vent_six.setOutline(outline)
    vent_six.draw(winOne)

    cannon = Rectangle(Point(258+x_shift, 312+y_shift), Point(288+x_shift, 319+y_shift))
    cannon.setFill(wing_color)
    cannon.setOutline(wing_color)
    cannon.draw(winOne)

    front_cannon = Rectangle(Point(301+x_shift, 278+y_shift), Point(320+x_shift, 309+y_shift))
    front_cannon.setFill(wing_color)
    front_cannon.setOutline(wing_color)
    front_cannon.draw(winOne)

    left_win = Polygon(Point(289, 277+y_shift), Point(292, 280+y_shift), Point(303, 267+y_shift), Point(301, 262+y_shift))
    left_win.setFill(wing_color)
    left_win.setOutline(wing_color)
    left_win.draw(winOne)

    right_win = Polygon(Point(324+x_shift, 261+y_shift), Point(334+x_shift, 277+y_shift), Point(338+x_shift, 277+y_shift), Point(328+x_shift, 260+y_shift))
    right_win.setFill(wing_color)
    right_win.setOutline(wing_color)
    right_win.draw(winOne)

    return[body, wing, wing_line, vent_one, vent_two, vent_three, vent_four, vent_five,
           vent_six, cannon, front_cannon, right_control, left_control, left_win, right_win, thruster]


# setting function to draw the outrider in launching perspective
def outrider_s2_p2(winOne):
    # x and y shift helps adjust the shapes into correct position
    x_shift = 239
    y_shift = 53 + 100 
    main_color = color_rgb(192, 192, 192)
    secondary_color = color_rgb(128, 128, 128)
    third_color = color_rgb(105, 105, 105)

    outrider_center = Point(559-x_shift, 247+y_shift)

    outrider_window = Oval(Point(550-x_shift, 209+y_shift+67), Point(566-x_shift, 217+y_shift+67))
    outrider_window.setFill(color_rgb(224, 255, 255))
    outrider_window.setOutline(color_rgb(224, 255, 255))
    outrider_window.draw(winOne)
    
    outrider_body = Oval(Point(525-x_shift, 212+y_shift), Point(592-x_shift, 281+y_shift))
    outrider_body.setFill(main_color)
    outrider_body.setOutline(main_color)
    outrider_body.draw(winOne)

    outrider_end = Polygon(Point(536-x_shift, 225+y_shift), Point(494-x_shift, 234+y_shift), Point(500-x_shift, 266+y_shift), Point(547-x_shift, 279+y_shift))
    outrider_end.setFill(main_color)
    outrider_end.setOutline(main_color)
    outrider_end.draw(winOne)

    outline_1 = Circle(outrider_center, 26)
    outline_1.setFill(main_color)
    outline_1.draw(winOne)

    outline_2 = Circle(outrider_center, 12)
    outline_2.setFill(main_color)
    outline_2.draw(winOne)

    connector = Polygon(Point(490-x_shift, 251+y_shift), Point(503-x_shift, 251+y_shift), Point(502-x_shift, 256+y_shift), Point(492-x_shift, 256+y_shift))
    connector.setFill(third_color)
    connector.setOutline(third_color)
    connector.draw(winOne)

    thruster_1 = Rectangle(Point(486-x_shift, 216+y_shift), Point(507-x_shift, 251+y_shift))
    thruster_1.setFill(secondary_color)
    thruster_1.setOutline(secondary_color)
    thruster_1.draw(winOne)

    thruster_2 = Polygon(Point(486-x_shift, 256+y_shift), Point(486-x_shift, 278+y_shift), Point(489-x_shift, 286+y_shift), Point(505-x_shift, 286+y_shift),
                         Point(507-x_shift, 278+y_shift), Point(506-x_shift, 256+y_shift))
    thruster_2.setFill(secondary_color)
    thruster_2.setOutline(secondary_color)
    thruster_2.draw(winOne)

    stripe_1 = Rectangle(Point(508-x_shift, 240+y_shift), Point(546-x_shift, 252+y_shift))
    stripe_1.setFill(secondary_color)
    stripe_1.setOutline(secondary_color)
    stripe_1.draw(winOne)

    stripe_2 = Rectangle(Point(552-x_shift, 212+y_shift+60), Point(565-x_shift, 221+y_shift+60))
    stripe_2.setFill(secondary_color)
    stripe_2.setOutline(secondary_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(582-x_shift, 240+y_shift), Point(592-x_shift, 249+y_shift))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    stripe_4 = Polygon(Point(544-x_shift, 263+y_shift), Point(550-x_shift, 267+y_shift), Point(548-x_shift, 271+y_shift), Point(540-x_shift, 266+y_shift))
    stripe_4.setFill(secondary_color)
    stripe_4.setOutline(secondary_color)
    stripe_4.draw(winOne)

    stripe_5 = Polygon(Point(568-x_shift, 267+y_shift), Point(575-x_shift, 263+y_shift), Point(578-x_shift, 265+y_shift), Point(570-x_shift, 271+y_shift))
    stripe_5.setFill(secondary_color)
    stripe_5.setOutline(secondary_color)
    stripe_5.draw(winOne)

    cannon_base = Rectangle(Point(553-x_shift, 240+y_shift), Point(564-x_shift, 252+y_shift))
    cannon_base.setFill(secondary_color)
    cannon_base.setOutline(secondary_color)
    cannon_base.draw(winOne)

    left_cannon = Rectangle(Point(555-x_shift, 251+y_shift - 24), Point(556-x_shift, 265+y_shift - 24))
    right_cannon = Rectangle(Point(562-x_shift, 251+y_shift - 24), Point(563-x_shift, 265+y_shift - 24))
    left_cannon.setFill(secondary_color)
    left_cannon.setOutline(secondary_color)
    right_cannon.setFill(secondary_color)
    right_cannon.setOutline(secondary_color)
    left_cannon.draw(winOne)
    right_cannon.draw(winOne)

    return[outrider_window, outrider_body, outrider_end, outline_1, outline_2,
           connector, thruster_1, thruster_2, stripe_1, stripe_2, stripe_3, stripe_4,
           stripe_5, cannon_base, left_cannon, right_cannon]


# setting function to draw x-wing in launching perspective
def xwing_s2_p2(winOne):
    main_color = color_rgb(192, 192, 192)
    stripe_color = color_rgb(255, 160, 122)
    secondary_color = color_rgb(128, 128, 128)

    y_shift = 115

    xwing_back = Oval(Point(300, 321+y_shift), Point(334, 332+y_shift))
    xwing_back.setFill(main_color)
    xwing_back.setOutline(main_color)
    xwing_back.draw(winOne)
    
    xwing_body = Rectangle(Point(290, 311+y_shift), Point(344, 326+y_shift))
    xwing_body.setFill(main_color)
    xwing_body.setOutline(main_color)
    xwing_body.draw(winOne)

    xwing_control = Rectangle(Point(312, 306+y_shift), Point(321, 335+y_shift))
    xwing_control.setFill(main_color)
    xwing_control.setOutline(main_color)
    xwing_control.draw(winOne)

    xwing_front = Rectangle(Point(315, 306+y_shift), Point(317, 250+y_shift))
    xwing_front.setFill(main_color)
    xwing_front.setOutline(main_color)
    xwing_front.draw(winOne)
    
    stripe_1 = Line(Point(315, 305+y_shift), Point(315, 265+y_shift))
    stripe_1.setOutline(stripe_color)
    stripe_1.draw(winOne)

    stripe_2 = Line(Point(317, 305+y_shift), Point(317, 265+y_shift))
    stripe_2.setOutline(stripe_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(314, 311+y_shift), Point(318, 333+y_shift))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    engine_1 = Rectangle(Point(306, 306+y_shift), Point(311, 324+y_shift))
    engine_1.setFill(secondary_color)
    engine_1.setOutline(secondary_color)
    engine_1.draw(winOne)

    engine_2 = Rectangle(Point(321, 306+y_shift), Point(326, 324+y_shift))
    engine_2.setFill(secondary_color)
    engine_2.setOutline(secondary_color)
    engine_2.draw(winOne)

    stripe_4 = Rectangle(Point(292, 313+y_shift), Point(295, 325+y_shift))
    stripe_5 = Rectangle(Point(338, 313+y_shift), Point(341, 325+y_shift))
    stripe_4.setFill(stripe_color)
    stripe_4.setOutline(stripe_color)
    stripe_5.setFill(stripe_color)
    stripe_5.setOutline(stripe_color)
    stripe_4.draw(winOne)
    stripe_5.draw(winOne)

    right_cannon = Rectangle(Point(344, 308+y_shift), Point(344, 271+y_shift))
    right_cannon.setFill(main_color)
    right_cannon.setOutline(main_color)
    right_cannon.draw(winOne)

    left_cannon = Rectangle(Point(288, 308+y_shift), Point(288, 271+y_shift))
    left_cannon.setFill(main_color)
    left_cannon.setOutline(main_color)
    left_cannon.draw(winOne)

    left_wing = Rectangle(Point(288, 306+y_shift), Point(291, 326+y_shift))
    left_wing.setFill(secondary_color)
    left_wing.setOutline(secondary_color)
    left_wing.draw(winOne)

    right_wing = Rectangle(Point(342, 306+y_shift), Point(345, 326+y_shift))
    right_wing.setFill(secondary_color)
    right_wing.setOutline(secondary_color)
    right_wing.draw(winOne)

    thruster_1 = Rectangle(Point(306, 342+y_shift), Point(309, 328+y_shift))
    thruster_1.setFill(main_color)
    thruster_1.setOutline(main_color)
    thruster_1.draw(winOne)

    thruster_2 = Rectangle(Point(324, 342+y_shift), Point(327, 328+y_shift))
    thruster_2.setFill(main_color)
    thruster_2.setOutline(main_color)
    thruster_2.draw(winOne)

    return[xwing_back, xwing_body, xwing_control, xwing_front, stripe_1, stripe_2, stripe_3, 
        engine_1, engine_2, stripe_4, stripe_5,
        left_wing, right_wing, right_cannon, left_cannon, thruster_1, thruster_2]


# setting function to draw TIE fighters in launching perspective
def fighters_s2_p2(winOne):
    main_color = color_rgb(192, 192, 192)
    secondary_color = color_rgb(128, 128, 128)
    third_color = color_rgb(169, 169, 169)

    y_shift = 90
    connector = Rectangle(Point(296, 306+y_shift), Point(337, 313+y_shift))
    connector.setFill(main_color)
    connector.setOutline(main_color)
    connector.draw(winOne)

    connector_base_1 = Polygon(Point(288, 303+y_shift), Point(296, 305+y_shift), Point(296, 314+y_shift), Point(288, 317+y_shift))
    connector_base_1.setFill(third_color)
    connector_base_1.setOutline(third_color)
    connector_base_1.draw(winOne)

    connector_base_2 = Polygon(Point(337, 305+y_shift), Point(345, 303+y_shift), Point(345, 316+y_shift), Point(337, 314+y_shift))
    connector_base_2.setFill(third_color)
    connector_base_2.setOutline(third_color)
    connector_base_2.draw(winOne)
    
    body = Oval(Point(306, 298+y_shift), Point(329, 326+y_shift))
    body.setFill(main_color)
    body.setOutline(main_color)
    body.draw(winOne)

    left_wing = Rectangle(Point(284, 276+y_shift), Point(288, 342+y_shift))
    left_wing.setFill(secondary_color)
    left_wing.setOutline(secondary_color)
    left_wing.draw(winOne)

    right_wing = Rectangle(Point(345, 276+y_shift), Point(349, 342+y_shift))
    right_wing.setFill(secondary_color)
    right_wing.setOutline(secondary_color)
    right_wing.draw(winOne)

    stripe_1 = Oval(Point(310, 302+y_shift), Point(325, 320+y_shift))
    stripe_1.setFill(third_color)
    stripe_1.setOutline(third_color)
    stripe_1.draw(winOne)

    front = Rectangle(Point(312, 296+y_shift), Point(323, 299+y_shift))
    front.setFill(main_color)
    front.setOutline(main_color)
    front.draw(winOne)

    stripe_2 = Rectangle(Point(312, 307+y_shift), Point(313, 311+y_shift))
    stripe_2.setFill(secondary_color)
    stripe_2.setOutline(secondary_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(315, 303+y_shift), Point(316, 310+y_shift))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    stripe_4 = Rectangle(Point(318, 304+y_shift), Point(319, 310+y_shift))
    stripe_4.setFill(secondary_color)
    stripe_4.setOutline(secondary_color)
    stripe_4.draw(winOne)

    stripe_5 = Rectangle(Point(321, 305+y_shift), Point(322, 311+y_shift))
    stripe_5.setFill(secondary_color)
    stripe_5.setOutline(secondary_color)
    stripe_5.draw(winOne)

    stripe_6 = Rectangle(Point(297, 309+y_shift), Point(307, 311+y_shift))
    stripe_6.setFill(third_color)
    stripe_6.setOutline(third_color)
    stripe_6.draw(winOne)

    stripe_7 = Rectangle(Point(326, 309+y_shift), Point(336, 311+y_shift))
    stripe_7.setFill(third_color)
    stripe_7.setOutline(third_color)
    stripe_7.draw(winOne)

    return[connector, body, left_wing, right_wing, connector_base_1, connector_base_2,
           stripe_1, front, stripe_2, stripe_3,
           stripe_4, stripe_5, stripe_6, stripe_7]


# setting function to draw TIE bombers in launching perspective
def bombers_s2_p2(winOne):
    main = color_rgb(192, 192, 192)
    secondary = color_rgb(0, 0, 0)
    third = color_rgb(169, 169, 169)
    fourth = color_rgb(75, 75, 75)

    # can help re-adjust shapes positions
    y_shift = 100
    
    left_body = Polygon(Point(293, 289+y_shift), Point(294, 285+y_shift), Point(310, 285+y_shift),
                        Point(312, 287+y_shift), Point(312, 331+y_shift), Point(310, 334+y_shift), Point(295, 334+y_shift), Point(293, 332+y_shift))

    left_body.setFill(main)
    left_body.setOutline(main)
    left_body.draw(winOne)

    right_body = Polygon(Point(318, 287+y_shift), Point(321, 280+y_shift), Point(334, 280+y_shift), Point(337, 285+y_shift),
                         Point(337, 333+y_shift), Point(335, 334+y_shift), Point(320, 334+y_shift), Point(318, 332+y_shift))

    right_body.setFill(main)
    right_body.setOutline(main)
    right_body.draw(winOne)

    connector = Rectangle(Point(307, 294+y_shift), Point(319, 304+y_shift))
    connector.setFill(third)
    connector.setOutline(third)
    connector.draw(winOne)

    left_wing = Polygon(Point(280, 269+y_shift), Point(292, 272+y_shift), Point(292, 348+y_shift), Point(280, 351+y_shift))
    left_wing.setFill(fourth)
    left_wing.draw(winOne)

    right_wing = Polygon(Point(338, 271+y_shift), Point(349, 268+y_shift), Point(349, 351+y_shift), Point(338, 347+y_shift))
    right_wing.setFill(fourth)
    right_wing.draw(winOne)

    front = Rectangle(Point(321, 280+y_shift), Point(335, 276+y_shift))
    front.setFill(third)
    front.setOutline(third)
    front.draw(winOne)

    stripe_1 = Rectangle(Point(296, 298+y_shift), Point(297, 326+y_shift))
    stripe_1.setFill(third)
    stripe_1.setOutline(third)
    stripe_1.draw(winOne)

    stripe_2 = Rectangle(Point(305, 298+y_shift), Point(306, 326+y_shift))
    stripe_2.setFill(third)
    stripe_2.setOutline(third)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(322, 304+y_shift), Point(334, 328+y_shift))
    stripe_3.setFill(third)
    stripe_3.setOutline(third)
    stripe_3.draw(winOne)

    stripe_4 = Oval(Point(321, 285+y_shift), Point(335, 300+y_shift))
    stripe_4.setFill(third)
    stripe_4.setOutline(third)
    stripe_4.draw(winOne)

    stripe_5 = Rectangle(Point(283, 298+y_shift), Point(290, 342+y_shift))
    stripe_5.setFill(secondary)
    stripe_5.draw(winOne)

    stripe_6 = Polygon(Point(283, 272+y_shift), Point(290, 277+y_shift), Point(290, 290+y_shift), Point(283, 290+y_shift))
    stripe_6.setFill(secondary)
    stripe_6.draw(winOne)

    stripe_7 = Rectangle(Point(340, 298+y_shift), Point(347, 344+y_shift))
    stripe_7.setFill(secondary)
    stripe_7.draw(winOne)

    stripe_8 = Polygon(Point(340, 277+y_shift), Point(347, 272+y_shift), Point(347, 290+y_shift), Point(340, 290+y_shift))
    stripe_8.setFill(secondary)
    stripe_8.draw(winOne)

    return[left_body, right_body, connector, left_wing, right_wing, front, stripe_1, stripe_2,
           stripe_3, stripe_4, stripe_5, stripe_6, stripe_7, stripe_8]


# setting funtion that executes all comands located in scene 2
def scene_two():
    winTwo = GraphWin("Scene two", 640, 360)
    winTwo.setBackground(color_rgb(0, 0, 0))

    draw_stars(winTwo)

    # setting function to draw the left side of the double sliding doors in scene 2
    frame_color = color_rgb(95, 95, 95)
    bottom_color = color_rgb(255, 255, 255)

    left_upper = Rectangle(Point(0, 0), Point(320, 36))
    left_upper.setFill(frame_color)
    left_upper.setOutline(frame_color)
    left_upper.draw(winTwo)
    
    left_connector = Rectangle(Point(317, 36), Point(320, 360))
    left_connector.setFill(frame_color)
    left_connector.setOutline(frame_color)
    left_connector.draw(winTwo)

    left_lower = Rectangle(Point(0, 95), Point(320, 127))
    left_lower.setFill(frame_color)
    left_lower.setOutline(frame_color)
    left_lower.draw(winTwo)

    left_bottom = Rectangle(Point(0, 127), Point(320, 129))
    left_bottom.setFill(bottom_color)
    left_bottom.setOutline(bottom_color)



    # setting function to draw the right side of the double sliding doors in scene 2  
    right_upper = Rectangle(Point(320, 0), Point(640, 36))
    right_upper.setFill(frame_color)
    right_upper.setOutline(frame_color)
    right_upper.draw(winTwo)
      
    right_connector = Rectangle(Point(320, 36), Point(323, 360))
    right_connector.setFill(frame_color)
    right_connector.setOutline(frame_color)
    right_connector.draw(winTwo)

    right_lower = Rectangle(Point(320, 95), Point(640, 127))
    right_lower.setFill(frame_color)
    right_lower.setOutline(frame_color)
    right_lower.draw(winTwo)

    right_bottom = Rectangle(Point(320, 127), Point(640, 129))
    right_bottom.setFill(bottom_color)
    right_bottom.setOutline(bottom_color)

    
    # draw spaceship's floor
    floor_parts = draw_floor(winTwo)

    runway_parts = draw_runway_s2(winTwo)
    left_lights = runway_left_lights(winTwo)
    right_lights = runway_right_lights(winTwo)
    markings = runway_markings(winTwo)

    left_bottom.draw(winTwo)
    right_bottom.draw(winTwo)

    # draw parking slots
    left_parking = left_parking_s2(winTwo)
    right_parking = right_parking_s2(winTwo)

    light_color = color_rgb(0, 255, 0)
    light_off = color_rgb(255, 0, 0)
    light_radius = 8
    
    parking_light_1 = Circle(Point(416, 173), light_radius - 1)
    parking_light_1.setFill(light_color)
    parking_light_1.draw(winTwo)

    parking_light_2 = Circle(Point(437, 285), light_radius)
    parking_light_2.setFill(light_color)
    parking_light_2.draw(winTwo)

    parking_light_3 = Circle(Point(215, 162), light_radius - 2)
    parking_light_3.setFill(light_color)
    parking_light_3.draw(winTwo)

    parking_light_4 = Circle(Point(193, 232), light_radius - 1)
    parking_light_4.setFill(light_color)
    parking_light_4.draw(winTwo)

    parking_light_5 = Circle(Point(167, 310), light_radius)
    parking_light_5.setFill(light_color)
    parking_light_5.draw(winTwo)

    # setting if, elif conditions to determine which spacecraft the user chose
    # and turn off the corresponding parking light
    
    if chosen_spacecraft == "1":
        outrider_p1 = outrider_s2_p1(winTwo)
        xwing_p1 = xwing_s2_p1(winTwo)
        fighters_p1 = fighters_s2_p1(winTwo)
        bombers_p1 = bombers_s2_p1(winTwo)
        falcon_p2 = falcon_s2_p2(winTwo)
        
        parking_light_1.undraw()
        parking_light_1.setFill(light_off)
        parking_light_1.draw(winTwo)
        
        launching_position = 253
        vertex = 364


    elif chosen_spacecraft == "2":
        falcon_p1 = falcon_s2_p1(winTwo)
        xwing_p1 = xwing_s2_p1(winTwo)
        fighters_p1 = fighters_s2_p1(winTwo)
        bombers_p1 = bombers_s2_p1(winTwo)
        outrider_p2 = outrider_s2_p2(winTwo)
        
        parking_light_2.undraw()
        parking_light_2.setFill(light_off)
        parking_light_2.draw(winTwo)
        
        launching_position = 271
        vertex = 365

    elif chosen_spacecraft == "3":
        falcon_p1 = falcon_s2_p1(winTwo)
        outrider_p1 = outrider_s2_p1(winTwo)      
        fighters_p1 = fighters_s2_p1(winTwo)
        bombers_p1 = bombers_s2_p1(winTwo)
        xwing_p2 = xwing_s2_p2(winTwo)
        
        parking_light_3.undraw()
        parking_light_3.setFill(light_off)
        parking_light_3.draw(winTwo)
        
        launching_position = 263
        vertex = 365
        
        
    elif chosen_spacecraft == "4":
        falcon_p1 = falcon_s2_p1(winTwo)
        outrider_p1 = outrider_s2_p1(winTwo)
        xwing_p1 = xwing_s2_p1(winTwo)
        bombers_p1 = bombers_s2_p1(winTwo)
        fighters_p2 = fighters_s2_p2(winTwo)
        
        parking_light_4.undraw()
        parking_light_4.setFill(light_off)
        parking_light_4.draw(winTwo)
        
        launching_position = 281
        vertex = 366
        

    elif chosen_spacecraft == "5":
        falcon_p1 = falcon_s2_p1(winTwo)
        outrider_p1 = outrider_s2_p1(winTwo)
        xwing_p1 = xwing_s2_p1(winTwo)
        fighters_p1 = fighters_s2_p1(winTwo)
        bombers_p2 = bombers_s2_p2(winTwo)
        
        parking_light_5.undraw()
        parking_light_5.setFill(light_off)
        parking_light_5.draw(winTwo)
        
        launching_position = 268
        vertex = 369

    # setting while loop to allow the chosen spacecraft to move into launching position
    vert_displacement = -1
    if chosen_spacecraft == "1":
        while vertex > launching_position:
            for parts in falcon_p2:
                parts.move(0, vert_displacement)
            vertex += vert_displacement
            time.sleep(0.05)
    
    elif chosen_spacecraft == "2":
        while vertex > launching_position:
            for parts in outrider_p2:
                parts.move(0, vert_displacement)
            vertex += vert_displacement
            time.sleep(0.05)
            
    elif chosen_spacecraft == "3":
        while vertex > launching_position:
            for parts in xwing_p2:
                parts.move(0, vert_displacement)
            vertex += vert_displacement
            time.sleep(0.05)

    elif chosen_spacecraft == "4":
        while vertex > launching_position:
            for parts in fighters_p2:
                parts.move(0, vert_displacement)
            vertex += vert_displacement
            time.sleep(0.05)
            
    elif chosen_spacecraft == "5":
        while vertex > launching_position:
            for parts in bombers_p2:
                parts.move(0, vert_displacement)
            vertex += vert_displacement
            time.sleep(0.05)

    # drawing the message that asks the user to press B key to launch the spacecraft
    launch_box = Rectangle(Point(265, 217), Point(380, 251))
    launch_box.setFill(color_rgb(255, 218, 185))
    launch_box.draw(winTwo)

    launch_text = Text(Point(321, 233), "Press B to launch")
    launch_text.setSize(9)
    launch_text.setStyle("bold")
    launch_text.draw(winTwo)
    

    # adding all parts in the left into one list except for door and user's spacecraft
    # adding all right side parts into one list except for door and user's spacecraft

    if chosen_spacecraft == "1":
        move_all_right = outrider_p1
        move_all_left = xwing_p1 + fighters_p1 + bombers_p1 

    elif chosen_spacecraft == "2":
        move_all_right = falcon_p1
        move_all_left = xwing_p1 + fighters_p1 + bombers_p1

    elif chosen_spacecraft == "3":
        move_all_right = falcon_p1 + outrider_p1
        move_all_left = fighters_p1 + bombers_p1

    elif chosen_spacecraft == "4":
        move_all_right = falcon_p1 + outrider_p1
        move_all_left = xwing_p1 + bombers_p1 

    elif chosen_spacecraft == "5":
        move_all_right = falcon_p1 + outrider_p1
        move_all_left = xwing_p1 + fighters_p1 

    for x in left_parking:
        move_all_left.append(x)

    for y in right_parking:
        move_all_right.append(y)
        

    # setting while loops such that when user presses B, the spacecraft will launch
    while True:
            launch_input = winTwo.getKey()
            launch_input = launch_input.lower()
            if launch_input == "b":
                launch_box.undraw()
                launch_text.undraw()
                break

    y_shift = 4
    x_shift = 1
    vertex_all = 0
    runway_light_movement = x_shift/2

    MAX_X = 640
    MAX_Y = 360


    while vertex_all <= MAX_Y:

        left_upper.move(-4, 0)
        left_connector.move(-4, 0)
        left_lower.move(-4, y_shift)
        left_bottom.move(-4, y_shift)
        
        right_upper.move(4, 0)
        right_connector.move(4, 0)
        right_lower.move(4, y_shift)
        right_bottom.move(4, y_shift)

        
        # In order to look like the spacecrat is moving, everything on the left side will slant downwards toward the left
        # whereas everything on the right slants downwards toward the right
        for right_parts in move_all_right:
            right_parts.move(x_shift, y_shift)

        for left_parts in move_all_left:
            left_parts.move(x_shift * -1, y_shift)

        for x in left_lights:
            x.move(runway_light_movement * -1, y_shift)

        for y in right_lights:
            y.move(runway_light_movement, y_shift)

        for runway in runway_parts:
            runway.move(0, y_shift)

        for floor in floor_parts:
            floor.move(0, y_shift)

        for parts in markings:
            parts.move(0, y_shift*2)
        
        parking_light_1.move(x_shift, y_shift)
        parking_light_2.move(x_shift, y_shift) 
        parking_light_3.move(x_shift * -1, y_shift)  
        parking_light_4.move(x_shift * -1, y_shift)
        parking_light_5.move(x_shift * -1, y_shift) 

        vertex_all += y_shift

    # setting conditions to move the chosen spacecraft out of scene
    if chosen_spacecraft == "1":
        for falcon in range(180):
            for parts in falcon_p2:
                parts.move(0, -2)

            time.sleep(0.01)

    elif chosen_spacecraft == "2":
        for outrider in range(180):
            for parts in outrider_p2:
                parts.move(0, -2)

            time.sleep(0.01)
            
    elif chosen_spacecraft == "3":
        for xwing in range(180):
            for parts in xwing_p2:
                parts.move(0, -2)

            time.sleep(0.01)

    elif chosen_spacecraft == "4":
        for fighters in range(180):
            for parts in fighters_p2:
                parts.move(0, -2)

            time.sleep(0.01)

    elif chosen_spacecraft == "5":
        for bombers in range(180):
            for parts in bombers_p2:
                parts.move(0, -2)

            time.sleep(0.01)

    winTwo.close()


# setting function to draw user's millennium falcon
def falcon_s3(winOne):
    # x shift and y_shift helps to adjust shape position in the right place
    x_shift = 8
    y_shift = -230
    
    body_color = color_rgb(192, 192, 192)
    wing_color = color_rgb(128, 128, 128)
    outline = color_rgb(105, 105, 105)

    thruster = Oval(Point(359, 360+y_shift), Point(278, 329+y_shift))
    thruster.setFill(color_rgb(224, 255, 255))
    thruster.setOutline(color_rgb(0, 255, 255))
    thruster.draw(winOne)
    
    body = Oval(Point(266, 284+y_shift), Point(370, 356+y_shift))
    body.setFill(body_color)
    body.setOutline(body_color)
    body.draw(winOne)

    right_control = Polygon(Point(347+x_shift, 294+y_shift), Point(323+x_shift, 255+y_shift), Point(317+x_shift, 255+y_shift), Point(317+x_shift, 294+y_shift))
    right_control.setFill(body_color)
    right_control.setOutline(body_color)
    right_control.draw(winOne)

    left_control = Polygon(Point(265+x_shift, 301+y_shift), Point(301+x_shift, 255+y_shift), Point(306+x_shift, 255+y_shift), Point(305+x_shift, 301+y_shift))
    left_control.setFill(body_color)
    left_control.setOutline(body_color)
    left_control.draw(winOne)
    
    wing = Polygon(Point(319+x_shift, 302+y_shift), Point(334+x_shift, 316+y_shift), Point(378+x_shift, 297+y_shift),
                   Point(370+x_shift, 278+y_shift), Point(344+x_shift, 281+y_shift), Point(348+x_shift, 290+y_shift))
    
    wing.setFill(wing_color)
    wing.setOutline(wing_color)
    wing.draw(winOne)

    wing_line = Polygon(Point(332+x_shift, 305+y_shift), Point(332+x_shift, 307+y_shift), Point(364+x_shift, 293+y_shift), Point(362+x_shift, 292+y_shift))
    wing_line.setFill(outline)
    wing_line.setOutline(outline)
    wing_line.draw(winOne)

    vent_radius = 5
    
    vent_one = Circle(Point(295+x_shift, 323+y_shift), vent_radius)
    vent_two = Circle(Point(310+x_shift, 328+y_shift), vent_radius)
    vent_three = Circle(Point(323+x_shift, 322+y_shift), vent_radius)
    vent_four = Circle(Point(323+x_shift, 335+y_shift), vent_radius)
    vent_five = Circle(Point(310+x_shift, 342+y_shift), vent_radius)
    vent_six = Circle(Point(295+x_shift, 336+y_shift), vent_radius)

    vent_one.setFill(wing_color)
    vent_one.setOutline(outline)
    vent_one.draw(winOne)

    vent_two.setFill(wing_color)
    vent_two.setOutline(outline)
    vent_two.draw(winOne)

    vent_three.setFill(wing_color)
    vent_three.setOutline(outline)
    vent_three.draw(winOne)

    vent_four.setFill(wing_color)
    vent_four.setOutline(outline)
    vent_four.draw(winOne)
    
    vent_five.setFill(wing_color)
    vent_five.setOutline(outline)
    vent_five.draw(winOne)

    vent_six.setFill(wing_color)
    vent_six.setOutline(outline)
    vent_six.draw(winOne)

    cannon = Rectangle(Point(258+x_shift, 312+y_shift), Point(288+x_shift, 319+y_shift))
    cannon.setFill(wing_color)
    cannon.setOutline(wing_color)
    cannon.draw(winOne)

    front_cannon = Rectangle(Point(301+x_shift, 278+y_shift), Point(320+x_shift, 309+y_shift))
    front_cannon.setFill(wing_color)
    front_cannon.setOutline(wing_color)
    front_cannon.draw(winOne)

    left_win = Polygon(Point(289, 277+y_shift), Point(292, 280+y_shift), Point(303, 267+y_shift), Point(301, 262+y_shift))
    left_win.setFill(wing_color)
    left_win.setOutline(wing_color)
    left_win.draw(winOne)

    right_win = Polygon(Point(324+x_shift, 261+y_shift), Point(334+x_shift, 277+y_shift), Point(338+x_shift, 277+y_shift), Point(328+x_shift, 260+y_shift))
    right_win.setFill(wing_color)
    right_win.setOutline(wing_color)
    right_win.draw(winOne)

    return[body, wing, wing_line, vent_one, vent_two, vent_three, vent_four, vent_five,
           vent_six, cannon, front_cannon, right_control, left_control, left_win, right_win, thruster]


# setting function to draw user's outrider
def outrider_s3(winOne):
    # x and y shift helps adjust the shapes into correct position
    x_shift = 239
    y_shift = 53 - 230
    main_color = color_rgb(192, 192, 192)
    secondary_color = color_rgb(128, 128, 128)
    third_color = color_rgb(105, 105, 105)

    outrider_center = Point(559-x_shift, 247+y_shift)

    outrider_window = Oval(Point(550-x_shift, 209+y_shift+67), Point(566-x_shift, 217+y_shift+67))
    outrider_window.setFill(color_rgb(224, 255, 255))
    outrider_window.setOutline(color_rgb(224, 255, 255))
    outrider_window.draw(winOne)
    
    outrider_body = Oval(Point(525-x_shift, 212+y_shift), Point(592-x_shift, 281+y_shift))
    outrider_body.setFill(main_color)
    outrider_body.setOutline(main_color)
    outrider_body.draw(winOne)

    outrider_end = Polygon(Point(536-x_shift, 225+y_shift), Point(494-x_shift, 234+y_shift), Point(500-x_shift, 266+y_shift), Point(547-x_shift, 279+y_shift))
    outrider_end.setFill(main_color)
    outrider_end.setOutline(main_color)
    outrider_end.draw(winOne)

    outline_1 = Circle(outrider_center, 26)
    outline_1.setFill(main_color)
    outline_1.draw(winOne)

    outline_2 = Circle(outrider_center, 12)
    outline_2.setFill(main_color)
    outline_2.draw(winOne)

    connector = Polygon(Point(490-x_shift, 251+y_shift), Point(503-x_shift, 251+y_shift), Point(502-x_shift, 256+y_shift), Point(492-x_shift, 256+y_shift))
    connector.setFill(third_color)
    connector.setOutline(third_color)
    connector.draw(winOne)

    thruster_1 = Rectangle(Point(486-x_shift, 216+y_shift), Point(507-x_shift, 251+y_shift))
    thruster_1.setFill(secondary_color)
    thruster_1.setOutline(secondary_color)
    thruster_1.draw(winOne)

    thruster_2 = Polygon(Point(486-x_shift, 256+y_shift), Point(486-x_shift, 278+y_shift), Point(489-x_shift, 286+y_shift), Point(505-x_shift, 286+y_shift),
                         Point(507-x_shift, 278+y_shift), Point(506-x_shift, 256+y_shift))
    thruster_2.setFill(secondary_color)
    thruster_2.setOutline(secondary_color)
    thruster_2.draw(winOne)

    stripe_1 = Rectangle(Point(508-x_shift, 240+y_shift), Point(546-x_shift, 252+y_shift))
    stripe_1.setFill(secondary_color)
    stripe_1.setOutline(secondary_color)
    stripe_1.draw(winOne)

    stripe_2 = Rectangle(Point(552-x_shift, 212+y_shift+60), Point(565-x_shift, 221+y_shift+60))
    stripe_2.setFill(secondary_color)
    stripe_2.setOutline(secondary_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(582-x_shift, 240+y_shift), Point(592-x_shift, 249+y_shift))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    stripe_4 = Polygon(Point(544-x_shift, 263+y_shift), Point(550-x_shift, 267+y_shift), Point(548-x_shift, 271+y_shift), Point(540-x_shift, 266+y_shift))
    stripe_4.setFill(secondary_color)
    stripe_4.setOutline(secondary_color)
    stripe_4.draw(winOne)

    stripe_5 = Polygon(Point(568-x_shift, 267+y_shift), Point(575-x_shift, 263+y_shift), Point(578-x_shift, 265+y_shift), Point(570-x_shift, 271+y_shift))
    stripe_5.setFill(secondary_color)
    stripe_5.setOutline(secondary_color)
    stripe_5.draw(winOne)

    cannon_base = Rectangle(Point(553-x_shift, 240+y_shift), Point(564-x_shift, 252+y_shift))
    cannon_base.setFill(secondary_color)
    cannon_base.setOutline(secondary_color)
    cannon_base.draw(winOne)

    left_cannon = Rectangle(Point(555-x_shift, 251+y_shift - 24), Point(556-x_shift, 265+y_shift - 24))
    right_cannon = Rectangle(Point(562-x_shift, 251+y_shift - 24), Point(563-x_shift, 265+y_shift - 24))
    left_cannon.setFill(secondary_color)
    left_cannon.setOutline(secondary_color)
    right_cannon.setFill(secondary_color)
    right_cannon.setOutline(secondary_color)
    left_cannon.draw(winOne)
    right_cannon.draw(winOne)

    return[outrider_window, outrider_body, outrider_end, outline_1, outline_2,
           connector, thruster_1, thruster_2, stripe_1, stripe_2, stripe_3, stripe_4,
           stripe_5, cannon_base, left_cannon, right_cannon]


# setting function to draw user's xwing 
def xwing_s3(winOne):
    main_color = color_rgb(192, 192, 192)
    stripe_color = color_rgb(255, 160, 122)
    secondary_color = color_rgb(128, 128, 128)

    # y shift helps with shapes re-adjustments
    y_shift = -230

    xwing_back = Oval(Point(300, 321+y_shift), Point(334, 332+y_shift))
    xwing_back.setFill(main_color)
    xwing_back.setOutline(main_color)
    xwing_back.draw(winOne)
    
    xwing_body = Rectangle(Point(290, 311+y_shift), Point(344, 326+y_shift))
    xwing_body.setFill(main_color)
    xwing_body.setOutline(main_color)
    xwing_body.draw(winOne)

    xwing_control = Rectangle(Point(312, 306+y_shift), Point(321, 335+y_shift))
    xwing_control.setFill(main_color)
    xwing_control.setOutline(main_color)
    xwing_control.draw(winOne)

    xwing_front = Rectangle(Point(315, 306+y_shift), Point(317, 250+y_shift))
    xwing_front.setFill(main_color)
    xwing_front.setOutline(main_color)
    xwing_front.draw(winOne)
    
    stripe_1 = Line(Point(315, 305+y_shift), Point(315, 265+y_shift))
    stripe_1.setOutline(stripe_color)
    stripe_1.draw(winOne)

    stripe_2 = Line(Point(317, 305+y_shift), Point(317, 265+y_shift))
    stripe_2.setOutline(stripe_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(314, 311+y_shift), Point(318, 333+y_shift))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    engine_1 = Rectangle(Point(306, 306+y_shift), Point(311, 324+y_shift))
    engine_1.setFill(secondary_color)
    engine_1.setOutline(secondary_color)
    engine_1.draw(winOne)

    engine_2 = Rectangle(Point(321, 306+y_shift), Point(326, 324+y_shift))
    engine_2.setFill(secondary_color)
    engine_2.setOutline(secondary_color)
    engine_2.draw(winOne)

    stripe_4 = Rectangle(Point(292, 313+y_shift), Point(295, 325+y_shift))
    stripe_5 = Rectangle(Point(338, 313+y_shift), Point(341, 325+y_shift))
    stripe_4.setFill(stripe_color)
    stripe_4.setOutline(stripe_color)
    stripe_5.setFill(stripe_color)
    stripe_5.setOutline(stripe_color)
    stripe_4.draw(winOne)
    stripe_5.draw(winOne)

    right_cannon = Rectangle(Point(344, 308+y_shift), Point(344, 271+y_shift))
    right_cannon.setFill(main_color)
    right_cannon.setOutline(main_color)
    right_cannon.draw(winOne)

    left_cannon = Rectangle(Point(288, 308+y_shift), Point(288, 271+y_shift))
    left_cannon.setFill(main_color)
    left_cannon.setOutline(main_color)
    left_cannon.draw(winOne)

    left_wing = Rectangle(Point(288, 306+y_shift), Point(291, 326+y_shift))
    left_wing.setFill(secondary_color)
    left_wing.setOutline(secondary_color)
    left_wing.draw(winOne)

    right_wing = Rectangle(Point(342, 306+y_shift), Point(345, 326+y_shift))
    right_wing.setFill(secondary_color)
    right_wing.setOutline(secondary_color)
    right_wing.draw(winOne)

    thruster_1 = Rectangle(Point(306, 342+y_shift), Point(309, 328+y_shift))
    thruster_1.setFill(main_color)
    thruster_1.setOutline(main_color)
    thruster_1.draw(winOne)

    thruster_2 = Rectangle(Point(324, 342+y_shift), Point(327, 328+y_shift))
    thruster_2.setFill(main_color)
    thruster_2.setOutline(main_color)
    thruster_2.draw(winOne)

    return[xwing_back, xwing_body, xwing_control, xwing_front, stripe_1, stripe_2, stripe_3, 
        engine_1, engine_2, stripe_4, stripe_5,
        left_wing, right_wing, right_cannon, left_cannon, thruster_1, thruster_2]


# setting function to draw user's TIE fighter
def fighters_s3(winOne):
    main_color = color_rgb(192, 192, 192)
    secondary_color = color_rgb(128, 128, 128)
    third_color = color_rgb(169, 169, 169)

    # y shift helps to adjust shapes positions
    y_shift = -230
    
    connector = Rectangle(Point(296, 306+y_shift), Point(337, 313+y_shift))
    connector.setFill(main_color)
    connector.setOutline(main_color)
    connector.draw(winOne)

    connector_base_1 = Polygon(Point(288, 303+y_shift), Point(296, 305+y_shift), Point(296, 314+y_shift), Point(288, 317+y_shift))
    connector_base_1.setFill(third_color)
    connector_base_1.setOutline(third_color)
    connector_base_1.draw(winOne)

    connector_base_2 = Polygon(Point(337, 305+y_shift), Point(345, 303+y_shift), Point(345, 316+y_shift), Point(337, 314+y_shift))
    connector_base_2.setFill(third_color)
    connector_base_2.setOutline(third_color)
    connector_base_2.draw(winOne)
    
    body = Oval(Point(306, 298+y_shift), Point(329, 326+y_shift))
    body.setFill(main_color)
    body.setOutline(main_color)
    body.draw(winOne)

    left_wing = Rectangle(Point(284, 276+y_shift), Point(288, 342+y_shift))
    left_wing.setFill(secondary_color)
    left_wing.setOutline(secondary_color)
    left_wing.draw(winOne)

    right_wing = Rectangle(Point(345, 276+y_shift), Point(349, 342+y_shift))
    right_wing.setFill(secondary_color)
    right_wing.setOutline(secondary_color)
    right_wing.draw(winOne)

    stripe_1 = Oval(Point(310, 302+y_shift), Point(325, 320+y_shift))
    stripe_1.setFill(third_color)
    stripe_1.setOutline(third_color)
    stripe_1.draw(winOne)

    front = Rectangle(Point(312, 296+y_shift), Point(323, 299+y_shift))
    front.setFill(main_color)
    front.setOutline(main_color)
    front.draw(winOne)

    stripe_2 = Rectangle(Point(312, 307+y_shift), Point(313, 311+y_shift))
    stripe_2.setFill(secondary_color)
    stripe_2.setOutline(secondary_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(315, 303+y_shift), Point(316, 310+y_shift))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    stripe_4 = Rectangle(Point(318, 304+y_shift), Point(319, 310+y_shift))
    stripe_4.setFill(secondary_color)
    stripe_4.setOutline(secondary_color)
    stripe_4.draw(winOne)

    stripe_5 = Rectangle(Point(321, 305+y_shift), Point(322, 311+y_shift))
    stripe_5.setFill(secondary_color)
    stripe_5.setOutline(secondary_color)
    stripe_5.draw(winOne)

    stripe_6 = Rectangle(Point(297, 309+y_shift), Point(307, 311+y_shift))
    stripe_6.setFill(third_color)
    stripe_6.setOutline(third_color)
    stripe_6.draw(winOne)

    stripe_7 = Rectangle(Point(326, 309+y_shift), Point(336, 311+y_shift))
    stripe_7.setFill(third_color)
    stripe_7.setOutline(third_color)
    stripe_7.draw(winOne)

    return[connector, body, left_wing, right_wing, connector_base_1, connector_base_2,
           stripe_1, front, stripe_2, stripe_3,
           stripe_4, stripe_5, stripe_6, stripe_7]


# setting function to draw user's TIE bomber
def bombers_s3(winOne):
    main = color_rgb(192, 192, 192)
    secondary = color_rgb(0, 0, 0)
    third = color_rgb(169, 169, 169)
    fourth = color_rgb(75, 75, 75)

    # y_shift helps re-adjust shapes positions
    y_shift = -230

    left_body = Polygon(Point(293, 289+y_shift), Point(294, 285+y_shift), Point(310, 285+y_shift),
                        Point(312, 287+y_shift), Point(312, 331+y_shift), Point(310, 334+y_shift), Point(295, 334+y_shift), Point(293, 332+y_shift))

    left_body.setFill(main)
    left_body.setOutline(main)
    left_body.draw(winOne)

    right_body = Polygon(Point(318, 287+y_shift), Point(321, 280+y_shift), Point(334, 280+y_shift), Point(337, 285+y_shift),
                         Point(337, 333+y_shift), Point(335, 334+y_shift), Point(320, 334+y_shift), Point(318, 332+y_shift))

    right_body.setFill(main)
    right_body.setOutline(main)
    right_body.draw(winOne)

    connector = Rectangle(Point(307, 294+y_shift), Point(319, 304+y_shift))
    connector.setFill(third)
    connector.setOutline(third)
    connector.draw(winOne)

    left_wing = Polygon(Point(280, 269+y_shift), Point(292, 272+y_shift), Point(292, 348+y_shift), Point(280, 351+y_shift))
    left_wing.setFill(fourth)
    left_wing.draw(winOne)

    right_wing = Polygon(Point(338, 271+y_shift), Point(349, 268+y_shift), Point(349, 351+y_shift), Point(338, 347+y_shift))
    right_wing.setFill(fourth)
    right_wing.draw(winOne)

    front = Rectangle(Point(321, 280+y_shift), Point(335, 276+y_shift))
    front.setFill(third)
    front.setOutline(third)
    front.draw(winOne)

    stripe_1 = Rectangle(Point(296, 298+y_shift), Point(297, 326+y_shift))
    stripe_1.setFill(third)
    stripe_1.setOutline(third)
    stripe_1.draw(winOne)

    stripe_2 = Rectangle(Point(305, 298+y_shift), Point(306, 326+y_shift))
    stripe_2.setFill(third)
    stripe_2.setOutline(third)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(322, 304+y_shift), Point(334, 328+y_shift))
    stripe_3.setFill(third)
    stripe_3.setOutline(third)
    stripe_3.draw(winOne)

    stripe_4 = Oval(Point(321, 285+y_shift), Point(335, 300+y_shift))
    stripe_4.setFill(third)
    stripe_4.setOutline(third)
    stripe_4.draw(winOne)

    stripe_5 = Rectangle(Point(283, 298+y_shift), Point(290, 342+y_shift))
    stripe_5.setFill(secondary)
    stripe_5.draw(winOne)

    stripe_6 = Polygon(Point(283, 272+y_shift), Point(290, 277+y_shift), Point(290, 290+y_shift), Point(283, 290+y_shift))
    stripe_6.setFill(secondary)
    stripe_6.draw(winOne)

    stripe_7 = Rectangle(Point(340, 298+y_shift), Point(347, 344+y_shift))
    stripe_7.setFill(secondary)
    stripe_7.draw(winOne)

    stripe_8 = Polygon(Point(340, 277+y_shift), Point(347, 272+y_shift), Point(347, 290+y_shift), Point(340, 290+y_shift))
    stripe_8.setFill(secondary)
    stripe_8.draw(winOne)

    return[left_body, right_body, connector, left_wing, right_wing, front, stripe_1, stripe_2,
           stripe_3, stripe_4, stripe_5, stripe_6, stripe_7, stripe_8]


# setting function to draw enemy TIE fighters that would be chasing user
def enemy_fighters(winOne):
    main_color = color_rgb(192, 192, 192)
    secondary_color = color_rgb(128, 128, 128)
    third_color = color_rgb(169, 169, 169)

    # x and y shift helps with re-positioning all the shapes
    y_shift = 90
    x_shift = 50
    
    connector = Rectangle(Point(296-x_shift, 306+y_shift), Point(337-x_shift, 313+y_shift))
    connector.setFill(main_color)
    connector.setOutline(main_color)
    connector.draw(winOne)

    connector_base_1 = Polygon(Point(288-x_shift, 303+y_shift), Point(296-x_shift, 305+y_shift), Point(296-x_shift, 314+y_shift), Point(288-x_shift, 317+y_shift))
    connector_base_1.setFill(third_color)
    connector_base_1.setOutline(third_color)
    connector_base_1.draw(winOne)

    connector_base_2 = Polygon(Point(337-x_shift, 305+y_shift), Point(345-x_shift, 303+y_shift), Point(345-x_shift, 316+y_shift), Point(337-x_shift, 314+y_shift))
    connector_base_2.setFill(third_color)
    connector_base_2.setOutline(third_color)
    connector_base_2.draw(winOne)
    
    body = Oval(Point(306-x_shift, 298+y_shift), Point(329-x_shift, 326+y_shift))
    body.setFill(main_color)
    body.setOutline(main_color)
    body.draw(winOne)

    left_wing = Rectangle(Point(284-x_shift, 276+y_shift), Point(288-x_shift, 342+y_shift))
    left_wing.setFill(secondary_color)
    left_wing.setOutline(secondary_color)
    left_wing.draw(winOne)

    right_wing = Rectangle(Point(345-x_shift, 276+y_shift), Point(349-x_shift, 342+y_shift))
    right_wing.setFill(secondary_color)
    right_wing.setOutline(secondary_color)
    right_wing.draw(winOne)

    stripe_1 = Oval(Point(310-x_shift, 302+y_shift), Point(325-x_shift, 320+y_shift))
    stripe_1.setFill(third_color)
    stripe_1.setOutline(third_color)
    stripe_1.draw(winOne)

    front = Rectangle(Point(312-x_shift, 296+y_shift), Point(323-x_shift, 299+y_shift))
    front.setFill(main_color)
    front.setOutline(main_color)
    front.draw(winOne)

    stripe_2 = Rectangle(Point(312-x_shift, 307+y_shift), Point(313-x_shift, 311+y_shift))
    stripe_2.setFill(secondary_color)
    stripe_2.setOutline(secondary_color)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(315-x_shift, 303+y_shift), Point(316-x_shift, 310+y_shift))
    stripe_3.setFill(secondary_color)
    stripe_3.setOutline(secondary_color)
    stripe_3.draw(winOne)

    stripe_4 = Rectangle(Point(318-x_shift, 304+y_shift), Point(319-x_shift, 310+y_shift))
    stripe_4.setFill(secondary_color)
    stripe_4.setOutline(secondary_color)
    stripe_4.draw(winOne)

    stripe_5 = Rectangle(Point(321-x_shift, 305+y_shift), Point(322-x_shift, 311+y_shift))
    stripe_5.setFill(secondary_color)
    stripe_5.setOutline(secondary_color)
    stripe_5.draw(winOne)

    stripe_6 = Rectangle(Point(297-x_shift, 309+y_shift), Point(307-x_shift, 311+y_shift))
    stripe_6.setFill(third_color)
    stripe_6.setOutline(third_color)
    stripe_6.draw(winOne)

    stripe_7 = Rectangle(Point(326-x_shift, 309+y_shift), Point(336-x_shift, 311+y_shift))
    stripe_7.setFill(third_color)
    stripe_7.setOutline(third_color)
    stripe_7.draw(winOne)

    return[connector, body, left_wing, right_wing, connector_base_1, connector_base_2,
           stripe_1, front, stripe_2, stripe_3,
           stripe_4, stripe_5, stripe_6, stripe_7]


# setting function to draw enemy TIE bombers that would be chasing user
def enemy_bombers(winOne):
    main = color_rgb(192, 192, 192)
    secondary = color_rgb(0, 0, 0)
    third = color_rgb(169, 169, 169)
    fourth = color_rgb(75, 75, 75)

    # can help re-adjust shapes positions
    y_shift = 100
    x_shift = 50
    
    left_body = Polygon(Point(293+x_shift, 289+y_shift), Point(294+x_shift, 285+y_shift), Point(310+x_shift, 285+y_shift),
                        Point(312+x_shift, 287+y_shift), Point(312+x_shift, 331+y_shift), Point(310+x_shift, 334+y_shift), Point(295+x_shift, 334+y_shift), Point(293+x_shift, 332+y_shift))

    left_body.setFill(main)
    left_body.setOutline(main)
    left_body.draw(winOne)

    right_body = Polygon(Point(318+x_shift, 287+y_shift), Point(321+x_shift, 280+y_shift), Point(334+x_shift, 280+y_shift), Point(337+x_shift, 285+y_shift),
                         Point(337+x_shift, 333+y_shift), Point(335+x_shift, 334+y_shift), Point(320+x_shift, 334+y_shift), Point(318+x_shift, 332+y_shift))

    right_body.setFill(main)
    right_body.setOutline(main)
    right_body.draw(winOne)

    connector = Rectangle(Point(307+x_shift, 294+y_shift), Point(319+x_shift, 304+y_shift))
    connector.setFill(third)
    connector.setOutline(third)
    connector.draw(winOne)

    left_wing = Polygon(Point(280+x_shift, 269+y_shift), Point(292+x_shift, 272+y_shift), Point(292+x_shift, 348+y_shift), Point(280+x_shift, 351+y_shift))
    left_wing.setFill(fourth)
    left_wing.draw(winOne)

    right_wing = Polygon(Point(338+x_shift, 271+y_shift), Point(349+x_shift, 268+y_shift), Point(349+x_shift, 351+y_shift), Point(338+x_shift, 347+y_shift))
    right_wing.setFill(fourth)
    right_wing.draw(winOne)

    front = Rectangle(Point(321+x_shift, 280+y_shift), Point(335+x_shift, 276+y_shift))
    front.setFill(third)
    front.setOutline(third)
    front.draw(winOne)

    stripe_1 = Rectangle(Point(296+x_shift, 298+y_shift), Point(297+x_shift, 326+y_shift))
    stripe_1.setFill(third)
    stripe_1.setOutline(third)
    stripe_1.draw(winOne)

    stripe_2 = Rectangle(Point(305+x_shift, 298+y_shift), Point(306+x_shift, 326+y_shift))
    stripe_2.setFill(third)
    stripe_2.setOutline(third)
    stripe_2.draw(winOne)

    stripe_3 = Rectangle(Point(322+x_shift, 304+y_shift), Point(334+x_shift, 328+y_shift))
    stripe_3.setFill(third)
    stripe_3.setOutline(third)
    stripe_3.draw(winOne)

    stripe_4 = Oval(Point(321+x_shift, 285+y_shift), Point(335+x_shift, 300+y_shift))
    stripe_4.setFill(third)
    stripe_4.setOutline(third)
    stripe_4.draw(winOne)

    stripe_5 = Rectangle(Point(283+x_shift, 298+y_shift), Point(290+x_shift, 342+y_shift))
    stripe_5.setFill(secondary)
    stripe_5.draw(winOne)

    stripe_6 = Polygon(Point(283+x_shift, 272+y_shift), Point(290+x_shift, 277+y_shift), Point(290+x_shift, 290+y_shift), Point(283+x_shift, 290+y_shift))
    stripe_6.setFill(secondary)
    stripe_6.draw(winOne)

    stripe_7 = Rectangle(Point(340+x_shift, 298+y_shift), Point(347+x_shift, 344+y_shift))
    stripe_7.setFill(secondary)
    stripe_7.draw(winOne)

    stripe_8 = Polygon(Point(340+x_shift, 277+y_shift), Point(347+x_shift, 272+y_shift), Point(347+x_shift, 290+y_shift), Point(340+x_shift, 290+y_shift))
    stripe_8.setFill(secondary)
    stripe_8.draw(winOne)

    return[left_body, right_body, connector, left_wing, right_wing, front, stripe_1, stripe_2,
           stripe_3, stripe_4, stripe_5, stripe_6, stripe_7, stripe_8]

# setting function to display victory message
def escape_success(winThree):
    message_color = color_rgb(255, 255, 255)
    text_size = 9
    
    congrats_image = Image(Point(316, 185), "darthvader_thumbup.gif")
    congrats_image.draw(winThree)

    congrats_line1 = Text(Point(382, 62), "Congratulations,")
    congrats_line1.setSize(text_size)
    congrats_line1.setTextColor(message_color)
    congrats_line1.draw(winThree)

    congrats_line2 = Text(Point(395, 78), "you have")
    congrats_line2.setSize(text_size)
    congrats_line2.setTextColor(message_color)
    congrats_line2.draw(winThree)

    congrats_line3 = Text(Point(406, 95), "successfully")
    congrats_line3.setSize(text_size)
    congrats_line3.setTextColor(message_color)
    congrats_line3.draw(winThree)

    congrats_line4 = Text(Point(410, 110), "escaped ! :)")
    congrats_line4.setSize(text_size)
    congrats_line4.setTextColor(message_color)
    congrats_line4.draw(winThree)

# setting function to display fail message
def escape_fail(winThree):
    message_color = color_rgb(255, 255, 255)
    text_size = 9
    
    fail_image = Image(Point(320, 180), "darthvader_intimidating.gif")
    fail_image.draw(winThree)

    message_line1 = Text(Point(402, 104), "YOU HAVE")
    message_line1.setSize(text_size)
    message_line1.setTextColor(message_color)
    message_line1.draw(winThree)

    message_line2 = Text(Point(407, 122), "FAILED TO")
    message_line2.setSize(text_size)
    message_line2.setTextColor(message_color)
    message_line2.draw(winThree)

    message_line3 = Text(Point(329, 215), "ESCAPE !!!")
    message_line3.setSize(text_size+5)
    message_line3.setTextColor(message_color)
    message_line3.draw(winThree)

# setting function to execute all commands present in scene three 
def scene_three():
    winThree = GraphWin("Scene three", 640, 360)
    winThree.setBackground(color_rgb(0, 0, 0))

    # draw random stars and meteors
    draw_stars(winThree)

    # draw meteors
    met_length = 60
    met_color = color_rgb(255, 255, 255)

    y_shift = 300
    
    met1 = Line(Point(99, 44-y_shift), Point(99, 44 + met_length-y_shift))
    met1.setFill(met_color)
    met1.setOutline(met_color)
    met1.draw(winThree)
    
    met2 = Line(Point(557, 180-y_shift), Point(557, 180 + met_length-y_shift))
    met2.setFill(met_color)
    met2.setOutline(met_color)
    met2.draw(winThree)

    met3 = Line(Point(321, 241-y_shift), Point(321, 241 + met_length-y_shift))
    met3.setFill(met_color)
    met3.setOutline(met_color)
    met3.draw(winThree)
    
    # drawing lasers and missiles
    lasers_color = color_rgb(255, 0, 0)

    missile_rad = 7

    laser_length = 8
    laser1 = Line(Point(235, 248), Point(235, 248 + laser_length))
    laser1.setFill(lasers_color)

    laser2 = Line(Point(297, 248), Point(297, 248 + laser_length))
    laser2.setFill(lasers_color)
    
    laser3 = laser1.clone()
    laser3.setFill(lasers_color)
    
    laser4 = laser2.clone()
    laser4.setFill(lasers_color)
    
    laser5 = laser1.clone()
    laser5.setFill(lasers_color)
    
    laser6 = laser2.clone()
    laser6.setFill(lasers_color)

    missile1 = Circle(Point(377, 243), missile_rad)
    missile1.setFill(lasers_color)
    
    missile2 = missile1.clone()
    missile2.setFill(lasers_color)
        
    # drawing the spacecraft that the user selected 
    if chosen_spacecraft == "1":
        user_spacecraft = falcon_s3(winThree)

    elif chosen_spacecraft == "2":
        user_spacecraft = outrider_s3(winThree)

    elif chosen_spacecraft == "3":
        user_spacecraft = xwing_s3(winThree)

    elif chosen_spacecraft == "4":
        user_spacecraft = fighters_s3(winThree)

    elif chosen_spacecraft == "5":
        user_spacecraft = bombers_s3(winThree)

    enemy_fighters_parts = enemy_fighters(winThree)
    fighters_vertex = 366
    fighters_position = 265

    enemy_bombers_parts = enemy_bombers(winThree)
    bombers_vertex = 369
    bombers_position = 260

    while fighters_vertex > fighters_position:
        for parts in enemy_fighters_parts:
            parts.move(0, -2)

        fighters_vertex -= 2
        time.sleep(0.01)

    while bombers_vertex >= bombers_position:
        for parts in enemy_bombers_parts:
            parts.move(0, -2)

        bombers_vertex -= 2
        time.sleep(0.01)


    center = 320

    turning_point1 = 150
    turning_point2 = 470
  
    round_num = 0
    lasers_vertex = 260

    meteor_vertex = -256

   # setting while loop to repeat for 3 times
   # user spacecraft dodges attacks from enemy spacecrafts
    while round_num < 3:

        while meteor_vertex <= 360:
            met1.move(0, 2)
            met2.move(0, 2)
            met3.move(0, 2)
            time.sleep(0.001)

            meteor_vertex += 2

        met1.undraw()
        met2.undraw()
        met3.undraw()

        laser1.draw(winThree)
        laser2.draw(winThree)
        missile1.draw(winThree)
        while lasers_vertex > 180:
            laser1.move(0, -5)
            laser2.move(0, -5) 
            missile1.move(0, -5)

            for parts in user_spacecraft:
                parts.move(-5, 0)
            center -= 5

            lasers_vertex -= 5
            

            time.sleep(0.001)

        laser3.draw(winThree)
        laser4.draw(winThree)
        missile2.draw(winThree)
        while lasers_vertex > 100:
            laser1.move(0, -5)
            laser2.move(0, -5)
            laser3.move(0, -5)
            laser4.move(0, -5)
            missile1.move(0, -5)
            missile2.move(0, -5)

            for parts in user_spacecraft:
                parts.move(-5, 0)
            center -= 5

            lasers_vertex -= 5

            time.sleep(0.001)

        laser5.draw(winThree)
        laser6.draw(winThree)
        while lasers_vertex > -260:
            laser1.move(0, -5)
            laser2.move(0, -5)
            laser3.move(0, -5)
            laser4.move(0, -5)
            missile1.move(0, -5)
            missile2.move(0, -5)

            if center <= turning_point1:
                for parts in user_spacecraft:
                    parts.move(0, 0)

            else:
                for parts in user_spacecraft:
                    parts.move(-5, 0)
                center -= 5

            laser5.move(0, -5)
            laser6.move(0, -5)

            lasers_vertex -= 5

            time.sleep(0.001)
            
        laser1.undraw()
        laser2.undraw()
        laser3.undraw()
        laser4.undraw()
        laser5.undraw()
        laser6.undraw()

        missile1.undraw()
        missile2.undraw()

        lasers_color = color_rgb(255, 0,0 )

        missile_rad = 7

        laser_length = 8
        laser1 = Line(Point(235 - 170, 248), Point(235 - 170, 248 + laser_length))
        laser1.setFill(lasers_color)
        
        laser2 = Line(Point(297 - 170, 248), Point(297 - 170, 248 + laser_length))
        laser2.setFill(lasers_color)

        laser3 = laser1.clone()
        laser3.setFill(lasers_color)
        
        laser4 = laser2.clone()
        laser4.setFill(lasers_color)

        laser5 = laser1.clone()
        laser5.setFill(lasers_color)

        laser6 = laser2.clone()
        laser6.setFill(lasers_color)

        missile1 = Circle(Point(377 - 170, 243), missile_rad)
        missile1.setFill(lasers_color)
        
        missile2 = missile1.clone()
        missile2.setFill(lasers_color)

        lasers_vertex = 260

        fighters_vertex = 268
        bombers_vertex = 367
        
        while fighters_vertex > 100:
            for parts in enemy_fighters_parts:
                parts.move(-4, 0)
            fighters_vertex -= 4
            time.sleep(0.001)
            
        while bombers_vertex > 200:
            for parts in enemy_bombers_parts:
                parts.move(-4, 0)
            bombers_vertex -= 4
            time.sleep(0.001)

        laser1.draw(winThree)
        laser2.draw(winThree)
        missile1.draw(winThree)
        while lasers_vertex > 180:
            laser1.move(0, -5)
            laser2.move(0, -5) 
            missile1.move(0, -5)

            for parts in user_spacecraft:
                parts.move(5, 0)
            center += 5
            

            lasers_vertex -= 5
            
            time.sleep(0.001)

        laser3.draw(winThree)
        laser4.draw(winThree)
        missile2.draw(winThree)
        while lasers_vertex > 100:
            laser1.move(0, -5)
            laser2.move(0, -5)
            laser3.move(0, -5)
            laser4.move(0, -5)
            missile1.move(0, -5)
            missile2.move(0, -5)

            for parts in user_spacecraft:
                parts.move(5, 0)
            center+= 5

            lasers_vertex -= 5

            time.sleep(0.001)

        laser5.draw(winThree)
        laser6.draw(winThree)
        while lasers_vertex > -260:
            laser1.move(0, -5)
            laser2.move(0, -5)
            laser3.move(0, -5)
            laser4.move(0, -5)
            missile1.move(0, -5)
            missile2.move(0, -5)
            laser5.move(0, -5)
            laser6.move(0, -5)

            if center >= turning_point2:
                for parts in user_spacecraft:
                    parts.move(0, 0)

            else:
                for parts in user_spacecraft:
                    parts.move(5, 0)
                center += 5

            lasers_vertex -= 5

            time.sleep(0.001)                

        laser1.undraw()              
        laser2.undraw()
        laser3.undraw()
        laser4.undraw()
        laser5.undraw()
        laser6.undraw()

        missile1.undraw()
        missile2.undraw()

        laser1 = Line(Point(235 +170, 248), Point(235 + 170, 248 + laser_length))
        laser1.setFill(lasers_color)
        
        laser2 = Line(Point(297 + 170, 248), Point(297 + 170, 248 + laser_length))
        laser2.setFill(lasers_color)

        laser3 = laser1.clone()
        laser3.setFill(lasers_color)
        
        laser4 = laser2.clone()
        laser4.setFill(lasers_color)

        laser5 = laser1.clone()
        laser5.setFill(lasers_color)

        laser6 = laser2.clone()
        laser6.setFill(lasers_color)

        missile1 = Circle(Point(377 + 170, 243), missile_rad)
        missile1.setFill(lasers_color)
        
        missile2 = missile1.clone()
        missile2.setFill(lasers_color)

        lasers_vertex = 260

        while bombers_vertex < 537:
            for parts in enemy_bombers_parts:
                parts.move(4, 0)
            bombers_vertex += 4
            time.sleep(0.001)

        while fighters_vertex < 438:
            for parts in enemy_fighters_parts:
                parts.move(4, 0)
            fighters_vertex += 4
            time.sleep(0.001)

        laser1.draw(winThree)
        laser2.draw(winThree)
        missile1.draw(winThree)
        while lasers_vertex > 180:
            laser1.move(0, -5)
            laser2.move(0, -5) 
            missile1.move(0, -5)

            for parts in user_spacecraft:
                parts.move(-5, 0)
            center -= 5

            lasers_vertex -= 5
            

            time.sleep(0.001)

        laser3.draw(winThree)
        laser4.draw(winThree)
        missile2.draw(winThree)
        while lasers_vertex > 100:
            laser1.move(0, -5)
            laser2.move(0, -5)
            laser3.move(0, -5)
            laser4.move(0, -5)
            missile1.move(0, -5)
            missile2.move(0, -5)

            for parts in user_spacecraft:
                parts.move(-5, 0)
            center -= 5

            lasers_vertex -= 5

            time.sleep(0.001)

        laser5.draw(winThree)
        laser6.draw(winThree)
        while lasers_vertex > -260:
            laser1.move(0, -5)
            laser2.move(0, -5)
            laser3.move(0, -5)
            laser4.move(0, -5)
            missile1.move(0, -5)
            missile2.move(0, -5)
            laser5.move(0, -5)
            laser6.move(0, -5)

            if center <= 320:
                for parts in user_spacecraft:
                    parts.move(0, 0)

            else:
                for parts in user_spacecraft:
                    parts.move(-5, 0)
                center -= 5

            lasers_vertex -= 5

            time.sleep(0.001)   


        laser1.undraw()              
        laser2.undraw()
        laser3.undraw()
        laser4.undraw()
        laser5.undraw()
        laser6.undraw()

        missile1.undraw()
        missile2.undraw()


        laser1 = Line(Point(235, 248), Point(235, 248 + laser_length))
        laser1.setFill(lasers_color)
        
        laser2 = Line(Point(297, 248), Point(297, 248 + laser_length))
        laser2.setFill(lasers_color)

        laser3 = laser1.clone()
        laser3.setFill(lasers_color)
        
        laser4 = laser2.clone()
        laser4.setFill(lasers_color)

        laser5 = laser1.clone()
        laser5.setFill(lasers_color)

        laser6 = laser2.clone()
        laser6.setFill(lasers_color)

        missile1 = Circle(Point(377, 243), missile_rad)
        missile1.setFill(lasers_color)
        
        missile2 = missile1.clone()
        missile2.setFill(lasers_color)

        lasers_vertex = 260

        while fighters_vertex > 268:
            for parts in enemy_fighters_parts:
                parts.move(-2, 0)
            fighters_vertex -= 2
            time.sleep(0.001)

        while bombers_vertex > 367:
            for parts in enemy_bombers_parts:
                parts.move(-2, 0)
            bombers_vertex -= 2
            time.sleep(0.001)

        meteor_vertex = -256
        met_length = 60
        met_color = color_rgb(255, 255, 255)

        y_shift = 300
    
        met1 = Line(Point(99, 44-y_shift), Point(99, 44 + met_length-y_shift))
        met1.setFill(met_color)
        met1.setOutline(met_color)
        met1.draw(winThree)
    
        met2 = Line(Point(557, 180-y_shift), Point(557, 180 + met_length-y_shift))
        met2.setFill(met_color)
        met2.setOutline(met_color)
        met2.draw(winThree)

        met3 = Line(Point(321, 241-y_shift), Point(321, 241 + met_length-y_shift))
        met3.setFill(met_color)
        met3.setOutline(met_color)
        met3.draw(winThree)
    
        round_num += 1

    # setting entry for user input
    message_box = Rectangle(Point(240, 158), Point(409, 190))
    counter_attack = Entry(Point(319, 180), 30)
    counter_attack.setText("Would you like to counter attack? (y/n) ")
    counter_attack.draw(winThree)

    key_pressed = winThree.getKey()
    if key_pressed == "BackSpace":
        key_pressed = ""
    user_input = counter_attack.clone()
    user_input.setText(key_pressed)
    user_input.draw(winThree)

    while True:
        winThree.getMouse()
        response = user_input.getText()
        response = response.lower()
        
        if response == "y":
            user_input.undraw()
            counter_attack.undraw()
            weapon_choice = Entry(Point(319, 180), 38)
            weapon_choice.setText("Photon Torpedo (1) or Concussion Missiles (2): ")
            weapon_choice.draw(winThree)
            
            key_pressed = winThree.getKey()
            if key_pressed == "BackSpace":
                key_pressed = ""
            user_input = weapon_choice.clone()
            user_input.setText(key_pressed)
            user_input.draw(winThree)
            break

                    
        elif response == "n":
            user_input.undraw()
            counter_attack.undraw()
            user_choice = ""
            break


    if response == "y":
        while True:
            winThree.getMouse()
            user_choice = user_input.getText()
    
            if user_choice == "1":
                user_input.undraw()
                weapon_choice.undraw()
                break

            elif user_choice == "2":
                user_input.undraw()
                weapon_choice.undraw()
                break

    user_vertex = 16
    if response == "y":
        while fighters_vertex > 140:
            for parts in enemy_fighters_parts:
                parts.move(-2, 0)

            for parts in enemy_bombers_parts:
                parts.move(2, 0)

            fighters_vertex -= 2
            time.sleep(0.001)

        while user_vertex < 240:
            for parts in user_spacecraft:
                parts.move(0, 4)

            for parts in enemy_fighters_parts:
                parts.move(0, -4)

            for parts in enemy_bombers_parts:
                parts.move(0, -4)
                
            user_vertex += 4
            time.sleep(0.001)


    # drawing photon torpedo
    torpedo_color = color_rgb(255, 255, 0)
    torpedo_rad = 4
    photon_torpedo = Circle(Point(310, 220), torpedo_rad)
    photon_torpedo.setFill(torpedo_color)

    torpedo_position = 220
    fighters_vertex = 120
    if user_choice == "1":
        photon_torpedo.draw(winThree)

        # setting while loop to make photon torpedo's radius bigger after each cycle
        while torpedo_rad < 25:
            photon_torpedo.undraw()
            torpedo_rad += 1
            photon_torpedo = Circle(Point(310, 220), torpedo_rad)
            photon_torpedo.setFill(torpedo_color)
            photon_torpedo.draw(winThree)
            time.sleep(0.05)

        while torpedo_position > 65:
            photon_torpedo.move(0, -2)
            torpedo_position -= 2
            time.sleep(0.01)

        # setting while loops such that enemy spacecrafts are sucked in by photon torpedo and destroyed
        while fighters_vertex < 268:
            for parts in enemy_fighters_parts:
                parts.move(4, 0)

            for parts in enemy_bombers_parts:
                parts.move(-4, 0)

            fighters_vertex += 4
            time.sleep(0.001)

        while torpedo_rad < 100:
            photon_torpedo.undraw()
            torpedo_rad += 2
            photon_torpedo = Circle(Point(310, 65), torpedo_rad)
            photon_torpedo.setFill(torpedo_color)
            photon_torpedo.draw(winThree)
            time.sleep(0.05)

        # move the enemy spacecrafts off scene to show that it has been destroyed
        for parts in enemy_fighters_parts:
            parts.move(0, -200)

        for parts in enemy_bombers_parts:
            parts.move(0, -200)

        while torpedo_rad > 0:
            photon_torpedo.undraw()
            torpedo_rad -= 2
            photon_torpedo = Circle(Point(310, 65), torpedo_rad)
            photon_torpedo.setFill(torpedo_color)
            photon_torpedo.draw(winThree)
            time.sleep(0.01)

        photon_torpedo.undraw()

        for s in range(360):
            for parts in user_spacecraft:
                parts.move(0, -1)

            time.sleep(0.001)

        escape_success(winThree)

    # drawing concussion missiles
    concus_missile1 = Rectangle(Point(490 - 351, 198), Point(496 - 351, 245))
    concus_missile1.setFill(lasers_color)
   
    concus_missile2 = Rectangle(Point(490, 198), Point(496, 245))
    concus_missile2.setFill(lasers_color)


    # drawing explosion effect
    explosion_rad = 120
    explosion1 = Circle(Point(144, 74), explosion_rad)
    explosion1.setFill(lasers_color)

    explosion2 = Circle(Point(489, 74), explosion_rad)
    explosion2.setFill(lasers_color)

    missile_vertex = 198

    if user_choice == "2":
        spacecraft_center = 320

        while spacecraft_center > 144:
            for parts in user_spacecraft:
                parts.move(-2, 0)

            spacecraft_center -= 2
            time.sleep(0.001)

        concus_missile1.draw(winThree)
        while missile_vertex > 91:
            concus_missile1.move(0, -2)
            missile_vertex -= 2
            time.sleep(0.001)

        explosion1.draw(winThree)

        concus_missile1.undraw()
        
        for parts in enemy_fighters_parts:
            parts.move(0, -200)


        while spacecraft_center < 495:
            if explosion_rad == 0:
                explosion_rad += 0

            else:
                explosion_rad -= 2

            explosion1.undraw()
            explosion1 = Circle(Point(144, 74), explosion_rad)
            explosion1.setFill(lasers_color)
            explosion1.draw(winThree)

            for parts in user_spacecraft:
                parts.move(6, 0)

            spacecraft_center += 6
            time.sleep(0.001)

        explosion1.undraw()
        missile_vertex = 198

        concus_missile2.draw(winThree)
        while missile_vertex > 98:
            concus_missile2.move(0, -2)
            missile_vertex -= 2
            time.sleep(0.001)

        explosion_rad = 120
        explosion2.draw(winThree)

        for parts in enemy_bombers_parts:
            parts.move(0, -200)

        concus_missile2.undraw()

        while explosion_rad > 0:
            explosion2.undraw()
            explosion_rad -= 2
            explosion2 = Circle(Point(489, 74), explosion_rad)
            explosion2.setFill(lasers_color)
            explosion2.draw(winThree)
            time.sleep(0.01)

        explosion2.undraw()

        for s in range(360):
            for parts in user_spacecraft:
                parts.move(0, -1)

            time.sleep(0.001)

        escape_success(winThree)


    # drawing enemy weapons
    missile_rad = 7

    laser_length = 8
    laser1 = Line(Point(235 + 10, 248), Point(235 + 10, 248 + laser_length))
    laser1.setFill(lasers_color)

    laser2 = Line(Point(297 + 10, 248), Point(297 + 10, 248 + laser_length))
    laser2.setFill(lasers_color)
    
    laser3 = laser1.clone()
    laser3.setFill(lasers_color)
    
    laser4 = laser2.clone()
    laser4.setFill(lasers_color)
    
    laser5 = laser1.clone()
    laser5.setFill(lasers_color)
    
    laser6 = laser2.clone()
    laser6.setFill(lasers_color)

    missile1 = Circle(Point(377 - 13, 243), missile_rad)
    missile1.setFill(lasers_color)
    
    missile2 = missile1.clone()
    missile2.setFill(lasers_color)

    # setting user spacecraft's explosion
    grand_rad = 75
    grand_explosion = Circle(Point(318, 77), grand_rad)
    grand_explosion.setFill(lasers_color)

    
    if response == "n":

        for f in range(10):
            for parts in enemy_fighters_parts:
                parts.move(1, 0)

            time.sleep(0.01)

        for b in range(13):
            for parts in enemy_bombers_parts:
                parts.move(-1, 0)

            time.sleep(0.01)
        
        laser1.draw(winThree)
        laser2.draw(winThree)
        missile1.draw(winThree)
        while lasers_vertex > 180:
            laser1.move(0, -5)
            laser2.move(0, -5) 
            missile1.move(0, -5)

            lasers_vertex -= 5
            

            time.sleep(0.01)

        laser3.draw(winThree)
        laser4.draw(winThree)
        missile2.draw(winThree)
        while lasers_vertex > 100:
            if lasers_vertex == 130:
                grand_explosion.draw(winThree)

                for parts in user_spacecraft:
                    parts.move(0, -260)
                
            
            laser1.move(0, -5)
            laser2.move(0, -5)
            laser3.move(0, -5)
            laser4.move(0, -5)
            missile1.move(0, -5)
            missile2.move(0, -5)

            lasers_vertex -= 5

            time.sleep(0.01)

        laser5.draw(winThree)
        laser6.draw(winThree)
        while lasers_vertex > -260:
            if lasers_vertex <= 130:
                grand_explosion.undraw()
                grand_rad += 1
                grand_explosion = Circle(Point(318, 77), grand_rad)
                grand_explosion.setFill(lasers_color)
                grand_explosion.draw(winThree)

                time.sleep(0.01)
                
            laser1.move(0, -5)
            laser2.move(0, -5)
            laser3.move(0, -5)
            laser4.move(0, -5)
            missile1.move(0, -5)
            missile2.move(0, -5)

            laser5.move(0, -5)
            laser6.move(0, -5)

            lasers_vertex -= 5

            time.sleep(0.01)

        for i in range(60):
            grand_explosion.undraw()
            grand_rad += 1
            grand_explosion = Circle(Point(318, 77), grand_rad)
            grand_explosion.setFill(lasers_color)
            grand_explosion.draw(winThree)

            time.sleep(0.01)
            
            for parts in enemy_fighters_parts:
                parts.move(0, 2)

            for parts in enemy_bombers_parts:
                parts.move(0, 2)

            time.sleep(0.001)

        # setting while loop to gradually change the color of grand explosion from red to yellow
        green = 0
        while green < 255:
            green += 1
            grand_explosion.undraw()
            grand_explosion.setFill(color_rgb(255, green, 0))
            grand_explosion.draw(winThree)

            time.sleep(0.001)

        # setting for loop to wait before explosion goes critical
        for i in range(3):
            time.sleep(0.05)

        while grand_rad > 0:
            grand_explosion.undraw()
            grand_rad -= 5
            grand_explosion = Circle(Point(318, 77), grand_rad)
            grand_explosion.setFill(color_rgb(255, green, 0))
            grand_explosion.draw(winThree)

            time.sleep(0.001)

        # setting while loop to change the color of grand explosion from yellow to white
        # indicating that the explosion has gone critical
        blue = 0
        while blue < 255:
            blue += 1
            grand_explosion.undraw()
            grand_explosion.setFill(color_rgb(255, green, blue))
            grand_explosion.draw(winThree)

            time.sleep(0.001)

        while grand_rad < 500:
            grand_explosion.undraw()
            grand_rad += 5
            grand_explosion = Circle(Point(318, 77), grand_rad)
            grand_explosion.setFill(color_rgb(255, green, blue))
            grand_explosion.draw(winThree)

            time.sleep(0.001)

        for i in range(5):
            time.sleep(0.5)
            
        while grand_rad > 0:
            grand_explosion.undraw()
            grand_rad -= 100
            grand_explosion = Circle(Point(318, 77), grand_rad)
            grand_explosion.setFill(color_rgb(255, green, blue))
            grand_explosion.draw(winThree)

            time.sleep(0.001)

        grand_explosion.undraw()
        escape_fail(winThree)

    # setting the exit condition
    exit_con = Text(Point(313, 312), "Click anywhere to exit. ")
    exit_con.setSize(10)
    exit_con.setTextColor(color_rgb(255, 255, 255))
    exit_con.draw(winThree)
    winThree.getMouse()
    winThree.close()
    

    
# Main  
chosen_spacecraft = scene_one()
scene_two()
scene_three()

