let colours_for_tiles = [['rgba(224, 115, 58, 0.8)', 'rgba(224, 115, 58, 0.5)'], ['rgba(82, 161, 157, 0.5)',
    'rgba(82, 161, 157, 0.3)'], ['rgb(224, 115, 58)', 'rgba(224, 115, 58, 0.6)'],
    ['rgb(78, 128, 126)', 'rgba(78, 128, 126, 0.8)']]

function  click_central(event) {
    for (let i=0; i <= 25; i++) {
        let tile = document.getElementById(String(i))
        const min = 0;
        const max = colours_for_tiles.length - 1;
        const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
        tile.style.backgroundColor = colours_for_tiles[randomNum][0]
        tile.addEventListener('mouseover', (event) => {
            let colour_of_tile = getComputedStyle(event.currentTarget).backgroundColor
            for (let i=0; i <= 25; i++) {
                if (colour_of_tile.localeCompare(colours_for_tiles[i][0]) === 0) {
                    event.currentTarget.style.backgroundColor = colours_for_tiles[i][1];
                    break;
                }
            }
        })
        tile.addEventListener('mouseout', (event) => {
            let colour_of_tile = getComputedStyle(event.currentTarget).backgroundColor
            for (let i=0; i <= 25; i++) {
                if (colour_of_tile.localeCompare(colours_for_tiles[i][1]) === 0) {
                    event.currentTarget.style.backgroundColor = colours_for_tiles[i][0];
                    break;
                }
            }
        })
        tile.addEventListener('click', (event) => {
            let colour_of_tile = getComputedStyle(event.currentTarget).backgroundColor
            if (colour_of_tile.localeCompare('rgb(255, 255, 255)') === 0) {
                const min = 0;
                const max = colours_for_tiles.length - 1;
                const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
                event.currentTarget.style.backgroundColor = colours_for_tiles[randomNum][0]
            } else {
                event.currentTarget.style.backgroundColor = 'white'
            }
        })
    }
    let new_elem = document.createElement('div')
    const min = 0;
    const max = colours_for_tiles.length - 1;
    const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
    new_elem.style.backgroundColor = colours_for_tiles[randomNum][0]
    new_elem.addEventListener('click', (event) => {
            let colour_of_tile = getComputedStyle(event.currentTarget).backgroundColor
            if (colour_of_tile.localeCompare('rgb(255, 255, 255)') === 0) {
                const min = 0;
                const max = colours_for_tiles.length - 1;
                const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
                event.currentTarget.style.backgroundColor = colours_for_tiles[randomNum][0]
            } else {
                event.currentTarget.style.backgroundColor = 'white'
            }
        })
    new_elem.addEventListener('mouseover', (event) => {
            let colour_of_tile = getComputedStyle(event.currentTarget).backgroundColor
            for (let i=0; i <= 25; i++) {
                if (colour_of_tile.localeCompare(colours_for_tiles[i][0]) === 0) {
                    event.currentTarget.style.backgroundColor = colours_for_tiles[i][1];
                    break;
                }
            }
        })
   new_elem.addEventListener('mouseout', (event) => {
        let colour_of_tile = getComputedStyle(event.currentTarget).backgroundColor
        for (let i=0; i <= 25; i++) {
            if (colour_of_tile.localeCompare(colours_for_tiles[i][1]) === 0) {
                event.currentTarget.style.backgroundColor = colours_for_tiles[i][0];
                break;
            }
        }
    })
    event.currentTarget.replaceWith(new_elem)
}
document.addEventListener('DOMContentLoaded', (event) => {
    let insert_area = document.getElementById('insert_area')
    for (let i=0; i <= 25; i++) {
        insert_area.insertAdjacentHTML('afterbegin', `<div id=${String(i)} class="no-active"></div>`)
        if (i === 13) {
            let centrall_elem = document.getElementById(String(i))
            centrall_elem.style.background = `#E0733A`
            centrall_elem.addEventListener('click', click_central)
        }
    }
})

document.getElementById('take_result').addEventListener('click', (event) => {
    window.location.reload()
})

