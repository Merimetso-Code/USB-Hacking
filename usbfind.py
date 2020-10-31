#
#   This is the USB profiling tool for USD devices
#       Program Name:               usbfind.py
#       Program Version Number:     1.0
#       Author(s):                  ab@merimetso.net
#       Date:                       31st October 2020
#
#
import sys
import usb.core
#
from objbrowser import browse
#
#
#
def usage():
    print("\nProgram: usbfind.py - Version: 1.0 - Author: ab@merimetso.net - Date: 2020/10/21")
    print("")
    print("USAGE: usbfind.py [-h] [-v] [-s bus:device] [-b backend]")
    print("")
    print(" Optional Arguments:")
    print("    -h    Show this help message and exit.")
    print("    -v    Display verbose USB information. Please note this argument overrules -s")
    print('    -s    Specify a specific USB device to profile. The device must be specified as a bus:devic')
    print('              For example, you can profile the device locate at BusID:001 and DeviceID:006 as')
    print('              $ python usbfind.py -s 001:006. Please note numbers must be decimal.')
    print('    -b     Specify the backend responsible for process USB API calls. For example to use the ')
    print('              /usr/lib/libusb-1.0.so  backend we would specify $ python usbfind.py -b 1')
    print('EXAMPLE:')
    print('    To produce a verbose profile of the device locate at BusID:002 and DeviceID:005 using the ')
    print('    libusb backend to process all USB API calls we would use the following:')
    print('        $ python usbfind.py -v -s 002:005 -b 1')
    print("")
    sys.exit(0)
#
#
#
def main():
    print("\nRunning USB Profiling Tool - Version: 1.0 - Author:ab@merimetso.net\n")
    if BackEnd != 'NONE':
        try:
            if str(BackEnd) == '1':
                backnd = usb.backend.libusb1.get_backend(find_library=lambda x: "/usr/lib/libusb-1.0.so")
                bsses = usb.busses(backend=backnd)
            else:
                print('ERROR: Attempt to use unkown USB backend.')
                sys.exit(0)
        except:
            print('ERROR: Error Processing Backend Request.')
            sys.exit(0)
    else:
        bsses = usb.busses()
    #
    for bus in bsses:

        for device in bus.devices:
            if Verbose == True:
                print(device.dev)
            else:
                if Busses == 'NONE':
                    print('Bus Location    : ' + str(hex(bus.location)))
                    print('Manufacturer    : ' + str(hex(device.iManufacturer)))
                    print('Product         : ' + str(hex(device.iProduct)))
                    print('Device Class    : ' + str(hex(device.deviceClass)))
                    print('Device Protocol : ' + str(hex(device.deviceProtocol)))
                    print('Device SubClass : ' + str(hex(device.deviceSubClass)))
                    print('Device Version  : ' + str(device.deviceVersion))
                    print('Device DevNum   : ' + str(hex(device.devnum)))
                    print('Device Filename : ' + str(device.filename))
                    print('Serial Number   : ' + str(hex(device.iSerialNumber)))
                    print('Product ID      : ' + str(hex(device.idProduct)))
                    print('Vendor ID       : ' + str(hex(device.idVendor)))
                    print('Max Packet Size : ' + str(hex(device.maxPacketSize)))
                    print('USB Version     : ' + str(device.usbVersion))
                    print('')
                else:
                    try:
                        busID = int(Busses.split(':')[0])
                        venID = int(Busses.split(':')[1])
                        if (busID == int(bus.location) and venID == int(device.idProduct)):
                            print('Bus Location    : ' + str(hex(bus.location)))
                            print('Manufacturer    : ' + str(hex(device.iManufacturer)))
                            print('Product         : ' + str(hex(device.iProduct)))
                            print('Device Class    : ' + str(hex(device.deviceClass)))
                            print('Device Protocol : ' + str(hex(device.deviceProtocol)))
                            print('Device SubClass : ' + str(hex(device.deviceSubClass)))
                            print('Device Version  : ' + str(device.deviceVersion))
                            print('Device DevNum   : ' + str(hex(device.devnum)))
                            print('Device Filename : ' + str(device.filename))
                            print('Serial Number   : ' + str(hex(device.iSerialNumber)))
                            print('Product ID      : ' + str(hex(device.idProduct)))
                            print('Vendor ID       : ' + str(hex(device.idVendor)))
                            print('Max Packet Size : ' + str(hex(device.maxPacketSize)))
                            print('USB Version     : ' + str(device.usbVersion))
                            print('')
                    except:
                        print('ERROR: Error process Bus ID and Vendor ID.')
                        sys.exit(0)
#
#
#
def mmember(argList, member):
    counter = 0
    for item in argList:
        if argList[counter] == member: return True, counter
        counter = counter + 1
    return False, -1


#
#
#
if __name__ == "__main__":
    Verbose = False
    Busses = 'NONE'
    BackEnd = 'NONE'
    #
    if len(sys.argv) == 1:
        main()
        sys.exit(0)
    else:
        sys.argv.pop(0)
    #
    try:
        memTruth, index = mmember(sys.argv, '-v')
        if memTruth:
            sys.argv.pop(index)
            Verbose = True
    except:
        print('ERROR: Error processing "-v" argument in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
    #

    memTruth, index = mmember(sys.argv, '-h')
    if memTruth:
        sys.argv.pop(index)
        usage()
        sys.exit(0)

    #
    try:
        memTruth, index = mmember(sys.argv, '-s')
        if memTruth:
            sys.argv.pop(index)
            Busses = sys.argv.pop(index)
    except:
        print('ERROR: Error processing the "-s" argument in the command line.')
        sys.exit(0)
    #
    try:
        memTruth, index = mmember(sys.argv, '-b')
        if memTruth:
            sys.argv.pop(index)
            BackEnd = sys.argv.pop(index)
    except:
        print('ERROR: Error processing the "-b" argument in the command line.')
        sys.exit(0)
    #
    if len(sys.argv) == 0:
        main()
        sys.exit(1)
    else:
        print('ERROR: There is an illegal parameter in the command line.')
        print('       If you need to see the help page then use the "-h" option.\n')
        sys.exit(0)
#
#
#
# The End of the FINDUSB.PY Program.
#

