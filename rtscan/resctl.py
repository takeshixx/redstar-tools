#!/usr/bin/env python2
from fcntl import ioctl

filename = '/dev/res'
fd = open(filename, 'wb')
ret = ioctl(fd, 29187, 0)

if ret is not 0:
    print('Error')

fd.close()
