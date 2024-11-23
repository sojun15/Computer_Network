def application_layer(frame):
    print('application layer recieved',frame,'frame')
    return 1

def network_layer(frame):
    print('network layer recieved',frame,'frame')
    return application_layer(frame)

def physical_layer(frame):
    print('physical layer recieved',frame,'frame')
    return network_layer(frame)

total_frame = 5
i=0

if __name__ == '__main__':
    ack = physical_layer(frame=2)
    while i<total_frame-2:
        if ack==1:
            print()
            ack = 0
            ack = physical_layer(frame=1)
            i += 1