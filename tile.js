const tile_size=20, border_size=5;
const green=[90,200,90], purple=[150,50,200], gray=[100,100,100], poop=[128,0,0], red=[255,0,0], orange=[255,165,0], yellow=[255,255,0];
let brush_color=[0,0,0];

class Tile {
	constructor(board_n, pos_x, pos_y, color="checkers"){
		this.coords = [pos_x, pos_y]
		this.b = board_n;
		this.x = [this.x1, this.x2] =
			[
				this.b*8*tile_size + tile_size*pos_x + border_size*this.b,
				this.b*8*tile_size + tile_size*pos_x+tile_size + border_size*this.b
			];
		this.y = [this.y1, this.y2] = [tile_size*pos_y, tile_size*pos_y+tile_size];
		//this.border_size = border_size;

		if (color == "checkers"){
			if ((pos_x+pos_y)%2 == 0){
				this.color = [200,200,200];
			} else {
				this.color = [250,250,250];
			}
		} else {
			this.color = color;
		}
		this.default_color = this.color;
	}

	newColor(color){
		this.color = color;
	}

	draw(){
		noStroke();
		fill(this.color);
		this.rect = rect(this.x1, this.y1, (this.x2-this.x1), (this.y2-this.y1));
	}

	mouseClicked(){
		if (this.color == this.default_color) {
			this.newColor(brush_color);
		} else {
			this.newColor(this.default_color);
		}
		console.log("http://pixel.rogerio.no/pypixels/GET?board="+this.b+"&row="+this.coords[1]+"&col="+this.coords[0]+"&0xFFFF00");
	}
}
