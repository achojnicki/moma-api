from .auth import Auth

class Middlewares:
	def __init__(self, root):
		self._root=root

		self.auth=Auth(root)