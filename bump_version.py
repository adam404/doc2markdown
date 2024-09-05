import re
import sys

def bump_version(version_file, bump_type):
    with open(version_file, 'r') as f:
        content = f.read()

    version_pattern = r'__version__\s*=\s*"(\d+)\.(\d+)\.(\d+)"'
    match = re.search(version_pattern, content)
    
    if not match:
        print("Version pattern not found.")
        return

    major, minor, patch = map(int, match.groups())

    if bump_type == 'major':
        major += 1
        minor = patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1

    new_version = f'{major}.{minor}.{patch}'
    new_content = re.sub(version_pattern, f'__version__ = "{new_version}"', content)

    with open(version_file, 'w') as f:
        f.write(new_content)

    print(f"Version bumped to {new_version}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bump_version.py <version_file> <major|minor|patch>")
        sys.exit(1)

    bump_version(sys.argv[1], sys.argv[2])