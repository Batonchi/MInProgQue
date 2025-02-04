document.getElementById('like').addEventListener('click', (event) => {
    let elem = document.getElementById('like')
    if (elem.title == 'no-active') {
        elem.style.backgroundImage = 'url("/static/images/tasks/heart.svg")'
        elem.title = 'active'
    } else {
        elem.style.backgroundImage = 'url("/static/images/tasks/no-active_heart.svg")'
        elem.title = 'no-active'
    }
})