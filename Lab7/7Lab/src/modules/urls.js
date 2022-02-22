class Urls {
    constructor() {
        this.url = 'http://localhost:8000/';
    }

    stocks() {
        return `${this.url}Books/`
    }

    stock(id) {
        return `${this.url}Books/${id}/`
    }
}

export const urls = new Urls()