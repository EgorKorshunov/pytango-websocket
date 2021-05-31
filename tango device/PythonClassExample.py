#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        PythonClassExample.py
#
#  Project :     
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      email$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["PythonClassExample", "PythonClassExampleClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import tango
import sys
# Add additional import
#----- PROTECTED REGION ID(PythonClassExample.additionnal_import) ENABLED START -----#
import json
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
# from websocket import create_connection
# import thread
# import time
#----- PROTECTED REGION END -----#	//	PythonClassExample.additionnal_import

# Device States Description
# ON : The device works
# OFF : Calculator is off


class PythonClassExample (PyTango.Device_4Impl):
    """This class is created in order to show the functionality of Tango Controls modules"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(PythonClassExample.global_variables) ENABLED START -----#

    #----- PROTECTED REGION END -----#	//	PythonClassExample.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        PythonClassExample.init_device(self)
        #----- PROTECTED REGION ID(PythonClassExample.__init__) ENABLED START -----#

        #----- PROTECTED REGION END -----#	//	PythonClassExample.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(PythonClassExample.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PythonClassExample.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_Result_read = 0.0
        self.attr_AllResults_read = [0.0]
        #----- PROTECTED REGION ID(PythonClassExample.init_device) ENABLED START -----#
        # device_name = self.get_name()
        device_name = "PythonClassExample/FirstExample/Example"


        #----- PROTECTED REGION END -----#	//	PythonClassExample.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(PythonClassExample.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PythonClassExample.always_executed_hook

    # -------------------------------------------------------------------------
    #    PythonClassExample read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_Result(self, attr):
        self.debug_stream("In read_Result()")
        #----- PROTECTED REGION ID(PythonClassExample.Result_read) ENABLED START -----#
        attr.set_value(self.attr_Result_read)
        # asyncio.get_event_loop().run_until_complete(attribute_change("Result", self.attr_Result_read))
        #----- PROTECTED REGION END -----#	//	PythonClassExample.Result_read
        
    def write_Result(self, attr):
        self.debug_stream("In write_Result()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(PythonClassExample.Result_write) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PythonClassExample.Result_write
        
    def read_AllResults(self, attr):
        self.debug_stream("In read_AllResults()")
        #----- PROTECTED REGION ID(PythonClassExample.AllResults_read) ENABLED START -----#
        attr.set_value(self.attr_AllResults_read)
        
        #----- PROTECTED REGION END -----#	//	PythonClassExample.AllResults_read
        
    def write_AllResults(self, attr):
        self.debug_stream("In write_AllResults()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(PythonClassExample.AllResults_write) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PythonClassExample.AllResults_write
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(PythonClassExample.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PythonClassExample.read_attr_hardware


    # -------------------------------------------------------------------------
    #    PythonClassExample command methods
    # -------------------------------------------------------------------------
    
    def Add(self, argin):
        """ Add two numbers
        :param argin: 
        :type argin: PyTango.DevVarDoubleArray
        :rtype: PyTango.DevDouble
        """
        self.debug_stream("In Add()")
        argout = 0.0
        #----- PROTECTED REGION ID(PythonClassExample.Add) ENABLED START -----#
        argout = argin[0] + argin[1]
        value = str(argout)
        ws.send("[\"PythonClassExample/FirstExample/Example/attribute/Result\",\"attribute_value\", \"" + value + "\"]")
        self.attr_Result_read = argout
        # asyncio.get_event_loop().run_until_complete(execute_command("Add"))
        # ws = create_connection("ws://localhost:8080")
        # print("Sending 'Hello, World'...")
        # ws.send(str(argout))
        #----- PROTECTED REGION END -----#	//	PythonClassExample.Add
        return argout
        
    def Subtract(self, argin):
        """ Subtract one number from another
        :param argin: 
        :type argin: PyTango.DevVarDoubleArray
        :rtype: PyTango.DevDouble
        """
        self.debug_stream("In Subtract()")
        argout = 0.0
        #----- PROTECTED REGION ID(PythonClassExample.Subtract) ENABLED START -----#
        argout = argin[0] - argin[1]
        self.attr_Result_read = argout
        #----- PROTECTED REGION END -----#	//	PythonClassExample.Subtract
        return argout
        
    def Multiply(self, argin):
        """ Multiply two numbers
        :param argin: 
        :type argin: PyTango.DevVarDoubleArray
        :rtype: PyTango.DevDouble
        """
        self.debug_stream("In Multiply()")
        argout = 0.0
        #----- PROTECTED REGION ID(PythonClassExample.Multiply) ENABLED START -----#
        argout = argin[0] * argin[1]
        self.attr_Result_read = argout
        #----- PROTECTED REGION END -----#	//	PythonClassExample.Multiply
        return argout
        
    def Divide(self, argin):
        """ Divide one number by another
        :param argin: 
        :type argin: PyTango.DevVarDoubleArray
        :rtype: PyTango.DevDouble
        """
        self.debug_stream("In Divide()")
        argout = 0.0
        #----- PROTECTED REGION ID(PythonClassExample.Divide) ENABLED START -----#
        argout = argin[0] / argin[1]
        self.attr_Result_read = argout
        #----- PROTECTED REGION END -----#	//	PythonClassExample.Divide
        return argout
        
    def CalculateAll(self, argin):
        """ Perform all actions in one
        :param argin: 
        :type argin: PyTango.DevVarDoubleArray
        :rtype: PyTango.DevVarDoubleArray
        """
        self.debug_stream("In CalculateAll()")
        argout = [0.0]
        #----- PROTECTED REGION ID(PythonClassExample.CalculateAll) ENABLED START -----#
        argout = [argin[0] + argin[1], argin[0] - argin[1], argin[0] * argin[1], argin[0] / argin[1]]
        self.attr_AllResults_read = argout
        #----- PROTECTED REGION END -----#	//	PythonClassExample.CalculateAll
        return argout
        

    #----- PROTECTED REGION ID(PythonClassExample.programmer_methods) ENABLED START -----#

    #----- PROTECTED REGION END -----#	//	PythonClassExample.programmer_methods

class PythonClassExampleClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(PythonClassExample.global_class_variables) ENABLED START -----#

    #----- PROTECTED REGION END -----#	//	PythonClassExample.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        'Add':
            [[PyTango.DevVarDoubleArray, "none"],
            [PyTango.DevDouble, "none"]],
        'Subtract':
            [[PyTango.DevVarDoubleArray, "none"],
            [PyTango.DevDouble, "none"]],
        'Multiply':
            [[PyTango.DevVarDoubleArray, "none"],
            [PyTango.DevDouble, "none"]],
        'Divide':
            [[PyTango.DevVarDoubleArray, "none"],
            [PyTango.DevDouble, "none"]],
        'CalculateAll':
            [[PyTango.DevVarDoubleArray, "none"],
            [PyTango.DevVarDoubleArray, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        'Result':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE]],
        'AllResults':
            [[PyTango.DevDouble,
            PyTango.SPECTRUM,
            PyTango.READ_WRITE, 4]],
        }

# async def hello(device_name):
#     uri = "ws://localhost:3000"
#     async with websockets.connect(uri) as websocket:
#         await websocket.send(device_name + " says: Hello world!")
#         await websocket.recv()
#
# async def attribute_change(attribute, value):
#     uri = "ws://localhost:3000"
#     async with websockets.connect(uri) as websocket:
#         await websocket.send(attribute + " changed to " + value)
#         await websocket.recv()
#
# async def execute_command(command):
#     uri = "ws://localhost:3000"
#     async with websockets.connect(uri) as websocket:
#         await websocket.send("Command " + command + " was executed")
#         await websocket.recv()
#
# asyncio.get_event_loop().run_until_complete(hello("None"))

def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(PythonClassExampleClass, PythonClassExample, 'PythonClassExample')
        #----- PROTECTED REGION ID(PythonClassExample.add_classes) ENABLED START -----#

        #----- PROTECTED REGION END -----#	//	PythonClassExample.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

def on_message(ws, message):
    print(message)

ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:3000/")
ws.send("[\"device_connect\",\"PythonClassExample/FirstExample/Example\"]")
ws.send("[\"PythonClassExample/FirstExample/Example/attribute/Result\",\"attribute_value\", \"0\"]")


if __name__ == '__main__':
    main()

