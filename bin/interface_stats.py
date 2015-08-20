#! /usr/bin/python

import common
import libvirt
import json

# LOG = common.get_logger("interface_stats")

try:
    conn = libvirt.openReadOnly()
    if conn is None:
        raise Exception('Failed to open connection to the hypervisor')

    for id in conn.listDomainsID():
        dom = conn.lookupByID(id)

        interface_stats = {}
        for dev in common.domain_xml(dom).findall("devices/interface/target"):
            devname = dev.get("dev")
            stats = dom.interfaceStats(devname)
            interface_stats[devname] = {
                "rx_bytes": stats[0],
                "rx_packets": stats[1],
                "rx_errs": stats[2],
                "rx_drop": stats[3],
                "tx_bytes": stats[4],
                "tx_packets": stats[5],
                "tx_errs": stats[6],
                "tx_drop": stats[7]
            }
            print json.dumps({
                "timestamp": common.now(),
                "nova": common.nova_metadata(dom),
                "uuid": dom.UUIDString(),
                "name": dom.name(),
                "id": dom.ID(),
                "interface_stats": interface_stats
            })

except Exception, e:
    print json.dumps({"timestamp": common.now(), "error": "%s" % e})
