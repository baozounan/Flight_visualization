import flight_attitude.receive_attitude_data as rec_att_data
import instrument_panel.receive_panel_data  as rec_pan_data
import instrument_panel.send_panel_data as sen_pan_data






if __name__ == '__main__':
    #rec_pan_data.udp_receive_message("127.0.0.1", 7080)
    #rec_att_data.udp_receive_message("127.0.0.1", 7080)
    #udp_send_message("")
    sen_pan_data.udp_send_message()


