const updateBtn = document.querySelectorAll('.update-cart')

// //рабочий метод можно использовать его
// // i += 1 можно заменить на i++
// for (let i = 0; i < updateBtn.length; i += 1) {
//     updateBtn[i].addEventListener('click', function () {
//         let productId = this.dataset.product
//         let action = this.dataset.action
//         console.log('productId:', productId, 'Action:', action)
//         authorizationCheck(user, productId, action)
//     })
// }

function checkButtons() {
    for (let btn of updateBtn) {
        btn.addEventListener('click', function () {
            let productId = this.dataset.product
            let action = this.dataset.action
            console.log('productId:', productId, 'Action:', action)

            authorizationCheck(user, productId, action)
        });
    }
}

const authorizationCheck = (dataUser, productId, action) => {
    console.log('USER:', dataUser)
    if (dataUser === "AnonymousUser") {
        console.log('Пользователь не авторизован')
    } else {
        updateUserOrder(productId, action)
    }
}

function updateUserOrder(productId, action) {
    //отправка данный на вьюху update_item
    console.log('Пользователь авторизовался')

    let url = 'update-item/'
    let jsonString = JSON.stringify({'productId': productId, 'action': action})

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: jsonString,
    })
        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data:', data)
        })
}

checkButtons()
console.log(updateBtn)
console.log(user)