# QA Mobile Appium Starter

A small Appium + WebdriverIO structure for Android UI automation. This is a starter template: it needs an Android app under test and a configured emulator or device before the example can run.

## Prerequisites
- Node.js 20+
- Android Studio, Android SDK and an emulator (or USB debugging enabled device)
- Appium 2 with UiAutomator2 driver
- A demo APK that you are permitted to test

## Setup
```bash
npm install
npx appium driver install uiautomator2
```
Set `APP_PATH` to the local APK path, then start the emulator and run Appium in another terminal:
```bash
$env:APP_PATH = 'C:\path\to\demo.apk'
npx appium
npm test
```
On macOS/Linux, export `APP_PATH` with the shell's normal environment syntax.

The sample test launches an app and checks that its first screen is visible. Replace the package/activity and selector with values from the selected demo app. Do not commit APKs unless licensing allows it.
