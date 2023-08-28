import axios from "axios";
const BASE_LOCALHOST_URL = 'http://localhost:8000/'

const Header = {
    Authorization : 'Authorization',
}

export const fetchDataFromApiLocal = async (url , params)=> {
    try{
        const req = await axios.get(`${BASE_LOCALHOST_URL}${url}` , {})

        return req.data
    } catch (err) {
        console.log(err);
        return null
    }
}


// export const fetchDataFromApiLocal = async (url , params)=> {
//     try{
//         const req = await axios.get(`${BASE_LOCALHOST_URL}${url}` , {})

//         return req
//     } catch (err) {
//         console.log(err);
//         return err
//     }
// }

export const fetchDataFromConstumeBaseUrl = (baseUrl ,  url , params) => {
    
}