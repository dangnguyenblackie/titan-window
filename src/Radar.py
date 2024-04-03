import numpy as np
import pyart
import cartopy.crs as ccrs
import os
from sklearn.preprocessing import MinMaxScaler
from Utils import color

class DIRECTORY:
  FILE_PATH = "../Data/"
  RADAR_NAME = "NHB/"
  DATE = "01/"
  MODE = "1_prt/"

class DataManager:

  RAW_DATA = None
  GRID_DATA = None
  NUM_OF_RAW_FILES = 0
  NUM_OF_GRID_FILES = 0

  @staticmethod
  def getAllDataFilePaths(filePath: str = DIRECTORY.FILE_PATH, radarName: str = DIRECTORY.RADAR_NAME, date: str = DIRECTORY.DATE, mode: str = DIRECTORY.MODE):
    filePaths = [
        fileName for fileName in os.listdir(
        filePath +
        radarName +
        date +
        mode)
        ]

    filePaths.sort()
    filePaths = [
        filePath +
        radarName +
        date +
        mode
        + fileName for fileName in filePaths
        ]

    if "grid" not in mode:
      DataManager.NUM_OF_RAW_FILES = len(filePaths)
    else:
      DataManager.NUM_OF_GRID_FILES = len(filePaths)

    return filePaths

  @staticmethod
  def splitData(filePath: str = DIRECTORY.FILE_PATH, radarName: str = DIRECTORY.RADAR_NAME, date: str = DIRECTORY.DATE, mode: str = DIRECTORY.MODE):
    print("Run splitData")
    if radarName == "NHB/" and mode == "raw/":
      data = DataManager.getAllDataFilePaths(filePath, radarName, date, mode)
      one_prt = []
      two_prt = []

      for i in range(len(data)):
          if pyart.io.read(data[i]).instrument_parameters['prt_mode']['data'][0].decode() == 'fixed':
            one_prt.append(data[i])
          else: two_prt.append(data[i])

      firstDir = filePath + radarName + date + '1_prt/'
      secondDir = filePath + radarName + date + '2_prt/'

      print("Creating firstDir at: ", firstDir)
      print("Creating secondDir at: ", secondDir)

      os.mkdir(firstDir)
      os.mkdir(secondDir)

      for i in one_prt:
          os.rename(i, firstDir + i.split('/')[-1])
      for i in two_prt:
          os.rename(i, secondDir + i.split('/')[-1])

    @staticmethod
    def genGrid(filePath: str = DIRECTORY.FILE_PATH, radarName: str = DIRECTORY.RADAR_NAME, date: str = DIRECTORY.DATE, mode: str = DIRECTORY.MODE):
      def get_grid(radar):
        """ Returns grid object from radar object. """
        grid = pyart.map.grid_from_radars(
            radar, grid_shape=(5, 1000, 1000),
            grid_limits=((0, 25000), (-330000,330000), (-330000, 330000)),
            fields=['reflectivity'], gridding_algo='map_gates_to_grid',
            h_factor=0., nb=0.6, bsp=1., min_radius=200.)
        return grid

      def write_grid():
          tmp_dir = filePath + radarName + date + "grid/" + mode
          if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)

          keys = DataManager.getAllDataFilePaths(filePath=filePath, radarName=radarName, date=date, mode=mode)
          for key in keys:
              radar = pyart.io.read(key)
              grid = get_grid(radar)
              pyart.io.write_grid(tmp_dir + 'grid_' + key.split("/")[-1].split(".")[0] + '.nc', grid)
              del radar, grid

      write_grid()

class Radar:

  def __init__(self, fileIndex = 0, filePath: str = DIRECTORY.FILE_PATH, radarName: str = DIRECTORY.RADAR_NAME, date: str = DIRECTORY.DATE, mode: str = DIRECTORY.MODE):
    if not DataManager.RAW_DATA:
      DataManager.RAW_DATA = DataManager.getAllDataFilePaths(filePath, radarName, date, mode)

    self.currentIndex = fileIndex
    self.getRadar()

  def getRadar(self):
    self.data = pyart.io.read(DataManager.RAW_DATA[self.currentIndex])

  def increaseIndex(self):
    self.currentIndex += 1

    if (self.currentIndex >= DataManager.NUM_OF_RAW_FILES):
      self.currentIndex = 0

  def readDataFromFilePath(self, filePath: str):
    self.data = pyart.io.read(filePath)

  def readDataFromOtherMode(self, mode: str, fileIndex: int = 0):
    data = DataManager.getAllDataFilePaths(mode = mode)
    self.data = pyart.io.read(data[fileIndex])

  def readDataFromOtherDate(self, date: str, mode: str, fileIndex: int = 0):
    data = DataManager.getAllDataFilePaths(date = date, mode=mode)
    self.data = pyart.io.read(data[fileIndex])

  def update(self):
    self.increaseIndex()
    self.getRadar()

  def get_vertices_positionX(self, indices=None):
        if indices:
            return self.data.gate_x["data"][indices]
        else:  return self.data.gate_x["data"]

  def get_vertices_positionY(self, indices=None):
      if indices:
          return self.data.gate_y["data"][indices]
      else:  return self.data.gate_y["data"]

  def get_vertices_positionZ(self, indices=None):
      if indices:
          return self.data.gate_z["data"][indices]
      else:  return self.data.gate_z["data"]

  def get_vertices_position(self, scaler):
      return scaler.fit_transform(
          np.column_stack(
              (
              self.data.gate_x["data"].flatten(),
              self.data.gate_y["data"].flatten(),
              self.data.gate_z["data"].flatten()
              )
          )
      )

  def get_all_vertices_by_threshold(self, threshold = 0):
      reflectivity = self.data.fields['reflectivity']['data'].flatten()

      indices = np.where(np.logical_and(np.logical_not(reflectivity.mask), reflectivity.data >= threshold))
      scaler = MinMaxScaler(feature_range=(-1.0, 1.0))
      vertices = self.get_vertices_position(scaler)
      return {
          'position': vertices[indices],
          'color': color(reflectivity[indices])
      }

class Grid:

  def __init__(self, fileIndex = 0, filePath: str = DIRECTORY.FILE_PATH, radarName: str = DIRECTORY.RADAR_NAME, date: str = DIRECTORY.DATE, mode: str = DIRECTORY.MODE):
    if not DataManager.GRID_DATA:
      DataManager.GRID_DATA = DataManager.getAllDataFilePaths(filePath, radarName, date, "grid/" + mode)

    self.currentIndex = fileIndex
    self.getGrid()

  def getGrid(self):
    self.data = pyart.io.read_grid(DataManager.GRID_DATA[self.currentIndex])

  def increaseIndex(self):
    self.currentIndex += 1

    if (self.currentIndex >= DataManager.NUM_OF_GRID_FILES):
      self.currentIndex = 0

  def readDataFromFilePath(self, filePath: str):
    self.data = pyart.io.read_grid(filePath)

  def readDataFromOtherMode(self, mode: str, fileIndex: int = 0):
    data = DataManager.getAllDataFilePaths(mode = "grid/" + mode)
    self.data = pyart.io.read_grid(data[fileIndex])

  def readDataFromOtherDate(self, date: str, mode: str, fileIndex: int = 0):
    data = DataManager.getAllDataFilePaths(date = date, mode="grid/" + mode)
    self.data = pyart.io.read_grid(data[fileIndex])

  def update(self):
    self.increaseIndex()
    self.getGrid()