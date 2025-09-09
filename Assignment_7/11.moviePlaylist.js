const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

function* moviePlayList(movies) {
    
    for (let movie of movies) {
        yield movie
    }

}

async function proc() {
    
    let playlist = moviePlayList(["Avengers", "Inception"]); 
    console.log(playlist.next())
    console.log(playlist.next())
    console.log(playlist.next())
    console.log(playlist.next())

}

async function main(){
    await proc()
    crw.close()
}

main()