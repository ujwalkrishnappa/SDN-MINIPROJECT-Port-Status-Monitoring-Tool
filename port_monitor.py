from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
import datetime

class PortMonitor(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PortMonitor, self).__init__(*args, **kwargs)
        self.failure_count = 0

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        print("\n✅ Switch Connected Successfully!\n")

    @set_ev_cls(ofp_event.EventOFPPortStatus, MAIN_DISPATCHER)
    def port_status_handler(self, ev):
        msg = ev.msg
        reason = msg.reason
        port_no = msg.desc.port_no
        state = msg.desc.state

        ofproto = msg.datapath.ofproto
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        status = ""

        # Detect UP/DOWN
        if state == 1:
            status = "DOWN"
            self.failure_count += 1
            print(f"⚠️ ALERT: Port {port_no} is DOWN!")
        else:
            status = "UP"
            print(f"✅ Port {port_no} is UP!")

        # Reason type
        if reason == ofproto.OFPPR_ADD:
            change = "ADDED"
        elif reason == ofproto.OFPPR_DELETE:
            change = "DELETED"
        elif reason == ofproto.OFPPR_MODIFY:
            change = "MODIFIED"
        else:
            change = "UNKNOWN"

        log_msg = f"{time} | Port {port_no} | {status} | {change} | Failures: {self.failure_count}"
       
        print(log_msg)

        # Save logs to file
        with open("port_log.txt", "a") as f:
            f.write(log_msg + "\n")
