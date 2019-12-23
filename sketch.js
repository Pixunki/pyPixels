let map;
const board_rows=8, board_cols=8, boards=2;
let last_mouse = [-1,-1];

function setup(){
	my_area = createCanvas(
                boards*board_cols*tile_size+border_size,
                board_rows*tile_size);
	my_area.mousePressed(clickListener,drag=false);

	background(gray);
	map = new Array(boards);
    for (let b=0; b<boards; b++){
        map[b] = new Array(board_cols);
    	for (let i=0; i<board_cols; i++){
    		map[b][i] = new Array(board_rows);
    		for (let j=0; j<board_rows; j++)
    			map[b][i][j] = new Tile(b, i, j);
    	}
    }
	draw();
    update_brush();
}

function draw() {
	for (let board of map) {
    	for (let row of board) {
    		for (let tile of row) {
    			tile.draw();
    		}
    	}
    }
}

function mouseDragged(){
	clickListener(drag=true);
}

function clickListener(drag){
	let estimateX, estimateY;
    let b = 0;
	index_x = floor((mouseX-b*border_size)/tile_size);
    while (index_x >= board_cols) {
        b++;
        index_x = floor((mouseX-b*border_size)/tile_size) - b*board_cols;
    }
	index_y = floor(mouseY/tile_size);

    console.log(index_x, index_y, last_mouse)
    if (index_x != last_mouse[0] || index_y != last_mouse[1]){
        last_mouse = [index_x, index_y]
        map[b][index_x][index_y].mouseClicked(drag);
    }
}

function update_brush(){
    let hex_rgb = document.getElementsByName('rgb')[0].value;
    let nohex_rgb = hex_rgb.slice(1);
    let hex_r = nohex_rgb.slice(0,2);
    let hex_g = nohex_rgb.slice(2,4);
    let hex_b = nohex_rgb.slice(4);

    let r = parseInt(hex_r, 16);
    let g = parseInt(hex_g, 16);
    let b = parseInt(hex_b, 16);
    console.log(hex_r, hex_g, hex_b)
    console.log(r, g, b)
    if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255) {
        brush_color = [0, 0, 0];
    } else {
        brush_color = [r, g, b];
    }
    console.log("new color!", brush_color)
}

function keyPressed(){
    if (key == "c") {
        update_brush()
        console.log("new color!", brush_color)
	}
}
