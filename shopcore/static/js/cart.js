const updateBtn = document.querySelectorAll('.update-cart')


// //рабочий метод можно использовать его
// // i += 1 можно заменить на i++
// for (let i = 0; i < updateBtn.length; i += 1) {
//     updateBtn[i].addEventListener('click', function () {
//         let productId = this.dataset.product
//         let action = this.dataset.action
//         console.log('productId:', productId, 'Action:', action)
//     })
// }
function checkButtons() {
    for (let btn of updateBtn) {
    btn.addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

        authorizationCheck(user)
    });
}}


const authorizationCheck = (dataUser) => {
    console.log('USER:', dataUser)
    if (dataUser === "AnonymousUser") {
        console.log('Пользователь не авторизован')
    } else {
        console.log('Пользователь авторизовался')
    }
}

checkButtons()
console.log(updateBtn)
console.log(user)