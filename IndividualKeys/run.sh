#!/bin/bash


echo 'Seed: ' $1
(./seed-converter-Darwin "$1") > privKey.txt
python3 trim.py #cuts off extra words at the start of Darwin output
