describe('Demo app smoke test', () => {
  it('opens the app and shows its primary screen', async () => {
    const primaryScreen = await $('~home-screen');
    await primaryScreen.waitForDisplayed({ timeout: 20000 });
    await expect(primaryScreen).toBeDisplayed();
  });
});
