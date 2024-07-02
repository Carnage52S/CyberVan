import java.net.InetSocketAddress;
import java.net.Socket;
import java.io.IOException;

public class PortScanner {
    
    // Method to check if a port is open
    public static boolean isPortOpen(String ip, int port, int timeout) {
        try (Socket socket = new Socket()) {
            socket.connect(new InetSocketAddress(ip, port), timeout);
            return true;
        } catch (IOException e) {
            return false;
        }
    }

    // Main method to scan a range of ports
    public static void main(String[] args) {
        String ip = "127.0.0.1"; // IP address to scan
        int timeout = 200; // Timeout for each port scan in milliseconds

        // Scan ports from 1 to 1024
        for (int port = 1; port <= 1024; port++) {
            if (isPortOpen(ip, port, timeout)) {
                System.out.println("Port " + port + " is open");
            } else {
                System.out.println("Port " + port + " is closed");
            }
        }
    }
}
