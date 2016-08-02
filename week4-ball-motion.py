# Ball motion with an explicit timer

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
a = 1
vel = [a * -40.0 / 60.0, a * 5.0 / 60.0]  # pixels per update (1/60 seconds)

def draw(canvas):

    # update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # collide and reflect off of left/right hand side of canvas
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
        vel[0] = - vel[0]

    # collide and reflect off of top/bottom of canvas
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        vel[1] = - vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

