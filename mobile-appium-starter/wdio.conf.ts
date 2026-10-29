import type { Options } from '@wdio/types';

export const config: Options.Testrunner = {
  runner: 'local',
  specs: ['./test/specs/**/*.ts'],
  maxInstances: 1,
  framework: 'mocha',
  reporters: ['spec'],
  services: ['appium'],
  port: 4723,
  capabilities: [{
    platformName: 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:deviceName': process.env.ANDROID_DEVICE_NAME || 'Android Emulator',
    'appium:app': process.env.APP_PATH,
    'appium:autoGrantPermissions': true,
    'appium:newCommandTimeout': 120,
  }],
  mochaOpts: { timeout: 90000 },
};
