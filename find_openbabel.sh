#!/bin/bash
locations=dpkg -L openbabel
for word in $( locations );
do	
	echo $word
	list=ls $word
	echo $list
done