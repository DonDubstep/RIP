import {StockComponent} from "../components/stock/StockComponent1.js";
import {BackButtonComponent} from "../components/back_button/BackButtonComponent.js";
import {MainPage} from "../pages/main/MainPage.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class StockPage {
    constructor(parent, id) {
        this.parent = parent;
        this.id = Number(id);

    }

    async getData() {
        return ajax.get(urls.stock(this.id))
    }

    get page() {
        return document.getElementById('stock-page')
    }

    getHTML() {
        return (
            `
                <div id="stock-page">
                </div>
            `
        )
    }

    clickBack() {
        const mainPage = new MainPage(this.parent)
        mainPage.render()
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const backButton = new BackButtonComponent(this.page)
        backButton.render(this.clickBack.bind(this))

        const data = await this.getData()
        const stock = new StockComponent(this.page)
        stock.render(data.data)
    }
}