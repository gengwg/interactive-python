# first example of drawing on the canvas

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!",[100, 100], 24, "White")
    # drawing starts from the lower left of the string
    canvas.draw_circle([100, 100], 2, 2, "Red")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register draw handler
frame.set_draw_handler(draw)

# start frame
frame.start()
