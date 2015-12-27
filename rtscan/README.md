# Interact with `rtscan`

`resctl.py` can be used to interact with `rtscan` kernel module via ioctl calls to `/dev/res`. `rtscan.ko` is the original kernel module from Red Star OS 3.0 Desktop.

*Note*: On Red Star 3.0 this needs to be executed with root privileges.

## Usage Examples

### Disable/Enable `rtscan`

```
# python resctl.py disable
```
```
# python resctl.py enable
```

### Protect/Hide a File

The following example adds a new file extension to the list of scanned extensions and a new file to the protected and hidden files:

```
# cat /tmp/secret.32c3
Kim loves Katy
# python resctl.py setsign .32c3
# python resctl.py protect /tmp/secret.32c3
# python resctl.py hide /tmp/secret.32c3
# cat /tmp/secret.32c3
cat: /tmp/secret.32c3: Operation not permitted
```

Disabling `rtscan` will make the file readable again:

```
# python resctl.py disable
# cat /tmp/secret.32c3
Kim loves Katy
```

*Note*: The default list of extensions added by `opprc`:

```
.mpg.dat.avi.vob.gif.doc.pdf.ppt.xls.mp3.wav.mpa.wma.asf.mp2..jpg.bmp.png.tif.jpeg.tiff.mov.wmv.mp4.rm.rmv.rmvb.swf.flv.3gp.chm..djuv.djv.caj.kdh.teb.nh.caa.docx.xlsx.pptx.txt.htm.html.mht.hwp.pdg.
```
