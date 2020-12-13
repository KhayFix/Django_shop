// смотри документацию django https://docs.djangoproject.com/en/3.1/ref/csrf/

const csrfToken = getCookie('csrftoken');
const cookieCart = JSON.parse(getCookie('cart'));

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

if (!cookieCart) { // если куки корзины пусты мы создаем объект cart
    cart = {}
    console.log('Корзина создана')
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/" // создали куки
}

console.log('Cart:', cookieCart)