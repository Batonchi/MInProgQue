document.getElementById('open_selector_of_task').addEventListener('click',
    (event) => {
        let field = document.querySelector('.selector_task')
        field.style.visibility = 'visible'
        field.style.display = 'flex'
        document.getElementById('first_vis').style.visibility = 'hidden'

    })

document.getElementById('exit').addEventListener('click', (event) => {
    let field = document.querySelector('.selector_task')
    field.style.visibility = 'hidden'
    field.style.display = 'none'
    document.getElementById('first_vis').style.visibility = 'visible'
})

let groups = document.querySelectorAll('.group_name')
for (let group of groups) {
    group.addEventListener('click', (event) => {
        let parent_elem = document.getElementById(event.target.parentElement.id)
        let elems = parent_elem.querySelectorAll('.scroll-elem')
        for (let elem of elems) {
            if (getComputedStyle(elem).visibility == 'hidden') {
                parent_elem.querySelector('h3').style.width = '1200px'
                elem.style.visibility = 'visible'
                elem.style.display = 'flex'
            } else {
                parent_elem.querySelector('h3').style.marginRight = '20px'
                elem.style.visibility = 'hidden'
                elem.style.display = 'none'
            }
        }
})
}
