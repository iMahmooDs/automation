import os
import re
import sys

def increment_version_code(version_code):
    return version_code + 1

def increment_version_name(version_name, release_type):
    version_parts = version_name.split(".")
    major, minor, fix = [int(part) for part in version_parts]
    if release_type == "major":
        major += 1
        minor = 0
        fix = 0
    elif release_type == "minor":
        minor += 1
        fix = 0
    elif release_type == "fix":
        fix += 1
    else:
        print("Invalid release type.")
        sys.exit(1)
    return f"{major}.{minor}.{fix}"

if __name__ == "__main__":
    path = input("Enter the path of the Android app source code: ")
    if not os.path.exists(path):
        print("The specified path does not exist.")
        sys.exit(1)

    release_type = input("Enter the type of release (major, minor, or fix): ")
    if release_type not in ["major", "minor", "fix"]:
        print("Invalid release type.")
        sys.exit(1)

    build_gradle_path = os.path.join(path, "app", "build.gradle")
    build_gradle_kts_path = os.path.join(path, "app", "build.gradle.kts")
    if not os.path.exists(build_gradle_path) and not os.path.exists(build_gradle_kts_path):
        print("The build.gradle or build.gradle.kts file does not exist.")
        sys.exit(1)
    
    build_gradle_file_path = build_gradle_path if os.path.exists(build_gradle_path) else build_gradle_kts_path

    with open(build_gradle_file_path, "r") as f:
        build_gradle = f.read()

    version_code_match = re.search(r'versionCode (\d+)', build_gradle)
    if not version_code_match:
        print("The versionCode property was not found in the build.gradle file.")
        sys.exit(1)
    version_code = int(version_code_match.group(1))

    version_name_match = re.search(r'versionName "([\d]+\.[\d]+\.[\d]+)"', build_gradle)
    if not version_name_match:
        print("The versionName property was not found in the build.gradle file.")
        sys.exit(1)
    version_name = version_name_match.group(1)

    version_code = increment_version_code(version_code)
    version_name = increment_version_name(version_name, release_type)

    new_build_gradle = re.sub(r'versionCode \d+', f'versionCode {version_code}', build_gradle)
    new_build_gradle = re.sub(r'versionName "(\d+\.\d+\.\d+)"', f'versionName "{version_name}"', new_build_gradle)

    with open(build_gradle_file_path, "w") as f:
        f.write(new_build_gradle)
    print(f"The build.gradle file has been updated with the new versionCode: {version_code} and versionName: {version_name}.")