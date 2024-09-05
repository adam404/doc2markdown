# 📄 doc2md

`doc2md` is a Python command-line tool that converts various document formats (PDF, PPTX, DOCX) to Markdown. It processes files in a given directory and its subdirectories, maintaining the original folder structure in the output.

## ✨ Features

- 📑 Converts PDF, PPTX, and DOCX files to Markdown format
- 🗂️ Preserves folder structure from input to output
- 💻 Command-line interface for easy use and integration with other tools
- 🔍 Verbose mode for detailed processing information

## ⚙️ Installation

To install `doc2md`, run the following command:

```bash
pip install doc2md
```

This will install `doc2md` along with its dependencies.

## 🚀 Usage

Basic usage:

```bash
doc2md /path/to/input/file.pdf /path/to/output/folder 
```

```bash
doc2md /path/to/input/folder /path/to/output/folder
```

With verbose output:

```bash
doc2md /path/to/input/folder /path/to/output/folder -v
```

For help and more options:

```bash
doc2md --help
```

## 🛠️ Requirements

- Python 3.6+
- PyPDF2
- python-pptx
- python-docx

These dependencies will be automatically installed when you install `doc2md` using pip.

## 🚀 Future Improvements

We're constantly working to improve doc2md. Here are some features and enhancements we're considering for future releases:

### TODO:

- [ ] Implement parallel processing for faster conversion of multiple files
- [ ] Add a progress bar for large batches of file conversions
- [ ] Create a plugin system for easy addition of new file format converters
- [ ] Implement comprehensive unit tests for each converter function
- [ ] Add logging mechanism for better debugging and user feedback
- [ ] Implement input sanitization for enhanced security
- [ ] Add type hints throughout the codebase for improved readability and maintainability
- [ ] Create a CONTRIBUTING.md file with guidelines for contributors

We welcome contributions from the community to help implement these features and improve doc2md. If you're interested in working on any of these tasks, please check our issues page or submit a pull request.

## 📝 Changelog

### [0.1.1] 
- Added File as well as folder support
- Improved the CLI messaging

### [0.1.0] 
- Initial release
- Basic functionality to convert PDF, PPTX, and DOCX files to Markdown
- Command-line interface with verbose mode option

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements 

This tool was inspired by the need for easy conversion of various document formats to Markdown for use with Large Language Models and other text processing applications.
