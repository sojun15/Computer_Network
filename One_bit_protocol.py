def Receiver(number):
    print('receiver receive bit:',number)

    # send acknowledge for sending the next bit 
    return number+1


def Sender():
    i=1
    while(1):
        if i==1:
            print('sender send bit number:',i)
            ack = Receiver(i)
        print('acknowledge received for sending bit:',ack)
        i+=1
        if ack==i:
            print('sender send bit number:',i)
            ack = Receiver(i)
        
        if i==5:
            break

if __name__=='__main__':
    Sender()