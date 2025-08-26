# Debian Package Statistics Analyzer

A Python command-line tool that downloads and analyzes Debian package Contents files to display statistics about packages with the most associated files.

## Overview

This tool connects to a Debian mirror, downloads the compressed Contents file for a specified architecture, and analyzes which packages contain the most files. This is useful for understanding package complexity and system footprint.

## Design Approach

### Architecture

The solution follows object-oriented design principles with clear separation of concerns:

1. **`ContentsDownloader`**: Handles all network operations
   - Downloads compressed Contents files from Debian mirrors
   - Provides progress feedback for large downloads
   - Handles decompression of gzipped files

2. **`ContentsFileParser`**: Parses and analyzes Contents files
   - Efficiently processes large files line by line
   - Extracts package names from qualified package specifications
   - Maintains statistics using a dictionary for O(1) lookups

3. **`PackageStats`**: Data class for clean data representation
   - Type-safe container for package statistics
   - Enables easy sorting and formatting

### Key Design Decisions

1. **Streaming Processing**: The parser processes files line by line rather than loading everything into memory, allowing it to handle large Contents files (typically 30-100 MB compressed, 300+ MB uncompressed).

2. **Error Handling**: Comprehensive error handling with informative messages:
   - Network errors (connection issues, timeouts)
   - HTTP errors (404 for unknown architectures)
   - Decompression errors
   - Parsing errors (malformed lines are skipped)

3. **Logging**: Structured logging provides visibility into the process:
   - INFO level for major operations
   - DEBUG level for detailed progress
   - ERROR level for failures

4. **Type Hints**: Full type annotations for better code maintainability and IDE support.

5. **Testing**: Unit tests cover core parsing logic with mock data.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd debian-package-statistics
```

2. Make the script executable:
```bash
chmod +x package_statistics.py
```

3. Install development dependencies 
```bash
pip install -r requirements.txt
```

## Usage

1. Basic usage:
```bash
./package_statistics.py amd64
```

2. Show top 20 packages:
```bash
./package_statistics.py amd64 -n 20
```

3. Use a different mirror:
```bash
./package_statistics.py arm64 -m http://ftp.debian.org/debian/dists/stable/main/
```

4. Enable verbose output:
```bash
./package_statistics.py amd64 -v
```

## Supported Architectures

1. amd64 - 64-bit x86 (most common)
2. arm64 - 64-bit ARM
3. armhf - 32-bit ARM hard float
4. i386 - 32-bit x86
4. ppc64el - PowerPC 64-bit little-endian
5. s390x - IBM System z

## Testing

1. Run unit tests:
```bash
python -m pytest tests/
```

2. Run with coverage:
```bash
python -m pytest tests/ --cov=package_statistics
```

## Time 

The development of this assesment took approximately 2 hours, broken down as follows:
- Research and understanding the task (15 minutes)
- Core implementation (45 minutes)
- Error handling and edge cases (30 minutes)
- Testing and validation (15 minutes)
- Documentation and some code cleanup (15-30 minutes)

## Performance 

1. Memory Usage: The tool uses approximately 500-600 MB of RAM for processing a typical amd64 Contents file

2. Download Time: Depends on network speed; typically 10-30 seconds for a ~40 MB compressed file in my personal case

3. Processing Time: Usually 5-10 seconds to parse a full Contents file

### Future Improvements

1. Caching: Cache downloaded Contents files to avoid repeated downloads
2. Parallel Processing: Use multiprocessing for parsing very large files
3. Multiple Architectures: Support analyzing multiple architectures simultaneously
4. Export Formats: Add JSON/CSV export options
5. Incremental Updates: Support for diff files to update statistics incrementally
6. Database Backend: Store historical data for trend analysis

### Author
Robert-George Leustean