#!/usr/bin/env python2
# This needs to run under Python2.6
import sys
import fcntl

DEV = '/dev/res'
SCAN_ENABLE = 29188
SCAN_DISABLE = 29187
ADD_PID = 29189
DEL_PID = 29193
RECV_FILES = 29191
PROTECT_FILE = 29192
UNPROTECT_FILE = 29194
HIDE_FILE = 29195
UNHIDE_FILE = 29196
SET_SIGN_EXTS = 29197
GET_SIGN_EXTS = 29198

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: {s} [CMD] [ARG]'.format(s=sys.argv[0]))
        sys.exit(1)

    CMD = sys.argv[1]

    if len(sys.argv) is 3:
        ARG = sys.argv[2]
    else:
        ARG = 0

    if CMD == 'enable':
        CMD = SCAN_ENABLE
    elif CMD == 'disable':
        CMD = SCAN_DISABLE
    elif CMD == 'pid':
        CMD = ADD_PID
    elif CMD == 'unpid':
        CMD = DEL_PID
    elif CMD == 'recv':
        CMD = RECV_FILES
    elif CMD == 'protect':
        CMD = PROTECT_FILE
    elif CMD == 'unprotect':
        CMD = UNPROTECT_FILE
    elif CMD == 'hide':
        CMD = HIDE_FILE
    elif CMD == 'unhide':
        CMD = UNHIDE_FILE
    elif CMD == 'setsign':
        CMD = SET_SIGN_EXTS
    elif CMD == 'getsign':
        CMD = GET_SIGN_EXTS
    else:
        print('unknown command: {c}'.format(c=CMD))
        sys.exit(1)

    fd = open(DEV, 'wb')
    ret = fcntl.ioctl(fd, CMD, ARG)
    print(ret)
    fd.close()
