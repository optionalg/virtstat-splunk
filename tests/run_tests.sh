#! /bin/bash

cd `dirname $0`
cd ..

flake8 .
./bin/block_info.py
./bin/block_stats.py
./bin/memory_stats.py
./bin/interface_stats.py
./bin/vcpus.py
