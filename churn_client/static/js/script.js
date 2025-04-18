document.addEventListener('DOMContentLoaded', function () {
    fetch("/dados_churn/")
        .then(response => response.json())
        .then(data => {
            Plotly.newPlot('grafico_churn', [{
                x: ['Não (0)', 'Sim (1)'],
                y: [data.nao, data.sim],
                type: 'bar',
                marker: {
                    color: ['#007acc', '#ffcc00']
                }
            }], {
                paper_bgcolor: '#2a2a2a',
                plot_bgcolor: '#2a2a2a',
                font: { color: '#fff' },
                title: 'Clientes com e sem Churn'
            });
        });

    fetch("/dados_contrato/")
        .then(response => response.json())
        .then(data => {
            Plotly.newPlot('grafico_contrato', [{
                labels: data.labels,
                values: data.valores,
                type: 'pie',
                marker: {
                    colors: ['#007acc', '#ffcc00', '#22d3ee']
                }
            }], {
                paper_bgcolor: '#2a2a2a',
                font: { color: '#fff' },
                title: 'Distribuição por Tipo de Contrato'
            });
        });

    fetch("/dados_pagamento/")
        .then(response => response.json())
        .then(data => {
            Plotly.newPlot('grafico_pagamento', [{
                x: data.labels,
                y: data.valores,
                type: 'scatter',
                mode: 'lines+markers',
                line: { color: '#ffcc00' }
            }], {
                paper_bgcolor: '#2a2a2a',
                font: { color: '#fff' },
                title: 'Distribuição por Método de Pagamento'
            });
        });
});
