from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys

name = "Terreno"
name_file_points = ""
name_file_sol = ""

num_points = 0
points = []
num_demands = 0
radars_max_radius = 0
points_demands = []
values_demands = []
rad_on = []

value_d = False

last_x = 0
last_y = 0
rotateZ = 0
min_point = []
max_point = []
middle_point = []


def main():
    global num_points, points, num_demands, radars_max_radius, points_demands, values_demands, rad_on, min_point, max_point, middle_point, name_file_points, name_file_sol, value_d
    radars_max_radius, num_points, points, num_demands, points_demands = read_instance_file(
        name_file_points)
    values_demands, rad_on = read_file_instance_sol(name_file_sol)

    min_point, max_point = min(points), max(points)
    middle_point = [(max_point[0]+min_point[0])/2,
                    (max_point[1]+min_point[1])/2]

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(name)

    init()

    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)

    glutMainLoop()

    return


def init():
    global middle_point

    glClearColor(1., 1., 1., 1.)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(40., 1., 1., 1000.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(50, 50, 160,
              50, 50, 0,
              0, 1, 0)
    return


def drawCircle(raio):
    theta = 0
    glBegin(GL_LINE_STRIP)
    for _ in range(101):
        glVertex2f(raio*cos(theta), raio*sin(theta))
        theta += 2*pi/100
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()

    glRotatef(rotateZ, 0, 0, 1)

    glPointSize(3)
    glLineWidth(2)
    for k in range(len(points)):
        glPointSize(4) if rad_on[k] else glPointSize(3)
        glColor3f(0, 0, 0) if rad_on[k] else glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_POINTS)
        glVertex2fv(points[k])
        glEnd()
        glColor3f(0, 0, 1)
        glPushMatrix()
        glTranslatef(points[k][0], points[k][1], 0)
        if rad_on[k]:
            drawCircle(radars_max_radius)
        glPopMatrix()

    glPointSize(5)
    glBegin(GL_POINTS)
    for k in range(len(points_demands)):
        glColor3f(0, 0.7, 0) if values_demands[k] != 0 else glColor3f(
            1, 0, 0)
        glVertex2fv(points_demands[k])
    glEnd()

    glPopMatrix()

    glutSwapBuffers()

    return


def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            last_x = x
            last_y = y

    glutPostRedisplay()
    return


def motion(x, y):
    global rotateZ, last_x, last_y
    #rotateZ += x - last_x

    last_x = x
    last_y = y

    glutPostRedisplay()

    return


def keyboard(key, x, y):
    global value_d
    if key == b' ':
        value_d = not value_d
    return


def idle():
    glutPostRedisplay()
    return


def read_instance_file(arq):
    with open(arq, 'r') as f:
        radars_max_radius = float(f.readline())
        num_points = int(f.readline())
        points = [[] for k in range(num_points)]
        for k in range(num_points):
            points[k] = list(map(float, f.readline().split()))

        num_demands = int(f.readline())
        points_demands = [[] for k in range(num_demands)]
        for k in range(num_demands):
            points_demands[k] = list(map(float, f.readline().split()))
    return radars_max_radius, num_points, points, num_demands, points_demands


def read_file_instance_sol(arq):
    values_demands = [[] for k in range(num_demands)]
    rad_on = [[] for k in range(num_points)]
    with open(arq, 'r') as f:
        f.readline()  # Comment
        f.readline()  # Objective function
        for k in range(num_demands):
            values_demands[k] = float(f.readline().split()[1])
        for k in range(num_points):
            rad_on[k] = True if int(
                f.readline().split()[1]) == 1 else False
    return values_demands, rad_on


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect params input")
        print("Right input:")
        print("               File of instance points - InstancesPoints/<file>")
        print("               File of solution - Solutions/<file>")
        sys.exit()
    name_file_points = sys.argv[1]
    name_file_sol = sys.argv[2]
    main()
