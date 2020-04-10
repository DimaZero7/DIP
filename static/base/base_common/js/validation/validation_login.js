/* ----------------------------

CustomValidation прототип

- Отслеживает список сообщений о недействительности для этого ввода
- Отслеживает, какие проверки достоверности должны быть выполнены для этого ввода
- Выполняет проверки достоверности и отправляет обратную связь в интерфейс

---------------------------- */

function CustomValidation(input) {
    this.invalidities = [];
    this.validityChecks = [];

    // добавить ссылку на входной узел
    this.inputNode = input;

    // триггерный метод для подключения слушателя
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

            } // конец if requireElement
        } // конец для
    },
    checkInput: function () { // checkInput теперь инкапсулирован

        this.inputNode.CustomValidation.invalidities = [];
        this.checkValidity(this.inputNode);

        if (this.inputNode.CustomValidation.invalidities.length === 0 && this.inputNode.value !== '') {
            this.inputNode.setCustomValidity('');
        } else {
            var message = this.inputNode.CustomValidation.getInvalidities();
            this.inputNode.setCustomValidity(message);
        }
    },
    registerListener: function () { // зарегистрируем слушателя здесь

        var CustomValidation = this;

        this.inputNode.addEventListener('keyup', function () {
            CustomValidation.checkInput();
        });


    }

};



/* ----------------------------

Проверка достоверности

Массивы проверок достоверности для каждого входа
Состоит из трех вещей
1. isInvalid () - функция, чтобы определить, удовлетворяет ли входные данные определенному требованию
2. invalididityMessage - сообщение об ошибке для отображения, если поле недействительно
3. элемент - элемент, который устанавливает требование

---------------------------- */

var mailValidityChecks = [
    {
        isInvalid: function (input) {
            return input.value.length < 3;
        },
        invalidityMessage: 'Вы ввели меньше чем 3 символа',
        element: document.querySelector('label[for="mail"] .input-requirements li:nth-child(1)')
	},
    {
        isInvalid: function (input) {
            var illegalCharacters = input.value.match(/^[a-zA-Z0-9.!#$%&*+/=?^_'{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/);
            return illegalCharacters ? false : true;
        },
        invalidityMessage: 'Должена содержать символ @',
        element: document.querySelector('label[for="mail"] .input-requirements li:nth-child(2)')
	}
];

var passwordValidityChecks = [
    {
        isInvalid: function (input) {
            return input.value.length < 8 | input.value.length > 20;
        },
        invalidityMessage: 'Пароль должен содержать от 8 до 20 символов',
        element: document.querySelector('label[for="password"] .input-requirements li:nth-child(1)')
	},
    {
        isInvalid: function (input) {
            return !input.value.match(/[0-9]/g);
        },
        invalidityMessage: 'Введите миним одну цифру',
        element: document.querySelector('label[for="password"] .input-requirements li:nth-child(2)')
	},
    {
        isInvalid: function (input) {
            return !input.value.match(/[aA-zZ]/g);
        },
        invalidityMessage: 'Введите минимум одну букву ',
        element: document.querySelector('label[for="password"] .input-requirements li:nth-child(3)')
	}
];




/* ----------------------------

Настройка CustomValidation

Установите прототип CustomValidation для каждого входа
Также устанавливает, какой массив проверок достоверности использовать для этого ввода

---------------------------- */

var mailInput = document.getElementById('mail');
var passwordInput = document.getElementById('password');

mailInput.CustomValidation = new CustomValidation(mailInput);
mailInput.CustomValidation.validityChecks = mailValidityChecks;

passwordInput.CustomValidation = new CustomValidation(passwordInput);
passwordInput.CustomValidation.validityChecks = passwordValidityChecks;






/* ----------------------------

Слушатели событий

---------------------------- */

var inputs = document.querySelectorAll('input:not([type="submit"])');


var submit = document.querySelector('input[type="submit"]');
var form = document.getElementById('login');

function validate() {
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].CustomValidation.checkInput();
    }
}

submit.addEventListener('click', validate);
form.addEventListener('submit', validate);
