#!/bin/sh
#Matthew McCormick 100448975

cat $3 | tail -n +$1 | head -n -$2
