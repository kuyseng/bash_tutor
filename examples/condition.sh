#!/bin/bash

number=$1

if [ $number -eq 1 ]; then
  result=one;
elif [ $number = "2" ]; then
  result="two";
else
  result="more";
fi

echo "That number is $result"



