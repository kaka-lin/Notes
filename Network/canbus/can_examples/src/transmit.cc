#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <net/if.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>

#include <linux/can.h>
#include <linux/can/raw.h>

int main(int argc, char *argv[]) {
	int can_fd;
	int nbytes;
	struct sockaddr_can addr;
	struct can_frame frame;
	struct ifreq ifr; // for saving config of interface

	const char *ifname = "can0";

  // 1. Create a socket(int domain, int type, int protocol)
  //    PF_CAN or AF_CAN
	if ((can_fd = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) {
		perror("Error while Opening Socket");
		return 1;
	}

  // 2. Retrieve the interface index for the interface name
  //    ex: can0, can1, vcan0 etc
	strcpy(ifr.ifr_name, ifname);
	ioctl(can_fd, SIOCGIFINDEX, &ifr);

  // 3. Bind the socket to the CAN Interface:
  memset(&addr, 0, sizeof(addr));
	addr.can_family  = AF_CAN;
	addr.can_ifindex = ifr.ifr_ifindex;

	if (bind(can_fd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
		perror("Error in Socket bind");
		return 1;
	}

  // 4. Trnsmit CAN bus frame
  frame.can_id  = 0x123;
	frame.can_dlc = 4;
	frame.data[0] = 0xDE;
	frame.data[1] = 0xAD;
  frame.data[2] = 0xBE;
  frame.data[3] = 0x11;

	// nbytes = write(can_fd, &frame, sizeof(struct can_frame))
  if (write(can_fd, &frame, sizeof(struct can_frame)) != sizeof(struct can_frame)) {
    perror("Write");
    return 1;
  }

  // 5. Closing the socket
	if (close(can_fd) < 0) {
		perror("Close");
		return 1;
	}

	return 0;
}
