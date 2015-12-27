# libos

`libos.so.0.0.0` is the original libos file from Red Star OS 3.0 Desktop.

## Compile custom libos

1. gcc -c -Wall -Werror -fpic libos.c
2. gcc -shared -o libos.so.0.0.0 libos.o

## Install custom libos

1. Move new libos.so.0.0.0 to /usr/lib/libos.so.0.0.0
2. Link /usr/lib/libos.so.0.0.0 to /usr/lib/libos.so.0
