import Axios from "axios";
import router from "@/router"

//Initialize Axios
const axios = Axios.create({
    baseURL: 'http://localhost:5000',

});
// API сервера
export default class API {

    // static async wait(milliseconds) {
    //     return new Promise(resolve => {
    //         setTimeout(resolve, milliseconds)
    //     })
    // }

    static get_sm(word) {
        let resp=""
        axios.post('/api/most_similar',{word:word}).then(response => {
            let data = response.data
            console.log(data)
            resp = data
            // router.push('/').catch(()=>{})
        }).catch(error => {
            // console.log('error')
            console.log(error.status)
        })
        return resp
    }
}