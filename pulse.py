import socket
import time
import threading

# Function to send a UDP packet
def send_packet(message):
    # Define the IPv6 address and port to send packets to
    server_ip = ''  # Replace with the target IPv6 address
    server_port = 12345  # Replace with the target port

    # Create a UDP socket for IPv6
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

    try:
        # Send the packet with user-defined message
        sock.sendto(message.encode(), (server_ip, server_port))
        print(f"Packet sent: {message}")
    except Exception as e:
        print(f"Error sending packet: {e}")
    finally:
        sock.close()

# Function to receive UDP messages
def receive_packet():
    # Define the local port to receive messages
    listen_port = 12345  # Replace with the same port you're using to send

    # Create a UDP socket for IPv6
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    sock.bind(('::', listen_port))  # Bind to all available interfaces

    print(f"Listening for incoming messages on port {listen_port}...")

    try:
        while True:
            # Receive the message
            data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
            print(f"Received message: {data.decode()} from {addr}")
    except Exception as e:
        print(f"Error receiving packet: {e}")
    finally:
        sock.close()

# Main function to start both sending and receiving in parallel using threads
def main():
    # Start the receiving function in a separate thread
    receive_thread = threading.Thread(target=receive_packet)
    receive_thread.daemon = True  # Allow the thread to exit when the main program exits
    receive_thread.start()
    while True:
        user_message = input("Enter the message to send over UDP: ")
        # Start sending packets periodically with user input
        send_packet(user_message)

if __name__ == '__main__':
    main()
