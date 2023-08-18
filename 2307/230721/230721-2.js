const map = ["110011000",
             "110001000",
             "100000000",
             "000000100",
             "000011110",
             "100000000",
             "110000110",
            ]

let mat = [];
for (let i = 0; i < map.length; i++) {
    mat.push(map[i].split("").map(Number));
}

const drow = [-1, 0, 1, 0];
const dcol = [0, 1, 0, -1];

const maxRow = mat.length;
const maxCol = mat[0].length;
const anset = new Set();


for (let row = 0; row < maxRow; row++) {
    for (let col = 0; col < maxCol; col++) {
        let stack = [];
        let visited = new Set();
        if (mat[row][col] == 1 && visited.has([row,col]) === false) {
            visited.add([row,col]);
            stack.push([row,col]);
            while (true) {
                if (stack.length === 0) {
                    break;
                }
                let [curRow, curCol] = stack.pop();

                for (let d = 0; d < 4; d++) {
                    if (0<=curRow+drow[d] && curRow+drow[d] < maxRow && 0<=curCol+dcol[d] && curCol+dcol[d] < maxCol) {
                        if (mat[curRow+drow[d]][curCol+dcol[d]] == 1 && visited.has([curRow+drow[d],curCol+dcol[d]]) === false) {
                            stack.push([curRow+drow[d],curRow+drow[d]]);
                            visited.add([curRow+drow[d],curRow+drow[d]]);
                        }
                    }    
                }
            }
        }
        anset.add(visited.length);
    }
};

console.log(anset)
