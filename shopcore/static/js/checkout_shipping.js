
if(shipping === "False") {
    document.querySelector('#shipping-info')
        .innerHTML = ''
}

let form = document.querySelector('#form')
form.addEventListener('submit', function (e) {
    e.preventDefault()
    document.querySelector('#form-button').classList.add('hidden')
    document.querySelector('#payment-info').classList.remove('hidden')

})

document.querySelector('#make-payment')
    .addEventListener('click', function (e) {
        submitFormData()
    })

function submitFormData() {
    console.log('Кликнута кнопка оплаты')
}