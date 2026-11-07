const button = document.querySelector('#run-mask-check');
const result = document.querySelector('#mask-check-result');
const names = ['C0.png', 'C1.png', 'C1Live.png'];

button.addEventListener('click', async () => {
  button.disabled = true;
  result.textContent = button.dataset.pending;
  try {
    const images = names.map(name => document.querySelector(`img[src="${name}"]`));
    await Promise.all(images.map(image => image.decode()));
    const {naturalWidth: width, naturalHeight: height} = images[0];
    const canvas = document.createElement('canvas');
    canvas.width = width;
    canvas.height = height;
    const context = canvas.getContext('2d', {willReadFrequently: true});
    const channels = images.map(image => {
      if (image.naturalWidth !== width || image.naturalHeight !== height) {
        throw new Error('Image dimensions differ');
      }
      context.drawImage(image, 0, 0);
      return context.getImageData(0, 0, width, height).data;
    });
    const foreground = [0, 0, 0];
    const differing = [0, 0];
    for (let i = 1; i < channels[0].length; i += 4) {
      const reference = channels[0][i] > 30;
      const cacheOnly = channels[1][i] > 30;
      const live = channels[2][i] > 30;
      foreground[0] += Number(reference);
      foreground[1] += Number(cacheOnly);
      foreground[2] += Number(live);
      differing[0] += Number(reference !== cacheOnly);
      differing[1] += Number(reference !== live);
    }
    result.textContent = `${button.dataset.foreground} C0 = ${foreground[0]}, C1 = ${foreground[1]}, C1Live = ${foreground[2]}. ${button.dataset.difference} C0 ↔ C1 = ${differing[0]}, C0 ↔ C1Live = ${differing[1]}.`;
  } catch {
    result.textContent = button.dataset.error;
  } finally {
    button.disabled = false;
  }
});
