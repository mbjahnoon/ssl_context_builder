import { BhResturantTemplatePage } from './app.po';

describe('BhResturant App', function() {
  let page: BhResturantTemplatePage;

  beforeEach(() => {
    page = new BhResturantTemplatePage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
