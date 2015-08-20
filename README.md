# OpenStack VM Stats Collector for Splunk [![Apache License](http://img.shields.io/hexpm/l/plug.svg?style=flat)](https://git.rakuten-it.com/projects/OPENSTACK/repos/virtstat-splunk/browse/LICENSE)
===

## Description

`virtstat-splunk` are python scripts to get useful statistics (like storage, virtual cpu stats etc) out of running VMs.
The data will be output in a JSON format.

## Installation

To install, run `git clone`.

```bash
$ git clone https://git.rakuten-it.com/scm/openstack/virtstat-splunk.git
```

## Usage

Run VM via Openstack (if it is not running already) and then run the scripts.

Here is example.

```bash
$ python memory_stats.py
```

## Requirements

`Python` version is required at least Python 2.7.

