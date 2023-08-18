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
        if (mat[row][col] == 1 && !visited.has(`${row},${col}`)) {
            visited.add(`${row},${col}`);
            stack.push([row, col]);
            while (stack.length !== 0) {
                let [curRow, curCol] = stack.pop();
                for (let d = 0; d < 4; d++) {
                    const newRow = curRow + drow[d];
                    const newCol = curCol + dcol[d];
                    if (newRow >= 0 && newRow < maxRow && newCol >= 0 && newCol < maxCol) {
                        if (mat[newRow][newCol] === 1 && !visited.has(`${newRow},${newCol}`)) {
                            stack.push([newRow, newCol]);
                            visited.add(`${newRow},${newCol}`);
                        }
                    }
                }
            }
        }
        anset.add(visited.size);
    }
};

console.log(anset);
