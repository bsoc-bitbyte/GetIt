import apiClient from './api';
import Cookies from 'js-cookie';

const setAccessToken = (token) => {
  Cookies.set(TOKEN_COOKIE_NAME, token);
};

const getAccessToken = () => {
  return Cookies.get(TOKEN_COOKIE_NAME);
};

const removeAccessToken = () => {
  Cookies.remove(TOKEN_COOKIE_NAME);
};

export const login = async (credentials) => {
  try {
    const response = await apiClient.post('/token/', credentials);
    const { access, refresh } = response.data;
    setAccessToken(access);
    return access;
  } catch (error) {
    console.error('Login failed', error);
    throw error;
  }
};

export const refreshAccessToken = async () => {
  try {
    const refresh = Cookies.get('refresh');
    if (!refresh) {
      throw new Error('Refresh token not found');
    }

    const response = await apiClient.post('/refresh/', { refresh });
    const { access } = response.data;
    setAccessToken(access);
    return access;
  } catch (error) {
    console.error('Token refresh failed', error);
    throw error;
  }
};

export const register = async (userData) => {
  try {
    const response = await apiClient.post('/accounts/', userData);
    const { access, refresh } = response.data;
    setAccessToken(access);
    return access_token;
  } catch (error) {
    console.error('Registration failed', error);
    throw error;
  }
};

export const isAuthenticated = () => {
  return !!getAccessToken();
};
