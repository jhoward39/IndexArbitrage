function renderStockChart(dateAddedToSP, pricingData, tickerId) {
    const chartContainer = document.getElementById(tickerId);

    console.log(pricingData)
    const margin = { top: 2, right: 2, bottom: 2, left: 2 };
    const width = 300;
    const height = 90;

    const svg = d3.select(chartContainer)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .attr('transform', `translate(${margin.left}, ${margin.top})`);

    const xScale = d3.scaleTime()
        .domain([new Date(pricingData[0].date), new Date(pricingData[pricingData.length - 1].date)])
        .range([0, width]);

    const yScale = d3.scaleLinear()
        .domain([0, d3.max(pricingData, d => d.price)])
        .range([height, 0]);

    const line = d3.line()
        .x(d => xScale(new Date(d.date)))
        .y(d => yScale(d.price));

    svg.append('line')
        .attr('x1', xScale(new Date(dateAddedToSP)))
        .attr('x2', xScale(new Date(dateAddedToSP)))
        .attr('y1', 0)
        .attr('y2', height)
        .attr('stroke', 'navy')
        .attr('stroke-width', 2);

    svg.append('path')
        .datum(pricingData)
        .attr('fill', 'none')
        .attr('stroke', 'grey')
        .attr('stroke-width', 2)
        .attr('d', line);
}