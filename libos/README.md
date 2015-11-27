# libos

## Compile

1. gcc -c -Wall -Werror -fpic libos.c
2. gcc -shared -o libos.so.0.0.0 libos.o

## Install

1. Move new libos.so.0.0.0 to /usr/lib/libos.so.0.0.0
2. Link /usr/lib/libos.so.0.0.0 to /usr/lib/libos.so.0
