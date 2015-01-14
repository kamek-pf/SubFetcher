import os.path
import struct

# This class gets informations based on
# the file name
class LocalVideo:

	def __init__(self, path):
		self.path = path
		self.name = os.path.basename(path)
		self.noExtName = os.path.splitext(self.name)[0]
		self.dirname = os.path.dirname(path)
		self.size = os.path.getsize(path)
