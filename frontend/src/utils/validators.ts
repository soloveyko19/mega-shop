import type { credentials, product } from "./types"

export function validateUsername(username: credentials["username"]) {
    if (username.length < 3) {
        throw new Error("Username should contain at least 3 characters.")
    } 
    if (username.includes(" ")) {
        throw new Error("Username cannot contain spaces.")
    }
    if (!/^[a-z0-9_.]+$/.test(username)) {
        throw new Error("Username should contain only latin characters, numbers, underscores and dots.")
    }
    if (username.startsWith(".") || username.endsWith(".")) {
        throw new Error("Username cannot start or end with dots.")
    }
    if (username.includes('..')) {
        throw new Error("Username cannot contain two or more dots in a row.")
    }
    return true
}


export function validatePassword(password: credentials["password"]) {
    const specialChars = "!@#$%^&*()_+=-{}[]\\|/?.`~";

    let hasSpecialChar = false;
    let hasUpperCase = false;
    let hasLowerCase = false;

    for (let char of password) {
        if (specialChars.includes(char)) {
            hasSpecialChar = true;
        } else if (char === char.toUpperCase() && isNaN(Number(char))) {
            hasUpperCase = true;
        } else if (char === char.toLowerCase() && isNaN(Number(char))) {
            hasLowerCase = true;
        }
        if (hasSpecialChar && hasUpperCase && hasLowerCase) {
            break;
        }
    }

    if (password.length < 8) {
        throw new Error("Password should contain at least 8 characters");
    }

    if (!hasSpecialChar) {
        throw new Error("Password should contain at least 1 special character");
    }
    if (!hasUpperCase) {
        throw new Error("Password should contain at least 1 uppercase character");
    }
    if (!hasLowerCase) {
        throw new Error("Password should contain at least 1 lowercase character");
    }

    return true;
}


export function validateProduct(toValidate: product) {
    if (toValidate.title.length < 3) {
        throw new Error('Product title should contain at least 3 characters')
    }
    if (toValidate.title.length > 100) {
        throw new Error('Product title can contain maximum 100 characters')
    }
    if (toValidate.description.length < 1) {
        throw new Error('Product description should contain at least 1 character')
    }
    if (toValidate.description.length > 4000) {
        throw new Error('Product description can contain maximum 4000 characters')
    }
    if (toValidate.category_id == 0) {
        throw new Error('Product category must be selected')
    }
    if (toValidate.price == 0) {
        throw new Error('Product price cannot be zero')
    }
    if (toValidate.price.toString().replace('.', '').length > 15) {
        throw new Error('Product price cannot contain more than 15 digits')
    }
    try {
        new URL(toValidate.image_url)
    } catch (_) {
        throw new Error('Product image url is not valid')
    }

}