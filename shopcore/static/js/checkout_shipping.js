let userFormData = {
    'name': null,
    'email': null,
    'total': total,
};

let userShippingInfo = {
    'address': null,
    'city': null,
    'state': null,
    'zipcode': null,
};

if (shipping === "False") {
    document.querySelector('#shipping-info')
        .innerHTML = ''
}

//Если пользователь не авторизован, то поля имя и email присутствуют.
if (user !== 'AnonymousUser') {
    document.querySelector('#user-info')
        .innerHTML = ''
}

if (shipping === "False" && user !== "AnonymousUser") {
    document.querySelector("#form-wrapper").classList.add('hidden');
    document.querySelector("#payment-info").classList.remove('hidden');

}

let form = document.querySelector('#form')
form.addEventListener('submit', function (e) {
    e.preventDefault();
    document.querySelector('#form-button').classList.add('hidden');
    document.querySelector('#payment-info').classList.remove('hidden');

})

document.querySelector('#make-payment')
    .addEventListener('click', function (e) {
        submitFormData()
    });

function submitFormData() {
    console.log('Кликнута кнопка оплаты')

    if (shipping !== 'False') {
        userShippingInfo.address = form.address.value
        userShippingInfo.city = form.city.value
        userShippingInfo.state = form.state.value
        userShippingInfo.zipcode = form.zipcode.value
    }

    if (user === "AnonymousUser") {
        userFormData.name = form.name.value
        userFormData.email = form.email.value
    }
}