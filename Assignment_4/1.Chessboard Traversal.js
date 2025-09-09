

// lets consider the starting color of the chess board is 0, 0  and the starting color in black

// consider from the bottom to top we will be traversing
// on every odd row we print the odd indexed cell and on every even row we print the even indexed cell

let start = 0;

for (let i = 0; i < 6; i++) {
    for ( let j = 0; j < 6; j++) {
        if (i % 2 == 0) {
            // even indexed row
            if (j % 2 == 0) console.log([i, j])
        }
        else {
            if (j % 2 != 0) console.log([i, j])
        }
    }
}