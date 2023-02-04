# Update Android App's Version
A Python script that can help Android developers to update the versionCode and versionName without touching build.gradle file.
It can work with both build.gradle and build.gradle.kts files.

## Run the program
### To run this script you need to have Python +v3.x installed in your computer.
```shell
python update-android-version.py
```
or
```git
python3 update-android-version.py
```
First, you will need to add the path of your Android source code:
```git
Enter the path of the Android app source code: C:\Users\mahmo\Desktop\BetterCallSaul
```
Second, type the release type: major, minor, or fix:
```git
Enter the type of release (major, minor, or fix): minor
```
You should get something like this in the terminal:
```git
The build.gradle file has been updated with the new versionCode: 7 and versionName: 2.2.0.
```
Now go and check your build.gradle file if versionCode and versionName got updated.

> Note: this script works with versionName in this format x.y.z , where x,y,z are integers
