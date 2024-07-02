#!/bin/bash

if [[ $(id -u) != "0" ]]; then
  echo "This script needs to run as root"
  exit
fi

function start {
  for i in {01..03}; do
    virsh start k8s-node$i
    echo "Starting k8s-node$i ..."
    sleep 10
  done
}

function stop {
  for i in {01..03}; do
    virsh shutdown k8s-node$i
    echo "Shutting down k8s-node$i..."
    sleep 10
  done
}

if [[ $1 == "start" ]]; then
  start
elif [[ $1 == "stop" ]]; then
  stop
else
  echo "Please select valid option"
  echo "Valid options are \"start\" and \"stop\""
fi
