const openModal = (id, btn) => {
    const modal_id = document.getElementById(id)
    const open_btn = document.querySelector(btn)

    open_btn.onclick =() => {
        modal_id.classList.add('active')
        modal_id.classList.add('loud_in')
    }
}

const closeModal = id => {
    const modal_id = document.getElementById(id)
    const close_btn = document.querySelector('.close-modal')

    close_btn.onclick =() => {
        modal_id.classList.remove('active')
        modal_id.classList.remove('loud_in')
    }
}

openModal('modal_singin', '.sing-in')
closeModal('modal_singin')