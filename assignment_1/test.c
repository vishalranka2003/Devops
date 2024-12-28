#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>

#define BUFFER_SIZE 32

int main(int argc, char* argv[]) {
  char ip[16];
  char hostname[BUFFER_SIZE];

  printf("Enter an IP address: ");
  
  fgets(ip, sizeof(ip), stdin)

  struct in_addr addr;
  if (inet_pton(AF_INET, ip, &addr) != 1) {
    printf("Invalid IP address\n");
    return 1;
  }

  struct hostent* host = gethostbyaddr((const void*)&addr, sizeof(addr), AF_INET);
  if (host == NULL) {
    printf("Error looking up hostname\n");
    return 1;
  }

  strcpy(hostname, host->h_name);  // CWE-119: Buffer Overflow
  printf("Hostname: %s\n", hostname);

  return 0;
}