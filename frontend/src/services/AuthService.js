// Created by ChatGPT --> subject to change

import { ref } from "vue";
import api from "@/environments/tesing-environment";

const user = ref(null);
const isAuthenticated = ref(false);
const loading = ref(false);
const error = ref(null);

export function useAuthService() {
  const login = async (username, password) => {
    loading.value = true;
    error.value = null;
    try {
      const response = await api.post("auth/login", { username, password });
      user.value = response.data.user;
      isAuthenticated.value = true;
      console.log("SUCCESS");
    } catch (err) {
      error.value = err.response?.data?.message || "Login failed";
      isAuthenticated.value = false;
      console.log("FAILED LOGIN");
    } finally {
      loading.value = false;
    }
  };

  const logout = () => {
    user.value = null;
    isAuthenticated.value = false;
  };

  return {
    user,
    isAuthenticated,
    loading,
    error,
    login,
    logout,
  };
}
