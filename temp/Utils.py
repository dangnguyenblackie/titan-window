from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import compileProgram,compileShader
from Config import *
import calendar
from datetime import datetime
import os

IGNOR_DIR = ["__pycache__", "icon", "style", "src"]

def listDirInDir(filePath):
    d = [
      dir for dir in os.listdir(filePath)
      if  not dir.startswith('.') and
          os.path.isdir(os.path.join(filePath, dir)) and
          dir not in IGNOR_DIR
    ]
    d.sort()
    return d

def folderEmpty(filePath):
    return len(os.listdir(filePath)) == 0

def is_valid_day_for_month_year(day, month_year):
    year, month = month_year.split('/')
    if not (1 <= int(month) <= 12):
        return False
    max_day = calendar.monthrange(int(year), int(month))[1]
    return 1 <= int(day) <= max_day

def is_safe_file(filename):
    unsafe_extensions = ['.exe', '.bat', '.sh', '.py']
    _, file_extension = os.path.splitext(filename)
    return file_extension.lower() not in unsafe_extensions

def listFile(folderPath):
    f = [
        file for file in os.listdir(folderPath)
        if  os.path.isfile(folderPath + file) and
            not file.startswith('.') and
            is_safe_file(file)
    ]
    f.sort(key=lambda e: e.split('.')[0])
    return f

def getYearMonthDate(radar):
    date_string = radar.time['units'].split(" ")[-1]
    dt = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")

    return (dt.year, dt.strftime("%m"), dt.strftime("%d"))

def color(value):
    normalized_values = (value - 0) / (65 - 0)
    colors = np.zeros((len(value), 3))
    colors[:, 0] = 0.2 + normalized_values # Red channel
    colors[:, 1] = normalized_values        # Green channel
    colors[:, 2] = 0.6-normalized_values     # Blue channel
    return colors

def create_shader(vertex_filepath: str, fragment_filepath: str) -> int:
    print(os.getcwd())
    """
        Compile and link shader modules to make a shader program.

        Parameters:

            vertex_filepath: path to the text file storing the vertex
                            source code

            fragment_filepath: path to the text file storing the
                                fragment source code

        Returns:

            A handle to the created shader program
    """
    with open(vertex_filepath,'r') as f:
        vertex_src = f.readlines()

    with open(fragment_filepath,'r') as f:
        fragment_src = f.readlines()

    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                            compileShader(fragment_src, GL_FRAGMENT_SHADER))

    return shader

def convertGameTime2Minute(time):
    minute = (time // WINDOW_PROPERTIES.FPS) // 60
    second = (time // WINDOW_PROPERTIES.FPS) - 60 * minute
    return "{:02d}:{:02d}".format(minute, second)

class Timer:
    def __init__(self, time ,fps=WINDOW_PROPERTIES.FPS):
        self.time = time*fps
        self.currentTime = time*fps
        self.flag = False

    def run(self):
        self.currentTime -= 1

        if self.currentTime <= 0:
            self.flag = True

    def reset(self):
        self.flag = False
        self.currentTime = self.time

    def removeAndSetOtherTime(self, time, fps=WINDOW_PROPERTIES.FPS):
        self.time = time*fps
        self.currentTime = time*fps
        self.flag = False


