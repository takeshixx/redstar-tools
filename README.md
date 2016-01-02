# Tools for Red Star OS (붉은별)

This repository includes several binaries from and tools for Red Star OS. These can be used for further research work.

## Disable malicious components

1. Get root privileges via `/usr/sbin/rootsetting`
2. Kill `securityd`

    Killing `securityd` will prevent the system from rebooting when editing/deleting various protected files.

        killall -9 securityd

3. Disable `rtscan` kernel module

    Either via `resctl.py` (see `rtscan`) or via a Python shell as follows:

        [root@localhost ~]# python
        Python 2.6 (r26:66714, Oct  7 2012, 13:39:47)
        [GCC 4.4.0 20090506 (Red Hat 4.4.0-4)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import fcntl
        >>> fcntl.ioctl(open('/dev/res', 'wb'), 29187)
        0

    After disabling `rtscan` protected processes like `opprc` will become killable.

4. Kill `scnprc` and `opprc`

        killall scnprc
        killall opprc

5. Replace `/usr/lib/libos.so.0.0.0`

    See `libos` for further information. Replacing this file will prevent the system from rebooting via `securityd` after rebooting the system. It also will prevent reboot loops by `kdm` rendering the system unusable.

6. Delete `/usr/share/autostart/scnprc.desktop`

    Deleting this file will prevent `kdeinit` from starting the framework after a system reboot.

7. Reboot the system

## Disclaimer

All of the information is based on research dedicated to analyzing Red Star OS. The authors take no responsibility for the accuracy, completeness or quality of the information provided.
