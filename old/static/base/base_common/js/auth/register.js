function CustomValidation(input) {
    this.invalidities = [];
    this.validityChecks = [];

    //добавить ссылку на входной узел
    this.inputNode = input;

    //триггерный метод для подключения слушателя
    this.registerListener();
}

CustomValidation.prototype = {
    addInvalidity: function (message) {
        this.invalidities.push(message);
    },
    getInvalidities: function () {
        return this.invalidities.join('. \n');
    },
    checkValidity: function (input) {
        for (var i = 0; i < this.validityChecks.length; i++) {

            var isInvalid = this.validityChecks[i].isInvalid(input);
            if (isInvalid) {
                this.addInvalidity(this.validityChecks[i].invalidityMessage);
            }

            var requirementElement = this.validityChecks[i].element;

            if (requirementElement) {
                if (isInvalid) {
                    requirementElement.classList.add('invalid');
                    requirementElement.classList.remove('valid');
                } else {
                    requirementElement.classList.remove('invalid');
                    requirementElement.classList.add('valid');
                }

            } // конец, если requireElement
        } // коней for
    },
    checkInput: function () { // checkInput now encapsulated

        this.inputNode.CustomValidation.invalidities = [];
        this.checkValidity(this.inputNode);

        if (this.inputNode.CustomValidation.invalidities.length === 0 && this.inputNode.value !== '') {
            this.inputNode.setCustomValidity('');
        } else {
            var message = this.inputNode.CustomValidation.getInvalidities();
            this.inputNode.setCustomValidity(message);
        }
    },
    registerListener: function () { //register the listener here

        var CustomValidation = this;

        this.inputNode.addEventListener('keyup', function () {
            CustomValidation.checkInput();
        });

    }

};


var usernameValidityChecks = [{
        isInvalid: function (input) {
            return input.value.length < 3 | input.value.length > 100;
        },
        invalidityMessage: 'Количество символов от 3 до 100',
        element: document.querySelector('.id_username li:nth-child(1)')
        },
    {
        isInvalid: function (input) {
            var illegalCharacters = input.value.match(/[^a-zA-Z0-9]/g);
            return illegalCharacters ? true : false;
        },
        invalidityMessage: 'Разрешены только буквы и цифры',
        element: document.querySelector('.id_username li:nth-child(2)')
        }
    ];

var passwordValidityChecks = [{
        isInvalid: function (input) {
            return input.value.length < 8 | input.value.length > 100;
        },
        invalidityMessage: 'Этот ввод должен быть от 8 до 100 символов',
        element: document.querySelector('.id_password1 li:nth-child(1)')
        },
    {
        isInvalid: function (input) {
            return !input.value.match(/[a-z]/g);
        },
        invalidityMessage: 'Требуется как минимум 1 строчная буква',
        element: document.querySelector('.id_password1 li:nth-child(2)')
        },
    {
        isInvalid: function (input) {
            return !input.value.match(/[A-Z]/g);
        },
        invalidityMessage: 'Требуется как минимум 1 заглавная буква',
        element: document.querySelector('.id_password1 li:nth-child(3)')
        }
    ];

var passwordRepeatValidityChecks = [{
    isInvalid: function () {
        return passwordRepeatInput.value != passwordInput.value;
    },
    invalidityMessage: 'Пароли должены соответствовать',
    element: document.querySelector('.id_password2 li:nth-child(1)')
    }];

var usernameInput = document.getElementById('id_username');
var passwordInput = document.getElementById('id_password1');
var passwordRepeatInput = document.getElementById('id_password2');

usernameInput.CustomValidation = new CustomValidation(usernameInput);
usernameInput.CustomValidation.validityChecks = usernameValidityChecks;

passwordInput.CustomValidation = new CustomValidation(passwordInput);
passwordInput.CustomValidation.validityChecks = passwordValidityChecks;

passwordRepeatInput.CustomValidation = new CustomValidation(passwordRepeatInput);
passwordRepeatInput.CustomValidation.validityChecks = passwordRepeatValidityChecks;

var inputs = document.querySelectorAll('input:not([type="submit"])');


var submit = document.querySelector('input[type="submit"');
var form = document.getElementById('auth');

function validate() {
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].CustomValidation.checkInput();
    }
}

submit.addEventListener('click', validate);
form.addEventListener('submit', validate);



