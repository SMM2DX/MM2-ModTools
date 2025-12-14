from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QPushButton

class QActionButton(QPushButton):
	def __init__(self, action: QAction):
		super().__init__()
		self.addAction(action)
	def addAction(self, action: QAction) -> None:
		self.setText(action.text())
		self.setIcon(action.icon())
		self.setStatusTip(action.statusTip())
		self.pressed.connect(action.trigger)