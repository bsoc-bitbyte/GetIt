import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://backend-getit.onrender.com/api/',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
