#! /usr/bin/python

# Copyright (c) 2016, Vinicius de Avila Jorge. All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the FreeBSD Project.

import time
import subprocess
import os

# Anyone can change the parameters below to fit better one needs. The values below are good for me, what doesn't mean that they are good for you ;).
# Check current value from Light sensor via terminal: 
# cat /sys/devices/platform/applesmc.768/light
# sensor outputs 0-255

sensor_threshold = 20
#keyboard backlight: 0 = off & 255 = max. 60 is not too bright according to my taste
on_brightness = 60
off_brightness = 5

def adjust_brightness():
    while True:
        out = subprocess.check_output(["cat", "/sys/devices/platform/applesmc.768/light"])
        out = out[1:-4]
        if int(out) < sensor_threshold:
            adj = on_brightness
        if int(out) >= sensor_threshold:
            adj = off_brightness
      
        os.system("echo " + str(adj) + " > /sys/devices/platform/applesmc.768/leds/smc\:\:kbd_backlight/brightness")
        time.sleep(3)
    
adjust_brightness()
