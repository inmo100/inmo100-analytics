document.addEventListener("click", (e) => {
  const selector = '.form-block.checkbox';
  const closest = e.target.closest(selector);

  document.querySelectorAll(selector).forEach(element => element.classList.remove('active'));

  if (closest) closest.classList.add('active');
});

const createChart = ({type, datasets}) => {
  const canvas = document.querySelector("#chart-canvas").getContext('2d');
  if (!canvas) return console.log('Make sure that the element is a canvas');

  let chart = Chart.getChart(canvas);

  if (chart != undefined) chart.destroy();

  const autocolors = window['chartjs-plugin-autocolors'];
  Chart.register(autocolors);

  chart = new Chart(canvas, {
    type,
    data: {
      datasets,
    },
    options: {
      plugins: {
        autocolors: {
          enabled: true,
          mode: 'data',
        },
      },
    }
  });
}