async function loadSummary() {
    const response = await fetch('/summary');
    const data = await response.json();

    document.getElementById('totalSales').textContent =
        '$' + data.total_predicted_sales.toLocaleString();

    document.getElementById('avgSales').textContent =
        '$' + data.average_monthly_sales.toLocaleString();

    document.getElementById('maxSales').textContent =
        '$' + data.highest_monthly_sales.toLocaleString();

    document.getElementById('minSales').textContent =
        '$' + data.lowest_monthly_sales.toLocaleString();
}

async function loadForecast() {
    const response = await fetch('/forecast');
    const data = await response.json();

    const months = data.map(item => item.Month);
    const sales = data.map(item => item["Predicted Sales"]);

    const trace = {
        x: months,
        y: sales,
        type: 'scatter',
        mode: 'lines+markers',
        name: 'Forecast'
    };

    const layout = {
        title: '12-Month Sales Forecast',
        xaxis: {
            title: 'Month'
        },
        yaxis: {
            title: 'Sales'
        }
    };

    Plotly.newPlot('chart', [trace], layout);
}

// Load dashboard data when page opens
loadSummary();
loadForecast();