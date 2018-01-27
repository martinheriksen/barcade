"""
This file is part of Barcade.

Barcade is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Barcade is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Barcade.  If not, see <http://www.gnu.org/licenses/>.
"""
import os

# Requires that the settings are injected as a static class variable before
# execute is called
class Emulator:

	# Curretnly the emulator class is very primitive, and there is no
	# subclassing. But to prepare that it may become more complex with
	# various emulator subclasses. If all consumers just use this 
	# factory method, and there is an execute method in all of them
	# then the imapct is small when that change comes.
	@staticmethod
	def factory(type):
		emulator = Emulator()
		emulator.type = type
		return emulator


	def execute(self, args):
		argString = " -rompath " + Emulator.settings[self.type]['rom_path'] + " " + args[0]

		print argString

		os.system(Emulator.settings[self.type]['exe_path'] + argString)

		"""
		try:
			os.spawnv(os.P_WAIT, Emulator.settings[self.type]['exe_path'], argString)
		except os.error:
			print "error"
		"""



