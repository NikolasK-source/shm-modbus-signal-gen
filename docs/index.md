# SHM-Modbus signal generator

This tool is a system time based signal generator for [stdin-to-modbus-shm](https://nikolask-source.github.io/stdin_to_modbus_shm/)

## Use the Application

The tool outputs values based on the following equation:
```
f(x = time.time()) = offset + scale * function((x + time-offset) * speed)
```

The constants ```offset```, ```scale```, ```time-offset``` and ```speed``` are specifed via command line arguments.

The value is generated at a configurable interval and can be written to multiple modbus registers of the same type.

### Example
The following writes a sine signal as 32 bit float to ```0x42@AO```.
The value is calculated evry 0.1 seconds.
```
shm-modbus-signal-gen -d 0.1 -e f32l sin ao 0x42 | stdin-to-modbus-shm
```

## Install

It is possible to use the python script ```src/signalgen.py``` without installation.

### Using the Arch User Repository (recommended for Arch based Linux distributions)
The application is available as [shm-modbus-signal-gen](https://aur.archlinux.org/packages/shm-modbus-signal-gen) in the [Arch User Repository](https://aur.archlinux.org/).
See the [Arch Wiki](https://wiki.archlinux.org/title/Arch_User_Repository) for information about how to install AUR packages.

## Links to related projects

### General Shared Memory Tools
- [Shared Memory Dump](https://nikolask-source.github.io/dump_shm/)
- [Shared Memory Write](https://nikolask-source.github.io/write_shm/)
- [Shared Memory Random](https://nikolask-source.github.io/shared_mem_random/)

### Modbus Clients
- [RTU](https://nikolask-source.github.io/modbus_rtu_client_shm/)
- [TCP](https://nikolask-source.github.io/modbus_tcp_client_shm/)

### Modbus Shared Memory Tools
- [STDIN to Modbus](https://nikolask-source.github.io/stdin_to_modbus_shm/)


## License

MIT License

Copyright (c) 2023 Nikolas Koesling

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

