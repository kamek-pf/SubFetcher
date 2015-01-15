import os.path
import struct

# This class gets informations based on
# the file name
class LocalVideo:

	def __init__(self, path):
		self.path = os.path.abspath(path)
		self.name = os.path.basename(self.path)
		self.noExtName = os.path.splitext(self.name)[0]
		self.dirname = os.path.dirname(self.path)
		self.size = os.path.getsize(self.path)
