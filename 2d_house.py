import cairo
import math

def draw_grid(ctx, width, height, spacing=50):
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    for x in range(0, width, spacing):
        ctx.move_to(x, 0)
        ctx.line_to(x, height)
    for y in range(0, height, spacing):
        ctx.move_to(0, y)
        ctx.line_to(width, y)
    ctx.stroke()

def draw_base(ctx):
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(100, 550, 500, 25)
    ctx.move_to(112.5, 550)
    ctx.line_to(112.5, 353)
    ctx.move_to(300, 550)
    ctx.line_to(300, 353)
    ctx.move_to(587.5, 550)
    ctx.line_to(587.5, 350)
    ctx.stroke()

def draw_window1(ctx):
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(425, 500, 125, 12.5)
    ctx.move_to(437.5, 500)
    ctx.line_to(437.5, 400)
    ctx.line_to(537.5, 400)
    ctx.line_to(537.5, 500)
    ctx.stroke()

def draw_window2(ctx):
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(150, 500, 125, 12.5)
    ctx.move_to(162.5, 500)
    ctx.line_to(162.5, 400)
    ctx.line_to(262.5, 400)
    ctx.line_to(262.5, 500)
    ctx.stroke()

def draw_window3(ctx):
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(187.5, 300, 50, 50)
    ctx.stroke()

def draw_roof1(ctx):
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(316, 350)
    ctx.line_to(600, 350)
    ctx.line_to(450, 200)
    ctx.line_to(224, 200)
    ctx.stroke()

def draw_roof(ctx):
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(100, 375)
    ctx.line_to(206.75, 200)
    ctx.line_to(312.5, 375)
    ctx.line_to(325, 362.5)
    ctx.line_to(206.75, 175)
    ctx.line_to(88.5, 362.5)
    ctx.close_path()
    ctx.move_to(318.5, 350)
    ctx.line_to(600, 350)
    ctx.stroke()

def draw_crescent(ctx):
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    ctx.arc(650, 150, 50, 0, 2 * math.pi)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.arc(625, 125, 50, 0, 2 * math.pi)
    ctx.fill()


if __name__ == '__main__':
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 600)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    # draw_grid(ctx, 800, 600, spacing=50)

    draw_base(ctx)
    draw_window1(ctx)
    draw_window2(ctx)
    draw_window3(ctx)
    draw_roof1(ctx)
    draw_crescent(ctx)
    draw_roof(ctx)

    surface.write_to_png("house.png")
