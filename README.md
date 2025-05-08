# Qt6 Builds

This repository provides automated build scripts for compiling Qt6 (including QtBase and QtTools components) and creating Debian packages (.deb) for multiple Linux distributions. All builds are automated via GitHub Actions and are available in the GitHub Releases section.

## Features

- Automated builds via GitHub Actions
- Debian packages that install Qt6 in `/opt/MediaEase/.binaries/installed/qt6_${VERSION}`
- Support for multiple Linux distributions:
  - Debian 11 (Bullseye)
  - Debian 12 (Bookworm)
  - Ubuntu 22.04 LTS
  - Ubuntu 24.04 LTS
- Multiple version support:
  - Qt 6.4.3
  - Qt 6.5.2
  - Qt 6.8.0
- QtBase and QtTools components included
- Automated metadata generation
- Package signing and verification

## Supported Versions & Distributions

### Detailed Version Support

| Version | Debian 11 | Ubuntu 22.04 | Debian 12 | Ubuntu 24.04 |
|---------|-----------|--------------|-----------|--------------|
| 6.4.3   |     ✔     |      ✔       |     ✘     |      ✘       |
| 6.5.2   |     ✔     |      ✔       |     ✔     |      ✔       |
| 6.8.0   |     ✘     |      ✘       |     ✔     |      ✔       |

## Build Process

The build process is fully automated and includes:
1. Environment setup with all required dependencies
2. Download and compilation of QtBase
3. Download and compilation of QtTools
4. Creation of Debian packages
5. Generation of JSON metadata
6. Automated release creation

## Available Packages

Packages are available in the GitHub Releases of this repository. Each release includes:
- A `.deb` file installable with `dpkg -i`
- A `.json` file containing package metadata
- Documentation and changelog
- Package signatures

### Package Structure

The Debian package installs Qt6 in a dedicated directory structure:
- Base installation path: `/opt/MediaEase/.binaries/installed/qt6_${VERSION}`
- Binaries in `/opt/MediaEase/.binaries/installed/qt6_${VERSION}/usr/bin`
- Libraries in `/opt/MediaEase/.binaries/installed/qt6_${VERSION}/usr/lib`
- Documentation in `/opt/MediaEase/.binaries/installed/qt6_${VERSION}/usr/share/doc/qt6`

The package uses Debian alternatives to manage the binaries, making them available in the system PATH.

## Installation

### Manual Installation
1. Download the appropriate .deb package for your distribution from the [GitHub Releases](../../releases)
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

### Automated Installation
The packages can be installed automatically using the JSON metadata and package management tools.

## Build Configuration

The build process is configured through:
- `build.yaml`: GitHub Actions workflow configuration
- `matrix.py`: Build matrix configuration for different versions and distributions

## Dependencies

The packages require:
- Standard build tools
- C++ compiler with C++17 support

## Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, new features, or improvements.

## Support

For questions, issues, or support, please use the GitHub Issues section of this repository.

## License

This repository is licensed under the terms specified in the LICENSE file.

Qt6 is licensed under the [GNU Lesser General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.html) (LGPL-3.0).
