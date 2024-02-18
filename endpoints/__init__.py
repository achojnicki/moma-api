from endpoints import (
    login,
    logout,
    )

class Endpoints(login.login,
    logout.logout,
    ):

    def __init__(self, root):
        self._root=root

        self._middlewares=root.middlewares
        self._log_handle=root.log_handle

        self._endpoints_with_required_login=[
            self.logout,
            ]