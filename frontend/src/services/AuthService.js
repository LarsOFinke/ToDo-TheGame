// Created by ChatGPT --> subject to change

import { ref } from "vue";
import api from "@/environments/testing-environment";

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
    } catch (err) {
      error.value = err.response?.data?.message || "Login failed failed for unknown reasons.";
      isAuthenticated.value = false;
    } finally {
      loading.value = false;
    }
  };

  const register = async (username, password) => {
    loading.value = true;
    error.value = null;
    try {
      const response = await api.post("auth/register", { username, password });
      user.value = response.data.user;
      return true;
    } catch (err) {
      error.value = err.response?.data?.message || "Registration failed for unknown reasons.";
      return false;
    } finally {
      loading.value = false;
    }
  };

  const logout = () => {
    api.get("auth/logout").then((response) => {
      if (response.success) {
        user.value = null;
        isAuthenticated.value = false;
      }
    });
  };

  return {
    user,
    isAuthenticated,
    loading,
    error,
    register,
    login,
    logout,
  };
}
