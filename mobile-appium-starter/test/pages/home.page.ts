class HomePage {
  get primaryScreen() {
    return $('~home-screen');
  }

  async waitUntilVisible() {
    await this.primaryScreen.waitForDisplayed({ timeout: 20000 });
  }
}

export default new HomePage();
