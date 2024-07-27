from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="doc2md",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to convert various document formats to Markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/doc2md",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "python-pptx",
        "python-docx",
    ],
    entry_points={
        "console_scripts": [
            "doc2md=doc2md.converter:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
