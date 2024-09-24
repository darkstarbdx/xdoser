# XdoseR

XdoseR is a powerful multi-threaded HTTP request tool designed for performance and stress testing of web servers. This tool enables users to send a high volume of concurrent requests to a specified URL, simulating user behavior while allowing for customization of request headers and user agents.

## Features

- **Multi-threaded Requests**: Easily simulate multiple users with concurrent requests to test server load.
- **Customizable Headers**: Modify HTTP headers to mimic real browser requests for better accuracy.
- **Random User Agents**: Automatically rotate through a list of user agents to minimize the risk of detection and blocking.
- **Graceful Shutdown**: Stop the script safely using `Ctrl + C`, ensuring all threads terminate properly.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/darkstarbdx/xdoser.git
   cd xdoser
   ```

2. **Run the Script**:
   ```bash
   python3 xdoser.py
   ```

3. **Follow the Prompts**: Enter the target URL and specify the number of threads you wish to use.

## Disclaimer

**Use responsibly and only on systems you own or have explicit permission to test. Unauthorized use may violate terms of service and local laws.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
