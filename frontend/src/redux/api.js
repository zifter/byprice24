import axios from "axios";

const instance = axios.create({
    baseURL: "/api/v1/",
})

export const api = {
    searchProducts(query, page, ordering){
        const url = 'search/products?query=' + query +
            '&page=' + page +'&ordering=' + ordering;
        return instance.get(url)
    },
    searchCurrentProduct(id){
        const url = 'products/' + id;
        return instance.get(url)
    },
    searchRecentlyViewedProducts(id){
        const url = 'products?id=' + id.join('&id=');
        return instance.get(url)
    },

    // login(payload) {
    //     return instance.post(`auth/login`, {...payload})
    // },
    // recoverPass(payload) {
    //     return instance.post('auth/forgot', {...payload})
    // },
    // register(payload) {
    //     return instance.post('auth/register', {...payload})
    //
    // },
    // checkMe(payload: {}) {
    //     return instance.post('auth/me', payload)
    // },
    // logout() {
    //     return instance.delete('auth/me')
    // },
    // setNewPassword(data: { password: string, resetPasswordToken: string }) {
    //     return instance.post('auth/set-new-password', data)
    // },
    //
    //

}


