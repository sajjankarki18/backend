let emailEL = document.querySelector('.email')
let passwordEL = document.querySelector('.password')
let errorMsgEL = document.querySelector('.error-message')

const emailCondition = /^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$/;

const validate_email = (email) => {

    if(email.length != 0){
        if(emailCondition.test(email.toLowerCase())){
            return true
        }else{
            errorMsgEL.innerHTML = 'Invalid Email Format!'
            return false
        }
    }else{
        errorMsgEL.innerHTML = 'The Email field could not be empty!'
    }
}

const validate_password = (password) => {

    if(password.length != 0){
        if(password.length <= 5){
            errorMsgEL.innerHTML = 'The password must be atleast 6 characters'
            return false
        }else{
            return true
        }
    }else{
        errorMsgEL.innerHTML = 'The password field is empty!'
    }
}
document.querySelector('.js-signup-button').addEventListener('click', (event) => {
    if(!validate_email(emailEL.value) || !validate_password(passwordEL.value)){
        event.preventDefault()
    }else{
        errorMsgEL.value = ''
    }
})