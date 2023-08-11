# Zscaler SDK (zsdk)

The Zscaler SDK (zsdk) is a Python library designed to provide an easy and programmatic way to interact with publicly available Zscaler API endpoints. With zsdk, developers can manage and automate tasks across Zscaler's suite of security services, including Zscaler Internet Access (ZIA), Zscaler Private Access (ZPA), and Zscaler Digital Experience (ZDX).

## Features

- Comprehensive coverage of Zscaler's public API.
- Easy-to-use Pythonic interfaces.
- Examples and guides to get started quickly.

## Installation

You can install zsdk via pip:

```bash
pip install zsdk
```

## Getting Started

Here's a quick example to get you started with ZIA:

```python
from zsdk.zia import zia
zscaler = zia(username='YOUR_USERNAME', password='YOUR_PASSWORD', api_key='YOUR_API_KEY', cloud_name="zscaler.net")
print(zscaler.locations.list())
```

See the [examples](examples/) directory for more comprehensive examples and the [documentation](link-to-documentation) for detailed API reference.

## Support and Contributions

For questions, issues, or contributions, please see the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

