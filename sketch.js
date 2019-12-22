let map;
const rows=8, cols=8;

function setup(){
	my_area = createCanvas(rows*tile_size, cols*tile_size);  // define an area for the html
	my_area.mousePressed(clickListener);

	background(gray);
	map = new Array(cols);
	for (let i=0; i<cols; i++){
		map[i] = new Array(rows);
		for (let j=0; j<rows; j++)
			map[i][j] = new Tile(i, j);
	}

	draw();
}

function draw() {
	for (let row of map) {
		for (let tile of row) {
			tile.draw();
		}
	}
}

function clickListener(){
	let estimateX, estimateY;
	index_x = floor(mouseX/tile_size);
	index_y = floor(mouseY/tile_size);

	map[index_x][index_y].newColor(orange);
}
