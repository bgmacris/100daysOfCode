var myCanvas = document.getElementById("myCanvas");
myCanvas.width = 500;
myCanvas.height = 500;

var ctx = myCanvas.getContext("2d");


function drawLine(ctx, startX, startY, endX, endY, color) {
    ctx.save();
    ctx.strokeStyle = color;
    ctx.beginPath();
    ctx.moveTo(startX, startY);
    ctx.lineTo(endX, endY);
    ctx.stroke();
    ctx.restore();
}


function drawBar(ctx, upperLeftCornerX, upperLeftCornerY, width, height, color) {
    ctx.save();
    ctx.fillStyle = color;
    ctx.fillRect(upperLeftCornerX, upperLeftCornerY, width, height);
    ctx.restore();
}



var myData = {
    "Barcelona": 101,
    "Madrid": 30,
    "valencia": 2,
    "Colombia": 23,
    "Sevilla": 10
};

var Barchart = function (options) {
    this.options = options;
    this.canvas = options.canvas;
    this.ctx = this.canvas.getContext("2d");
    this.colors = options.colors;

    this.draw = function () {
        var maxValue = 0;
        for (var categ in this.options.data) {
            maxValue = Math.max(maxValue, this.options.data[categ]);
        }
        var canvasActualHeight = this.canvas.height - this.options.padding * 2;
        var canvasActualWidth = this.canvas.width - this.options.padding * 2;

        // Dibujar lineas
        var gridValue = 0;
        while (gridValue <= maxValue) {
            var gridY = canvasActualHeight * (1 - gridValue / maxValue) + this.options.padding;
            drawLine(
                this.ctx,
                0,
                gridY,
                this.canvas.width,
                gridY,
                this.options.gridColor
            );

            this.ctx.save();
            this.ctx.fillStyle = this.options.gridColor;
            this.ctx.font = "bold 10px Arial";
            this.ctx.fillText(gridValue, 10, gridY - 2);
            this.ctx.restore();

            gridValue += this.options.gridScale;
        }

        // Dibujar barras
        var barIndex = 0;
        var numberOfBars = Object.keys(this.options.data).length;
        var barSize = (canvasActualWidth) / numberOfBars;

        for (categ in this.options.data) {
            var val = this.options.data[categ];
            var barHeight = Math.round(canvasActualHeight * val / maxValue);
            drawBar(
                this.ctx,
                this.options.padding + barIndex * barSize + 25,
                this.canvas.height - barHeight - this.options.padding,
                barSize,
                barHeight,
                this.colors[barIndex % this.colors.length]
            );

            // Test escribir nombre
            this.ctx.save();
            this.ctx.font = "bold 10px Arial";
            this.ctx.fillText(this.options.data[categ], (this.options.padding + barIndex * barSize) + barSize / 2 + 15 , this.canvas.height - barHeight - this.options.padding - 5);
            // console.log(this.options.padding, barIndex, barSize, barSize / 2)
            this.ctx.restore();

            barIndex++;
        }

        // Nombre de serie grafica
        this.ctx.save();
        this.ctx.textBaseline = "bottom";
        this.ctx.textAlign = "center";
        this.ctx.fillStyle = "#000000";
        this.ctx.font = "bold 14px Arial";
        this.ctx.fillText(this.options.seriesName, this.canvas.width / 2, this.canvas.height);
        this.ctx.restore();


        // Leyenda
        barIndex = 0;
        var legend = document.querySelector("legend[for='myCanvas']");
        var ul = document.createElement("ul");
        legend.append(ul);
        for (categ in this.options.data) {
            var li = document.createElement("li");
            li.style.listStyle = "none";
            li.style.borderLeft = "20px solid " + this.colors[barIndex % this.colors.length];
            li.style.padding = "5px";
            li.textContent = categ;
            ul.append(li);
            barIndex++;
        }
    }
}


var myBachart = new Barchart(
    {
        canvas: myCanvas,
        seriesName: "myData",
        padding: 20,
        gridScale: 5,
        gridColor: "#666262",
        data: myData,
        colors: ["#a55ca5", "#67b6c7", "#bccd7a", "#eb9743"]
    }
);
myBachart.draw();