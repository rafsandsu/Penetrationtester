#!/bin/bash

for ip in $(seq 1 254):
do for ip1 in $(seq 1 254):
	do host 199.17.$ip.$ip1 | grep "domain name pointer"
done
done > ips_reverse.txt

