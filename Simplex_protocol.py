import time

class Data_layer:
    def __init__(self):
        pass

    def sender(self):
        self.From_physical_layer()
        
    def From_physical_layer(self):
            print('packet come from physical layer')
            self.To_network_layer()
            
    def To_network_layer(self):
            print('packet go to network layer')
            
    def Receiver(self):
        self.From_physical_layer()
        self.Wait_for_event()
        
    def Wait_for_event(self):
            print('wait for event!')


class Physical_layer:
    packet = Data_layer()
    packet.sender()
    packet.Receiver()
