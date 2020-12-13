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
        addCookieItem(productId, action)
    } else {
        updateUserOrder(productId, action)
    }
}

function addCookieItem(productId, action) {
    console.log('Пользователь не авторизован')

    if (action === 'add') {
        if(cookieCart[productId] === undefined) {
            cookieCart[productId] = {'quantity': 1}
        }else {
            cookieCart[productId]['quantity'] += 1
        }
    }

    if(action === 'remove') {
        cookieCart[productId]['quantity'] -= 1

        if(cookieCart[productId]['quantity'] <= 0) {
            console.log("Удаляем элемент")
            delete cookieCart[productId]
        }
    }

    document.cookie = 'cart=' + JSON.stringify(cookieCart) + ';domain=;path=/'
    location.reload()
}

function updateUserOrder(productId, action) {
    //отправка данный на вьюху update_item
    console.log('Пользователь авторизовался')

    let url = '/shop/update-item/'
    let json = {'productId': productId, 'action': action}

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Accept": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify(json),
    })
        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
}

checkButtons()
console.log(updateBtn)
console.log(user)