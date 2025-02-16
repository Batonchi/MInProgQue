document.getElementById('reg').addEventListener('click', async (event) => {
    event.preventDefault()

    let main_view = document.getElementById('reg_view_container')
    main_view.style.display = null
    main_view.style.visibility = 'hidden'
    let add_special = document.getElementById('view_add')
    add_special.style.display = 'flex'
    add_special.style.visibility = 'visible'


    const reg_form = document.getElementById('registration')

    if (reg_form.password.value !== reg_form.repeat_password.value) {
        alert("Пвроли не совпадают!")
        return
    }
    let response = await fetch(`/registration?first_name=${reg_form.first_name.value}&last_name=${reg_form.last_name.value}&email=${reg_form.email.value}&birth_date=${reg_form.birth_date.value}&password=${reg_form.password.value}`, {
        method: "POST",
    })
    if (response.status == 409) {
        alert("Такой пользователь уже зарегистрирован!")
        return
    } else if (response.status != 200) {
        alert("Ой! Что то пошло не так :(")
        return
    }
    window.location.href="/successfully"
})