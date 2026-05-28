/**
 * Buffer utilities — intentionally vulnerable for VulnScout testing.
 */
#include <cstring>
#include <cstdio>

void copy_data(char *input) {
    char buffer[64];
    // Buffer overflow via strcpy
    strcpy(buffer, input);
}

void format_string(char *user, char *ip) {
    char log[256];
    // Buffer overflow via sprintf
    sprintf(log, "User: %s from IP: %s", user, ip);
}

void read_input() {
    char buf[128];
    // Unsafe gets()
    gets(buf);
}

int add(int a, int b) {
    // Safe
    return a + b;
}
