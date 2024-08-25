fetch('/analytics')
  .then(response => response.json())
  .then(data => {
      var ctx = document.getElementById('grievanceChart').getContext('2d');
      var chart = new Chart(ctx, {
          type: 'bar',
          data: {
              labels: data.map(item => item.month),
              datasets: [{
                  label: 'Grievances',
                  data: data.map(item => item.count)
              }]
          }
      });
  });
