import time
def application_layer(frame):
    time1 = time.time();
    print('application layer recieved frame:',frame)
    
    # application_layer task starts here
    # ........
    # application layer task ends here
    
    time2 = time.time();
    time_difference = time2-time1
    print('difference time:',time_difference)
    if time_difference<1:
        return 1
    else:
        return -1

def network_layer(frame):
    print('network layer recieved frame:',frame)
    return application_layer(frame)

def physical_layer(frame):
    print('physical layer recieved frame:',frame)
    return network_layer(frame)

total_frame = [1,4,2,6,9]
i=0

if __name__ == '__main__':
    
    while i<len(total_frame)-1:
        if i==0:
            ack = physical_layer(total_frame[i])
            print('acknowledge recieved for next frame:',ack)
        
        if ack==1:
            print('acknowledge recieved for next frame')
            i += 1
            ack = physical_layer(total_frame[i])
            
        elif ack==-1:
            print('acknowledge recieved for currupted frame')
            ack = physical_layer(total_frame[i])