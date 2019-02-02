import time
#import 8051_isa

class intel_8051:
	#Implementation of a simulator for Intel's 8051
	

	def __init__(self):

		self._PC = 0x0000
		self._DP = 0
		self._isa = [0] * 0x100
		self.opcode = 0

		# ALU registers
		self.reg_A = 0
		#self.reg_B = register(8)

		# I/O
		#self.port_P0 = port(8)
		#self.port_P1 = port(8)
		#self.port_P2 = port(8)
		#self.port_P3 = port(8)

		# Memory
		self.rom = [0x74, 0xFF, 0x04, 0x14, 0x70, 0xFC, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00] # bytes
		#self.ram = ram(128)

		# Timers
		#self.timer_t0 = timer(16)
		#self.timer_t1 = timer(16)
		# Serial Transceiver
		# self.sbuf = sbuf()

		# Control registers
		#self.reg_IE = register(8, bit) # Interrupt Enable
		#self.reg_IP = register(8, bit) # Interrupt Priority
		#self.reg_PCON = register(8, bit) # Power Mode Control
		#self.reg_SCON = register(8, bit) # Serial Port Control
		#self.reg_TMOD = register(8, bit) # Timer Mode Control
		#self.reg_TCON = register(8, bit) # Timer Control

		self.init_isa()

	def step(self):
		self.opcode = self.rom[self._PC]	# Get instruction
		#print("Opcode: " + hex(self.opcode))				# Execute instruction
		instruction = self._isa[self.opcode]
		self._PC += 1						# Increment PC
		instruction()
		self._overflow_registers()

	def _overflow_registers(self):
		self._PC = self._PC & 0xFF
		self.reg_A = self.reg_A & 0xFF

	def run(self):
		while 1:
			self.print_cpu_state()
			self.step()


	def print_cpu_state(self):
		print("Opcode: " + hex(self.opcode) + " | Acc: " + str(self.reg_A) + " | PC: " + str(self._PC))

	def _nop(self):
		if (self._PC + 1) > len(self.rom):
			exit()
		else:
			pass

	def _404(self):
		print("Unimplemented Opcode: " + hex(self.opcode))

	def _mov(self):
		byte = self.rom_next_byte()
		self.reg_A = byte

	def _dec(self):
		self.reg_A -= 1


	def _inc(self):
		if self.opcode == 0x04:
			self.reg_A += 1
		else:
			pass
 
	def rom_next_byte(self):
		byte = self.rom[self._PC]
		self._PC += 1
		return byte

	def rom_next_nibble(self):
		nibble = (self.rom[self._PC + 1] << 8) + self.rom[self._PC]
		self._PC += 2
		return nibble

	def _jnz(self):
		if self.reg_A != 0x00:
			rel = self.rom_next_nibble()
			self._PC += rel
		else:
			self._PC += 1
			pass

	def init_isa(self):
		self._isa[0x00] = self._nop
		self._isa[0x01] = self._404
		self._isa[0x02] = self._404
		self._isa[0x03] = self._404
		self._isa[0x04] = self._inc
		self._isa[0x05] = self._404
		self._isa[0x06] = self._404
		self._isa[0x07] = self._404
		self._isa[0x08] = self._404
		self._isa[0x09] = self._404
		self._isa[0x0A] = self._404
		self._isa[0x0B] = self._404
		self._isa[0x0C] = self._404
		self._isa[0x0D] = self._404
		self._isa[0x0E] = self._404
		self._isa[0x0F] = self._404
		self._isa[0x10] = self._404
		self._isa[0x11] = self._404
		self._isa[0x12] = self._404
		self._isa[0x13] = self._404
		self._isa[0x14] = self._dec
		self._isa[0x15] = self._404
		self._isa[0x16] = self._404
		self._isa[0x17] = self._404
		self._isa[0x18] = self._404
		self._isa[0x19] = self._404
		self._isa[0x1A] = self._404
		self._isa[0x1B] = self._404
		self._isa[0x1C] = self._404
		self._isa[0x1D] = self._404
		self._isa[0x1E] = self._404
		self._isa[0x1F] = self._404
		self._isa[0x20] = self._404
		self._isa[0x21] = self._404
		self._isa[0x22] = self._404
		self._isa[0x23] = self._404
		self._isa[0x24] = self._404
		self._isa[0x25] = self._404
		self._isa[0x26] = self._404
		self._isa[0x27] = self._404
		self._isa[0x28] = self._404
		self._isa[0x29] = self._404
		self._isa[0x2A] = self._404
		self._isa[0x2B] = self._404
		self._isa[0x2C] = self._404
		self._isa[0x2D] = self._404
		self._isa[0x2E] = self._404
		self._isa[0x2F] = self._404
		self._isa[0x30] = self._404
		self._isa[0x31] = self._404
		self._isa[0x32] = self._404
		self._isa[0x33] = self._404
		self._isa[0x34] = self._404
		self._isa[0x35] = self._404
		self._isa[0x36] = self._404
		self._isa[0x37] = self._404
		self._isa[0x38] = self._404
		self._isa[0x39] = self._404
		self._isa[0x3A] = self._404
		self._isa[0x3B] = self._404
		self._isa[0x3C] = self._404
		self._isa[0x3D] = self._404
		self._isa[0x3E] = self._404
		self._isa[0x3F] = self._404
		self._isa[0x40] = self._404
		self._isa[0x41] = self._404
		self._isa[0x42] = self._404
		self._isa[0x43] = self._404
		self._isa[0x44] = self._404
		self._isa[0x45] = self._404
		self._isa[0x46] = self._404
		self._isa[0x47] = self._404
		self._isa[0x48] = self._404
		self._isa[0x49] = self._404
		self._isa[0x4A] = self._404
		self._isa[0x4B] = self._404
		self._isa[0x4C] = self._404
		self._isa[0x4D] = self._404
		self._isa[0x4E] = self._404
		self._isa[0x4F] = self._404
		self._isa[0x50] = self._404
		self._isa[0x51] = self._404
		self._isa[0x52] = self._404
		self._isa[0x53] = self._404
		self._isa[0x54] = self._404
		self._isa[0x55] = self._404
		self._isa[0x56] = self._404
		self._isa[0x57] = self._404
		self._isa[0x58] = self._404
		self._isa[0x59] = self._404
		self._isa[0x5A] = self._404
		self._isa[0x5B] = self._404
		self._isa[0x5C] = self._404
		self._isa[0x5D] = self._404
		self._isa[0x5E] = self._404
		self._isa[0x5F] = self._404
		self._isa[0x60] = self._404
		self._isa[0x61] = self._404
		self._isa[0x62] = self._404
		self._isa[0x63] = self._404
		self._isa[0x64] = self._404
		self._isa[0x65] = self._404
		self._isa[0x66] = self._404
		self._isa[0x67] = self._404
		self._isa[0x68] = self._404
		self._isa[0x69] = self._404
		self._isa[0x6A] = self._404
		self._isa[0x6B] = self._404
		self._isa[0x6C] = self._404
		self._isa[0x6D] = self._404
		self._isa[0x6E] = self._404
		self._isa[0x6F] = self._404
		self._isa[0x70] = self._jnz
		self._isa[0x71] = self._404
		self._isa[0x72] = self._404
		self._isa[0x73] = self._404
		self._isa[0x74] = self._mov
		self._isa[0x75] = self._404
		self._isa[0x76] = self._404
		self._isa[0x77] = self._404
		self._isa[0x78] = self._404
		self._isa[0x79] = self._404
		self._isa[0x7A] = self._404
		self._isa[0x7B] = self._404
		self._isa[0x7C] = self._404
		self._isa[0x7D] = self._404
		self._isa[0x7E] = self._404
		self._isa[0x7F] = self._404
		self._isa[0x80] = self._404
		self._isa[0x81] = self._404
		self._isa[0x82] = self._404
		self._isa[0x83] = self._404
		self._isa[0x84] = self._404
		self._isa[0x85] = self._404
		self._isa[0x86] = self._404
		self._isa[0x87] = self._404
		self._isa[0x88] = self._404
		self._isa[0x89] = self._404
		self._isa[0x8A] = self._404
		self._isa[0x8B] = self._404
		self._isa[0x8C] = self._404
		self._isa[0x8D] = self._404
		self._isa[0x8E] = self._404
		self._isa[0x8F] = self._404
		self._isa[0x90] = self._404
		self._isa[0x91] = self._404
		self._isa[0x92] = self._404
		self._isa[0x93] = self._404
		self._isa[0x94] = self._404
		self._isa[0x95] = self._404
		self._isa[0x96] = self._404
		self._isa[0x97] = self._404
		self._isa[0x98] = self._404
		self._isa[0x99] = self._404
		self._isa[0x9A] = self._404
		self._isa[0x9B] = self._404
		self._isa[0x9C] = self._404
		self._isa[0x9D] = self._404
		self._isa[0x9E] = self._404
		self._isa[0x9F] = self._404
		self._isa[0xA0] = self._404
		self._isa[0xA1] = self._404
		self._isa[0xA2] = self._404
		self._isa[0xA3] = self._404
		self._isa[0xA4] = self._404
		self._isa[0xA5] = self._404
		self._isa[0xA6] = self._404
		self._isa[0xA7] = self._404
		self._isa[0xA8] = self._404
		self._isa[0xA9] = self._404
		self._isa[0xAA] = self._404
		self._isa[0xAB] = self._404
		self._isa[0xAC] = self._404
		self._isa[0xAD] = self._404
		self._isa[0xAE] = self._404
		self._isa[0xAF] = self._404
		self._isa[0xB0] = self._404
		self._isa[0xB1] = self._404
		self._isa[0xB2] = self._404
		self._isa[0xB3] = self._404
		self._isa[0xB4] = self._404
		self._isa[0xB5] = self._404
		self._isa[0xB6] = self._404
		self._isa[0xB7] = self._404
		self._isa[0xB8] = self._404
		self._isa[0xB9] = self._404
		self._isa[0xBA] = self._404
		self._isa[0xBB] = self._404
		self._isa[0xBC] = self._404
		self._isa[0xBD] = self._404
		self._isa[0xBE] = self._404
		self._isa[0xBF] = self._404
		self._isa[0xC0] = self._404
		self._isa[0xC1] = self._404
		self._isa[0xC2] = self._404
		self._isa[0xC3] = self._404
		self._isa[0xC4] = self._404
		self._isa[0xC5] = self._404
		self._isa[0xC6] = self._404
		self._isa[0xC7] = self._404
		self._isa[0xC8] = self._404
		self._isa[0xC9] = self._404
		self._isa[0xCA] = self._404
		self._isa[0xCB] = self._404
		self._isa[0xCC] = self._404
		self._isa[0xCD] = self._404
		self._isa[0xCE] = self._404
		self._isa[0xCF] = self._404
		self._isa[0xD0] = self._404
		self._isa[0xD1] = self._404
		self._isa[0xD2] = self._404
		self._isa[0xD3] = self._404
		self._isa[0xD4] = self._404
		self._isa[0xD5] = self._404
		self._isa[0xD6] = self._404
		self._isa[0xD7] = self._404
		self._isa[0xD8] = self._404
		self._isa[0xD9] = self._404
		self._isa[0xDA] = self._404
		self._isa[0xDB] = self._404
		self._isa[0xDC] = self._404
		self._isa[0xDD] = self._404
		self._isa[0xDE] = self._404
		self._isa[0xDF] = self._404
		self._isa[0xE0] = self._404
		self._isa[0xE1] = self._404
		self._isa[0xE2] = self._404
		self._isa[0xE3] = self._404
		self._isa[0xE4] = self._404
		self._isa[0xE5] = self._404
		self._isa[0xE6] = self._404
		self._isa[0xE7] = self._404
		self._isa[0xE8] = self._404
		self._isa[0xE9] = self._404
		self._isa[0xEA] = self._404
		self._isa[0xEB] = self._404
		self._isa[0xEC] = self._404
		self._isa[0xED] = self._404
		self._isa[0xEE] = self._404
		self._isa[0xEF] = self._404
		self._isa[0xF0] = self._404
		self._isa[0xF1] = self._404
		self._isa[0xF2] = self._404
		self._isa[0xF3] = self._404
		self._isa[0xF4] = self._404
		self._isa[0xF5] = self._404
		self._isa[0xF6] = self._404
		self._isa[0xF7] = self._404
		self._isa[0xF8] = self._404
		self._isa[0xF9] = self._404
		self._isa[0xFA] = self._404
		self._isa[0xFB] = self._404
		self._isa[0xFC] = self._404
		self._isa[0xFD] = self._404
		self._isa[0xFE] = self._404
		self._isa[0xFF] = self._404

cpu = intel_8051()
cpu.run()

