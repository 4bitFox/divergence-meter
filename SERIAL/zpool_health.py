#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import json
import glob
from time import sleep

SERIAL_PATH = "/dev/serial/by-id/*Divergence_Meter*"



while True:
    serial_path = glob.glob(SERIAL_PATH)
    if serial_path:
        serial_path = serial_path[0]

        status_json_string = subprocess.run(
            ["zpool", "status", "-j"],
            capture_output=True,
            text=True
        ).stdout

        status_data = json.loads(status_json_string)

        instructions_nixie = []
        for pool_data in status_data["pools"].values():
            # print(pool_data)
            # print()
            print("NAME:", pool_data["name"])
            print("STATE:", pool_data["state"])
    
            if pool_data["state"] == "ONLINE":
                state = 0
                duration = 1
                flashes = 1
            elif pool_data["state"] == "DEGRADED":
                state = 1
                duration = 2
                flashes = 3
            elif pool_data["state"] == "FAULTED":
                state = 2
                duration = 3
                flashes = 3
            else:
                state = 9
                duration = 3
                flashes = 3
    
    
            error_count = 0
            for raidz in pool_data["vdevs"][pool_data["name"]]["vdevs"].values():
                for vdev in raidz["vdevs"].values():
                    read_errors = int(vdev["read_errors"])
                    write_errors = int(vdev["write_errors"])
                    checksum_errors = int(vdev["checksum_errors"])
                    print("- DRIVE:", vdev["name"], read_errors, write_errors, checksum_errors)
                    error_count += read_errors + write_errors + checksum_errors
            print("TOTAL ERROR COUNT:", error_count)
    
            if error_count > 9999999:
                error_count_string_7c = "9999999"
            else:
                error_count_string_7c = f"{error_count:07d}"
            nixie_state = [state, 
                           int(error_count_string_7c[0]), 
                           int(error_count_string_7c[1]), 
                           int(error_count_string_7c[2]), 
                           int(error_count_string_7c[3]), 
                           int(error_count_string_7c[4]), 
                           int(error_count_string_7c[5]), 
                           int(error_count_string_7c[6])]
                    
            for flash in range(flashes):
                instructions_nixie.append([nixie_state, [None, 1], duration])
                if flashes != flash + 1: # don't wait when done
                    instructions_nixie.append([[None, None, None, None, None, None, None, None], [None, None], 1])
        
        instructions_nixie = str(instructions_nixie)
        print(instructions_nixie)
        
        try:
            with open(serial_path, "w") as serial:
                serial.write(instructions_nixie + "\n")
        except OSError:
            pass
    
    sleep(60)
    
