import axios from 'axios';

export const getAllUser = () => {
    return axios.get('http://127.0.0.1:8000/users')
    .then((response) => {
        console.log('user_list:', response.data);
        return response.data;
    })
    .catch((error) => {
        console.error('Error fetching users:', error);
        throw error;
    });
};

export const getCurrency = () => {
    return axios
    .get('http://127.0.0.1:8000/currency/suggest/?query=rub')
    .then((response) => {
        console.log('currency', response.data);
        return response.data
    })
}