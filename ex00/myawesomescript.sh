#!/bin/sh

if [ "$#" -eq 1 ]; then
	curl -I -s "$1" | grep -i location | cut -d ' ' -f 2
fi
