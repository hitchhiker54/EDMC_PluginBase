from config import config
from ctypes import *
import sys
import os
import plug
from threading import Thread

this = sys.modules[__name__]
this.Running = True
this.system = "This is not the System you are looking for."

class inArg(Structure):
    _fields_ = [("name", c_char_p),
                ("testVal1", c_int32),
                ("testVal2", c_float)]

def plugin_start():
	print(os.path.exists(config.plugin_dir + r'\EDMC_PluginBase\EDMC_PluginBase.dll'))
	print(os.getcwd())
	print(config.plugin_dir)
	dllpath = config.plugin_dir + r'\EDMC_PluginBase\EDMC_PluginBase.dll'
	d = dllpath.encode('ascii','ignore')
	this.dll = windll.LoadLibrary(d)

	this.dll.Init()
	
	return "EDMC_PluginBase"

def plugin_app(parent):
	this.thread = Thread(target = worker, name = 'EDMC_PluginBase worker')
	this.thread.daemon = True
	this.thread.start()
	
def plugin_stop():
	this.dll.Closing()
	this.Running = False
	this.thread.join()
	this.thread = None

def journal_entry(cmdr, is_beta, system, station, entry, state):
	arg = inArg(c_char_p(system), 42, 3.141)
	this.dll.Update(byref(arg))

def dashboard_entry(cmdr, is_beta, entry):
	dummy = 0
	# do stuff
	
def cmdr_data(data, is_beta):
	dummy = 0
	# do stuff
	
# Worker thread
def worker():
	while this.Running:
		dummy = 0
		# do stuff