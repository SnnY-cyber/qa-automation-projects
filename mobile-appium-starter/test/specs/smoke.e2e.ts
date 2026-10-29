import HomePage from '../pages/home.page';

describe('Demo app smoke test', () => {
  it('opens the app and shows its primary screen', async () => {
    await HomePage.waitUntilVisible();
    await expect(HomePage.primaryScreen).toBeDisplayed();
  });
});
