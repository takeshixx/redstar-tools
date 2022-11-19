# Tools for Red Star OS (붉은별)

This repository includes several binaries from and tools for Red Star OS. These can be used for further research work.

## Disable malicious components

The easiest way is to run the `defuse.sh` script on Red Star OS 3.0 Desktop (requires root privileges), make sure it's executable by running `chmod u+x defuse.sh`.

### Manual steps

1. Get root privileges via `/usr/sbin/rootsetting`
2. Disable SELinux

    SELinux protects several files an directories (e.g. /var/log). It should be disabled in order to make changes to some parts of the system.

        setenforce 0

    In order to keep SELinux disabled after rebooting, append `selinux=0` to the kernel line in the GRUB config file (/boot/grub/grub.conf).

3. Kill `securityd`

    Killing `securityd` will prevent the system from rebooting when editing/deleting various protected files.

        killall -9 securityd

4. Disable `rtscan` kernel module

    Either via `resctl.py` (see `rtscan`) or via a Python shell as follows:

        [root@localhost ~]# python
        Python 2.6 (r26:66714, Oct  7 2012, 13:39:47)
        [GCC 4.4.0 20090506 (Red Hat 4.4.0-4)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import fcntl
        >>> fcntl.ioctl(open('/dev/res', 'wb'), 29187)
        0

    After disabling `rtscan` protected processes like `opprc` will become killable.

5. Kill `scnprc` and `opprc`

        killall scnprc
        killall opprc

6. Replace `/usr/lib/libos.so.0.0.0`

    See `libos` for further information. Replacing this file will prevent the system from rebooting via `securityd` after rebooting the system. It also will prevent reboot loops by `kdm` rendering the system unusable.

7. Delete `/usr/share/autostart/scnprc.desktop`

    Deleting this file will prevent `kdeinit` from starting the framework after a system reboot.

8. Delete `/etc/init/ctguard.conf`

    Deleting this file will prevent `init` from starting `opprc` even when `scnprc` is not running.

9. Reboot the system

## Debugging

### Prepare building environment

The default installation of Red Star OS 3.0 Desktop does not include GCC but the ISO includes the required packages.

1. Insert the Red Star OS ISO into the system
2. Go to `/media/RedStar\ Desktop\ 3.0/RedStar/RPMS`
3. Install the following packages:

        yum localinstall glibc-headers-2.10.1-2.i386.rpm
        yum localinstall glibc-devel-2.10.1-2.i386.rpm
        yum localinstall ncurses-devel-5.6-0.rs3.0.i386.rpm
        yum localinstall gcc-4.4.0-4.i386.rpm

Now it is possible to build a recent (e.g. the latest) version of GDB for better debugging.

### Install non-stripped threading libraries

The default installation of Red Star OS 3.0 Desktop does not allow to debug threads with the shipped version of GDB in e.g. `scnprc` and `opprc` because the required `libpthread.so.0` library is stripped.

Use the `libpthread-2.10.1.so`/`libpthread.so.0` and `libthread_db-1.0.so`/`libthread_db.so.1` libraries from the `glibc-2.10.1-2.i686.rpm` package of [Fedora 11](http://rpm.pbone.net/index.php3/stat/4/idpl/18887613/dir/fedora_11/com/glibc-2.10.1-2.i686.rpm.html).

## Disclaimer

All of the information is based on research dedicated to analyzing Red Star OS. The authors take no responsibility for the accuracy, completeness or quality of the information provided.
